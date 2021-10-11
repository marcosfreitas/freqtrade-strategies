# pragma pylint: disable=missing-docstring, invalid-name, pointless-string-statement
# flake8: noqa: F401

# --- Do not remove these libs ---
import numpy as np  # noqa
import pandas as pd  # noqa
from pandas import DataFrame

from freqtrade.strategy import (BooleanParameter, CategoricalParameter, DecimalParameter,
                                IStrategy, IntParameter)

# --------------------------------
# Add your lib to import here
import talib.abstract as ta
import freqtrade.vendor.qtpylib.indicators as qtpylib
from functools import reduce

class GlobinsGold(IStrategy):
    """
    Globin's Gold
    author@: Marcos Freitas
    github@: https://github.com/marcosfreitas/freqtrade-strategies

    @todo improve description
    This strategy file combines these trading strategies:
    - 3 SMAs Crossovers
      a bearing exchanging technique set on X,Y,Z periods (based on hyperopt results, by default It is 30, 50 and 100).

    Ps.: Buy hyperspace params, optimized by SharpeHyperOptLossDaily loss function.
    Loaded from GlobinsGold.json

    How to use it?
    > python3 ./freqtrade/main.py -s GlobinsGold
    """
    # Strategy interface version - allow new iterations of the strategy interface.
    # Check the documentation or the Sample strategy to get the latest version.
    INTERFACE_VERSION = 2

    # Minimal ROI designed for the strategy.
    # This attribute will be overridden if the config file contains "minimal_roi".

    minimal_roi = {
       "0": 0.178,
       "24": 0.084,
       "36": 0.028,
       "130": 0
    }

    # Optimal stoploss designed for the strategy.
    # This attribute will be overridden if the config file contains "stoploss".
    # Immediate sell if the profit dips below -28% for a given trade.
    stoploss = -0.286

    # Trailing stoploss
    trailing_stop = True
    trailing_stop_positive = 0.091
    trailing_stop_positive_offset = 0.127 # Disabled / not configured
    trailing_only_offset_is_reached = False

    # Optimal timeframe for the strategy.
    timeframe = '5m'

    # Run "populate_indicators()" only for new candle.
    process_only_new_candles = False

    # These values can be overridden in the "ask_strategy" section in the config.
    use_sell_signal = True
    sell_profit_only = False
    sell_profit_offset = 0.05
    ignore_roi_if_buy_signal = False

    # Number of candles the strategy requires before producing valid signals
    startup_candle_count: int = 100

    # Optional order type mapping.
    # @todo test change limit to market
    order_types = {
        'buy': 'limit',
        'sell': 'limit',
        'stoploss': 'market',
        'stoploss_on_exchange': False
    }

    # Optional order time in force.
    order_time_in_force = {
        'buy': 'gtc',
        'sell': 'gtc'
    }

    plot_config = {
        "main_plot": {
            "sma_5": {
                "color": "#Eedb0b",
                "type": "line"
            },
            "sma_20": {
                "color": "#4c9dcb",
                "type": "line"
            },
            "ema_short_5": {
                "color": "#D30bee",
                "type": "line"
            }
        },
        "subplots": {
            "RSI": {
                "rsi": {
                    "color": "#edc618",
                    "type": "line"
                }
            }
        }
    }

    buy_rsi_enabled = BooleanParameter(default=True, space="buy")
    buy_ema_enabled = BooleanParameter(default=False, space="buy")
    buy_3sma_enabled = BooleanParameter(default=False, space="buy")
    buy_2sma_enabled = BooleanParameter(default=True, space="buy")
    buy_cdl_hammer_enabled = BooleanParameter(default=False, space="buy")

    sell_rsi_enabled = BooleanParameter(default=True, space="sell")
    sell_ema_enabled = BooleanParameter(default=False, space="sell")
    sell_3sma_enabled = BooleanParameter(default=False, space="sell")
    sell_2sma_enabled = BooleanParameter(default=True, space="sell")
    sell_cdl_hammer_enabled = BooleanParameter(default=False, space="sell")

    rsi_overbought_limit = 70
    rsi_oversell_limit = 20
    # the difference between the RSI line and the overbought / oversell line
    rsi_proximity_boundaries = 10


    buy_ema_short = IntParameter(3, 19, default=19, space="buy")
    buy_3sma_short = IntParameter(3, 5, default=5, space="buy")
    buy_3sma_medium = IntParameter(5, 10, default=10, space="buy")
    buy_3sma_long = IntParameter(10, 20, default=20, space="buy")

    sell_ema_short = IntParameter(3, 19, default=19, space="sell")
    sell_3sma_short = IntParameter(3, 5, default=5, space="sell")
    sell_3sma_medium = IntParameter(5, 10, default=10, space="sell")
    sell_3sma_long = IntParameter(10, 20, default=20, space="sell")

    buy_trigger = CategoricalParameter([
        "bb_lower",
        "macd_cross_signal",
        "elders_moment"
    ], default="bb_lower", space="buy")

    sell_trigger = CategoricalParameter([
        "bb_lower",
        "macd_cross_signal",
        "elders_moment"
    ], default="bb_lower", space="sell")

    cooldown_lookback = IntParameter(2, 48, default=2, space="protection", optimize=False)

    use_lowprofit_protection = BooleanParameter(default=True, space="protection", optimize=True)
    use_stoploss_protection = BooleanParameter(default=True, space="protection", optimize=True)

    low_profit_lookback = IntParameter(2, 60, default=20, space="protection", optimize=False)
    low_profit_stop_duration = IntParameter(12, 200, default=20, space="protection", optimize=False)
    low_profit_min_req = DecimalParameter(-0.05, 0.05, default=-0.05, space="protection", decimals=2, optimize=False)

    stoploss_lookback = IntParameter(2, 60, default=10, space="protection", optimize=True)
    stoploss_stop_duration = IntParameter(12, 200, default=20, space="protection", optimize=True)

    @property
    def protections(self):
        prot = []

        prot.append({
            "method": "CooldownPeriod",
            "stop_duration_candles": self.cooldown_lookback.value
        })

        if self.use_lowprofit_protection.value:
            prot.append({
                "method": "LowProfitPairs",
                "lookback_period_candles": self.low_profit_lookback.value,
                "trade_limit": 1,
                "stop_duration": self.low_profit_stop_duration.value,
                "required_profit": self.low_profit_min_req.value
            })

        if self.use_stoploss_protection.value:
            prot.append({
                "method": "StoplossGuard",
                "lookback_period_candles": self.stoploss_lookback.value,
                "trade_limit": 1,
                "stop_duration_candles": self.stoploss_stop_duration.value,
                "only_per_pair": True
            })

        return prot

    def informative_pairs(self):
        """
        Define additional, informative pair/interval combinations to be cached from the exchange.
        These pair/interval combinations are non-tradeable, unless they are part
        of the whitelist as well.
        For more information, please consult the documentation
        :return: List of tuples in the format (pair, interval)
            Sample: return [("ETH/USDT", "5m"),
                            ("BTC/USDT", "15m"),
                            ]
        """
        return []

    def populate_indicators(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        """
        Adds several different TA indicators to the given DataFrame

        Performance Note: For the best performance be frugal on the number of indicators
        you are using. Let uncomment only the indicator you are using in your strategies
        or your hyperopt configuration, otherwise you will waste your memory and CPU usage.
        :param dataframe: Dataframe with data from the exchange
        :param metadata: Additional information, like the currently traded pair
        :return: a Dataframe with all mandatory indicators for the strategies
        """

        # Momentum Indicators
        # ------------------------------------

        # MOM
        dataframe['mom'] = ta.MOM(dataframe,14)

        # ADX
        #dataframe['adx'] = ta.ADX(dataframe)

        # # Plus Directional Indicator / Movement
        # dataframe['plus_dm'] = ta.PLUS_DM(dataframe)
        # dataframe['plus_di'] = ta.PLUS_DI(dataframe)

        # # Minus Directional Indicator / Movement
        # dataframe['minus_dm'] = ta.MINUS_DM(dataframe)
        # dataframe['minus_di'] = ta.MINUS_DI(dataframe)

        # # Aroon, Aroon Oscillator
        # aroon = ta.AROON(dataframe)
        # dataframe['aroonup'] = aroon['aroonup']
        # dataframe['aroondown'] = aroon['aroondown']
        # dataframe['aroonosc'] = ta.AROONOSC(dataframe)

        # # Awesome Oscillator
        # dataframe['ao'] = qtpylib.awesome_oscillator(dataframe)

        # # Keltner Channel
        # keltner = qtpylib.keltner_channel(dataframe)
        # dataframe["kc_upperband"] = keltner["upper"]
        # dataframe["kc_lowerband"] = keltner["lower"]
        # dataframe["kc_middleband"] = keltner["mid"]
        # dataframe["kc_percent"] = (
        #     (dataframe["close"] - dataframe["kc_lowerband"]) /
        #     (dataframe["kc_upperband"] - dataframe["kc_lowerband"])
        # )
        # dataframe["kc_width"] = (
        #     (dataframe["kc_upperband"] - dataframe["kc_lowerband"]) / dataframe["kc_middleband"]
        # )

        # # Ultimate Oscillator
        # dataframe['uo'] = ta.ULTOSC(dataframe)

        # # Commodity Channel Index: values [Oversold:-100, Overbought:100]
        # dataframe['cci'] = ta.CCI(dataframe)

        # RSI
        dataframe['rsi'] = ta.RSI(dataframe)

        # # Inverse Fisher transform on RSI: values [-1.0, 1.0] (https://goo.gl/2JGGoy)
        # rsi = 0.1 * (dataframe['rsi'] - 50)
        # dataframe['fisher_rsi'] = (np.exp(2 * rsi) - 1) / (np.exp(2 * rsi) + 1)

        # # Inverse Fisher transform on RSI normalized: values [0.0, 100.0] (https://goo.gl/2JGGoy)
        # dataframe['fisher_rsi_norma'] = 50 * (dataframe['fisher_rsi'] + 1)

        # # Stochastic Slow
        # stoch = ta.STOCH(dataframe)
        # dataframe['slowd'] = stoch['slowd']
        # dataframe['slowk'] = stoch['slowk']

        # Stochastic Fast
        #stoch_fast = ta.STOCHF(dataframe)
        #dataframe['fastd'] = stoch_fast['fastd']
        #dataframe['fastk'] = stoch_fast['fastk']

        # # Stochastic RSI
        # Please read https://github.com/freqtrade/freqtrade/issues/2961 before using this.
        # STOCHRSI is NOT aligned with tradingview, which may result in non-expected results.
        # stoch_rsi = ta.STOCHRSI(dataframe)
        # dataframe['fastd_rsi'] = stoch_rsi['fastd']
        # dataframe['fastk_rsi'] = stoch_rsi['fastk']

        # MACD
        macd = ta.MACD(dataframe)
        dataframe['macd'] = macd['macd']
        dataframe['macdsignal'] = macd['macdsignal']
        dataframe['macdhist'] = macd['macdhist']

        # MFI
        #dataframe['mfi'] = ta.MFI(dataframe)

        # # ROC
        # dataframe['roc'] = ta.ROC(dataframe)

        # Overlap Studies
        # ------------------------------------

        # Bollinger Bands
        bollinger = qtpylib.bollinger_bands(qtpylib.typical_price(dataframe), window=20, stds=2)
        dataframe['bb_lowerband'] = bollinger['lower']
        dataframe['bb_middleband'] = bollinger['mid']
        dataframe['bb_upperband'] = bollinger['upper']
        dataframe["bb_percent"] = (
            (dataframe["close"] - dataframe["bb_lowerband"]) /
            (dataframe["bb_upperband"] - dataframe["bb_lowerband"])
        )
        dataframe["bb_width"] = (
            (dataframe["bb_upperband"] - dataframe["bb_lowerband"]) / dataframe["bb_middleband"]
        )

        # Bollinger Bands - Weighted (EMA based instead of SMA)
        # weighted_bollinger = qtpylib.weighted_bollinger_bands(
        #     qtpylib.typical_price(dataframe), window=20, stds=2
        # )
        # dataframe["wbb_upperband"] = weighted_bollinger["upper"]
        # dataframe["wbb_lowerband"] = weighted_bollinger["lower"]
        # dataframe["wbb_middleband"] = weighted_bollinger["mid"]
        # dataframe["wbb_percent"] = (
        #     (dataframe["close"] - dataframe["wbb_lowerband"]) /
        #     (dataframe["wbb_upperband"] - dataframe["wbb_lowerband"])
        # )
        # dataframe["wbb_width"] = (
        #     (dataframe["wbb_upperband"] - dataframe["wbb_lowerband"]) / dataframe["wbb_middleband"]
        # )

        # # EMA - Exponential Moving Average
        # Calculate all ema_short values in generated range

        for val in self.buy_ema_short.range:
            dataframe[f'buy_ema_short_{val}'] = ta.EMA(dataframe, timeperiod=val)

        for val in self.sell_ema_short.range:
            dataframe[f'sell_ema_short_{val}'] = ta.EMA(dataframe, timeperiod=val)

        # # SMA - Simple Moving Average
        # Calculate all sma_* values in generated range

        for val in self.buy_3sma_short.range:
            dataframe[f'buy_sma_short_{val}'] = ta.SMA(dataframe, timeperiod=val)

        for val in self.buy_3sma_medium.range:
            dataframe[f'buy_sma_medium_{val}'] = ta.SMA(dataframe, timeperiod=val)

        for val in self.buy_3sma_long.range:
            dataframe[f'buy_sma_long_{val}'] = ta.SMA(dataframe, timeperiod=val)

        for val in self.sell_3sma_short.range:
            dataframe[f'sell_sma_short_{val}'] = ta.SMA(dataframe, timeperiod=val)

        for val in self.sell_3sma_medium.range:
            dataframe[f'sell_sma_medium_{val}'] = ta.SMA(dataframe, timeperiod=val)

        for val in self.sell_3sma_long.range:
            dataframe[f'sell_sma_long_{val}'] = ta.SMA(dataframe, timeperiod=val)


        dataframe['ema_short_5'] = ta.EMA(dataframe, timeperiod=5)
        dataframe['sma_5'] = ta.SMA(dataframe, timeperiod=5)
        dataframe['sma_20'] = ta.SMA(dataframe, timeperiod=20)

        # Parabolic SAR
        #dataframe['sar'] = ta.SAR(dataframe)

        # TEMA - Triple Exponential Moving Average
        #dataframe['tema'] = ta.TEMA(dataframe, timeperiod=9)

        # Cycle Indicator
        # ------------------------------------
        # Hilbert Transform Indicator - SineWave
        #hilbert = ta.HT_SINE(dataframe)
        #dataframe['htsine'] = hilbert['sine']
        #dataframe['htleadsine'] = hilbert['leadsine']

        # Pattern Recognition - Bullish candlestick patterns
        # ------------------------------------
        # # Hammer: values [0, 100]
        dataframe['CDLHAMMER'] = ta.CDLHAMMER(dataframe)
        # # Inverted Hammer: values [0, 100]
        #dataframe['CDLINVERTEDHAMMER'] #= ta.CDLINVERTEDHAMMER(dataframe)
        # # Dragonfly Doji: values [0, 100]
        # dataframe['CDLDRAGONFLYDOJI'] = ta.CDLDRAGONFLYDOJI(dataframe)
        # # Piercing Line: values [0, 100]
        # dataframe['CDLPIERCING'] = ta.CDLPIERCING(dataframe) # values [0, 100]
        # # Morningstar: values [0, 100]
        # dataframe['CDLMORNINGSTAR'] = ta.CDLMORNINGSTAR(dataframe) # values [0, 100]
        # # Three White Soldiers: values [0, 100]
        # dataframe['CDL3WHITESOLDIERS'] = ta.CDL3WHITESOLDIERS(dataframe) # values [0, 100]

        # Pattern Recognition - Bearish candlestick patterns
        # ------------------------------------
        # # Hanging Man: values [0, 100]
        # dataframe['CDLHANGINGMAN'] = ta.CDLHANGINGMAN(dataframe)
        # # Shooting Star: values [0, 100]
        # dataframe['CDLSHOOTINGSTAR'] = ta.CDLSHOOTINGSTAR(dataframe)
        # # Gravestone Doji: values [0, 100]
        # dataframe['CDLGRAVESTONEDOJI'] = ta.CDLGRAVESTONEDOJI(dataframe)
        # # Dark Cloud Cover: values [0, 100]
        # dataframe['CDLDARKCLOUDCOVER'] = ta.CDLDARKCLOUDCOVER(dataframe)
        # # Evening Doji Star: values [0, 100]
        # dataframe['CDLEVENINGDOJISTAR'] = ta.CDLEVENINGDOJISTAR(dataframe)
        # # Evening Star: values [0, 100]
        # dataframe['CDLEVENINGSTAR'] = ta.CDLEVENINGSTAR(dataframe)

        # Pattern Recognition - Bullish/Bearish candlestick patterns
        # ------------------------------------
        # # Three Line Strike: values [0, -100, 100]
        # dataframe['CDL3LINESTRIKE'] = ta.CDL3LINESTRIKE(dataframe)
        # # Spinning Top: values [0, -100, 100]
        # dataframe['CDLSPINNINGTOP'] = ta.CDLSPINNINGTOP(dataframe) # values [0, -100, 100]
        # # Engulfing: values [0, -100, 100]
        # dataframe['CDLENGULFING'] = ta.CDLENGULFING(dataframe) # values [0, -100, 100]
        # # Harami: values [0, -100, 100]
        # dataframe['CDLHARAMI'] = ta.CDLHARAMI(dataframe) # values [0, -100, 100]
        # # Three Outside Up/Down: values [0, -100, 100]
        # dataframe['CDL3OUTSIDE'] = ta.CDL3OUTSIDE(dataframe) # values [0, -100, 100]
        # # Three Inside Up/Down: values [0, -100, 100]
        # dataframe['CDL3INSIDE'] = ta.CDL3INSIDE(dataframe) # values [0, -100, 100]

        # # Chart type
        # # ------------------------------------
        # # Heikin Ashi Strategy
        # heikinashi = qtpylib.heikinashi(dataframe)
        # dataframe['ha_open'] = heikinashi['open']
        # dataframe['ha_close'] = heikinashi['close']
        # dataframe['ha_high'] = heikinashi['high']
        # dataframe['ha_low'] = heikinashi['low']

        # Retrieve best bid and best ask from the orderbook
        # ------------------------------------
        """
        # first check if dataprovider is available
        if self.dp:
            if self.dp.runmode.value in ('live', 'dry_run'):
                ob = self.dp.orderbook(metadata['pair'], 1)
                dataframe['best_bid'] = ob['bids'][0][0]
                dataframe['best_ask'] = ob['asks'][0][0]
        """

        return dataframe

    def populate_buy_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        """
        Based on TA indicators, populates the buy signal for the given dataframe
        :param dataframe: DataFrame populated with indicators
        :param metadata: Additional information, like the currently traded pair
        :return: DataFrame with buy column
        """
        conditions = []
        dataframe.loc[:, 'buy_tag'] = ''
        dataframe.loc[:, 'buy'] = 0

        # Guards and Trends
        """
            - if SMA_SHORT crosses above all SMAs
            -- extra check with proximity factor
            - if SMA_5 crosses above SMA_20
            - if Momentum is positive
            - if RSI is oversold compared to Its limits
            - if Consider Hammer in max value
        """
        if self.buy_3sma_enabled.value:
            SMAshort_SMAmedium_difference = (
                dataframe[f'buy_sma_short_{self.buy_3sma_short.value}'] - dataframe[f'buy_sma_medium_{self.buy_3sma_medium.value}']
            )
            SMAs_proximity = round(SMAshort_SMAmedium_difference,1)
            # 1.2 is a factor of proximity when the SMAs indicator are descendent
            PROXIMITY_FACTOR = 1.2

            check_3sma = (
                (SMAs_proximity > PROXIMITY_FACTOR)
                &
                (dataframe[f'buy_sma_short_{self.buy_3sma_short.value}'] > dataframe[f'buy_sma_medium_{self.buy_3sma_medium.value}'])
                &
                (dataframe[f'buy_sma_short_{self.buy_3sma_short.value}'] > dataframe[f'buy_sma_long_{self.buy_3sma_long.value}'])
                &
                (dataframe[f'buy_sma_medium_{self.buy_3sma_medium.value}'] > dataframe[f'buy_sma_long_{self.buy_3sma_long.value}'])
            )
            dataframe.loc[check_3sma,'buy_tag'] += '3sma '
            conditions.append(check_3sma)

        # 2 SMA Crossover
        if self.buy_2sma_enabled.value:
            buy_2ma = (
                qtpylib.crossed_above(
                    dataframe['sma_5'], dataframe['sma_20']
                )
                &
                (dataframe['volume'] >= 1000)
            )
            dataframe.loc[buy_2ma,'buy_tag'] += '2sma '
            conditions.append(buy_2ma)

            #check_volume = dataframe['volume'] >= 1000
            #dataframe.loc[check_volume,'buy_tag'] += 'volume_1000 '
            #conditions.append(check_volume)

        if self.buy_rsi_enabled.value:
            """
            rsi = (
                (dataframe['rsi'] > self.rsi_oversell_limit)
                &
                (dataframe['rsi'] < self.rsi_overbought_limit)
            )
            """
            rsi = (
                (dataframe['rsi'] > self.rsi_oversell_limit)
                &
                (dataframe['rsi'] < (self.rsi_overbought_limit - self.rsi_proximity_boundaries))
            )
            dataframe.loc[rsi,'buy_tag'] += 'rsi '
            conditions.append(rsi)

        if self.buy_cdl_hammer_enabled.value:
            cdl_hammer = (dataframe['CDLHAMMER'] == 100)
            dataframe.loc[cdl_hammer,'buy_tag'] += 'cdl_hammer '
            conditions.append(cdl_hammer)


        # Triggers
        """
            - if EMA_* is minor than candle close price AND momentum is greater than 0
            - if close price is minor than bolinger lowerband
            - if MACD crossed above Its signal line
        """
        if self.buy_trigger == 'elders_moment':
            # Trying Elder's Moment
            # combining A Momentum with a EMA. By default it's expected to be a MOM(14) with a EMA(19) for H1-D1 time frames.
            # A buy signal is Momentum above the average level, the most part of a body of the current candle is higher than a moving average
            # @see https://www.fcxchief.asia/library/indicators/momentum-indicator/

            elders_moment = (
                (dataframe['close'] > dataframe[f'buy_ema_short_{self.buy_ema_short.value}'])
                &
                (dataframe['mom'] > 0)
            )
            dataframe.loc[elders_moment,'buy_tag'] += 'elders_moment '
            conditions.append(elders_moment)

        if self.buy_trigger == 'bb_lower':
            bb_lowerband = (
                dataframe['close'] < dataframe['bb_lowerband']
            )
            dataframe.loc[bb_lowerband,'buy_tag'] += 'bb_lowerband '
            conditions.append(bb_lowerband)

        if self.buy_trigger.value == 'macd_cross_signal':
            macd = (
                qtpylib.crossed_above(
                    dataframe['macd'], dataframe['macdsignal']
                )
            )
            dataframe.loc[macd,'buy_tag'] += 'macd_positive '
            conditions.append(macd)

        # Check that volume is not 0
        volume_gt_zero = (dataframe['volume'] > 0)

        """
        dataframe.loc[
            (
                (qtpylib.crossed_above(dataframe['sma5'], dataframe['sma10'])) &
                (qtpylib.crossed_above(dataframe['sma5'], dataframe['sma20'])) &
                (dataframe['rsi'] > 25) &  # Signal: RSI crosses oversell line
                (dataframe['rsi'] < 75) &  # Signal: RSI not crosses overbought line
                #(dataframe['bb_lowerband'] > dataframe['close']) &
                (dataframe['mom'] > 0) &
                (dataframe['ema19'] < dataframe['close']) &
                (dataframe['volume'] > 0)  # Make sure Volume is not 0
            ),
            'buy'] = 1
        """

        if conditions:
            # change | to & can decrease profit
            """
            dataframe.loc[
                reduce(lambda x, y: x & y, conditions),
                'buy'
            ] = 1
            """
            dataframe.loc[:, 'buy'] = (volume_gt_zero & reduce(lambda x, y: x & y, conditions))

        return dataframe

    def populate_sell_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        """
        Based on TA indicators, populates the sell signal for the given dataframe
        :param dataframe: DataFrame populated with indicators
        :param metadata: Additional information, like the currently traded pair
        :return: DataFrame with buy column
        """

        conditions = []

        # Guards and Trends
        """
            - if SMA_SHORT crosses below all SMAs
            - if SMA_50 crosses below SMA_200
            - if Momentum is negative
            - if RSI is oversold compared to its limits
        """

        if self.sell_3sma_enabled.value:
            conditions.append(
                (dataframe[f'sell_sma_short_{self.sell_3sma_short.value}'] < dataframe[f'sell_sma_medium_{self.sell_3sma_medium.value}'])
                &
                (dataframe[f'sell_sma_short_{self.sell_3sma_short.value}'] < dataframe[f'sell_sma_long_{self.sell_3sma_long.value}'])
                &
                (dataframe[f'sell_sma_medium_{self.sell_3sma_medium.value}'] < dataframe[f'sell_sma_long_{self.sell_3sma_long.value}'])
            )

        # 2 SMA Crossover
        if self.sell_2sma_enabled.value:
            conditions.append(qtpylib.crossed_below(
                dataframe['sma_5'], dataframe['sma_20']
            ))

        if self.sell_rsi_enabled.value:
            conditions.append(
                (dataframe['rsi'] > (self.rsi_overbought_limit - self.rsi_proximity_boundaries))
            )

        # Triggers
        """
            - if EMA_* is greater than candle close price AND momentum is minor than 0
            - if close price is greater than bolinger lowerband
            - if MACD crossed below Its signal line
        """
        if self.sell_trigger == 'elders_moment':

            # Trying Elder's Moment
            # combining A Momentum with a EMA. By default it's expected to be a MOM(14) with a EMA(19) for H1-D1 time frames.
            # A sell signal is Momentum below the average level, the most part of a body of the current candle is higher than a moving average
            # @see https://www.fcxchief.asia/library/indicators/momentum-indicator/
            conditions.append(
                (dataframe['close'] < dataframe[f'sell_ema_short_{self.sell_ema_short.value}'])
                &
                (dataframe['mom'] < 0)
            )

        if self.sell_trigger == 'bb_lower':
            conditions.append(dataframe['close'] > dataframe['bb_lowerband'])

        if self.sell_trigger.value == 'macd_cross_signal':
            conditions.append(qtpylib.crossed_below(
                dataframe['macd'], dataframe['macdsignal']
            ))

        # Check that volume is not 0
        volume_gt_zero = (dataframe['volume'] > 0)


        if conditions:
            # change & to | can decrease profits
            dataframe.loc[:, 'sell'] = (volume_gt_zero & reduce(lambda x, y: x & y, conditions))


        return dataframe
