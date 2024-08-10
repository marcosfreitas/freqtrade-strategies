# --- Do not remove these libs ---
from freqtrade.strategy.interface import IStrategy
import freqtrade.vendor.qtpylib.indicators as qtpylib
from freqtrade.persistence import Trade
from freqtrade.strategy import stoploss_from_open

from pandas import DataFrame
import talib.abstract as ta

from freqtrade.strategy import (BooleanParameter, CategoricalParameter, DecimalParameter, IStrategy, IntParameter)

import talib.abstract as ta
import freqtrade.vendor.qtpylib.indicators as qtpylib

from datetime import datetime
from calendar import monthrange

from freqtrade.exchange import timeframe_to_minutes

from datetime import timedelta

# --------------------------------

class BusyGuy(IStrategy):
    """
    Busy Guy - An active and bold trading strategy that uses the 200 SMA as a reference.
    Indicators: 200 SMA, 50 SMA, RSI, Bollinger Bands
    author@: Marcos Freitas
    github@: https://github.com/marcosfreitas/freqtrade-strategies
    version@: 1.1.0-2024-08-09

    Strategy's logic explained:

    With low timeframes, the strategy is designed to be active and agressive, providing a high number of trades.
    
    A buffer margin is used to ensure that trades can be executed even when the price is near the 200 SMA, enhancing the strategy's responsiveness and trade frequency.

    Checkout buy and sell signal functions for more details on the strategy's logic.
    
    Extra notes:

    - The strategy uses the 200 SMA as a reference to determine the market's direction.
    - The strategy uses the 50 SMA to confirm the trend.
    - The strategy also uses the RSI and Bollinger Bands to provide additional confirmation for the signals.
    - Designed to timeframe of 1h
    - Added Hypeopt attributes, optimized by SharpeHyperOptLossDaily loss function are loaded from BusyGuy.json
    - Added protections for cooldown, max drawdown and stoploss

    """

    # Strategy interface version - allow new iterations of the strategy interface.
    # Check the documentation or the Sample strategy to get the latest version.
    INTERFACE_VERSION = 2

    # Minimal ROI designed for the strategy.


    # Optimal timeframe for the strategy.
    timeframe = '1h'
    # Number of candles the strategy requires before producing valid signals
    # considering the 1h timeframe, 200hs = 8 days
    startup_candle_count: int = 200
    timeframe_mins = timeframe_to_minutes(timeframe)

    # Minimal ROI designed for the strategy.
    minimal_roi = {
        "0": DecimalParameter(0.02, 1.0, default=0.5, space='roi'), # exit immediately if achieved x% profit
        str(timeframe_mins * 3): DecimalParameter(0.02, 1.0, default=0.5, space='roi'),  # after 3 candles
        str(timeframe_mins * 6): DecimalParameter(0.02, 1.0, default=0.2, space='roi'), 
        str(timeframe_mins * 9): DecimalParameter(0.02, 1.0, default=0.3, space='roi'),  
        str(timeframe_mins * 12): DecimalParameter(0.02, 1.0, default=0.1, space='roi')
    }

    # Stoploss:
    stoploss = -0.7  # Stoploss at 70%

    # Trailing stoploss
    trailing_stop = True
    trailing_stop_positive = 0.03  # Trailing stop activates at 3% profit
    # 5% from peak, trailing stop starts at 2% profit
    # should be lower than minimal_roi
    trailing_stop_positive_offset = 0.05 # stop will actually be 10% below the peak price once the price has moved 2% in your favor.
    trailing_only_offset_is_reached = True

    # Run "populate_indicators()" only for new candle instead of running for past candles on every loop
    # @tip: during development, set to false to plot points for past candles also.
    process_only_new_candles = True

    # These values can be overridden in the "ask_strategy" section in the config.
    use_sell_signal = True
    sell_profit_only = True
    ignore_roi_if_buy_signal = False

    # Define hyperopt parameters
    
    buy_buffer = DecimalParameter(0.50, 1.0, default=0.98, space='buy')
    sell_buffer = DecimalParameter(0.50, 1.0, default=0.98, space='sell')

    #sma50_crossed_sma200_above = IntParameter(1, 30, default=48, space='buy')  # Window of validity in hours
    close_crossed_above_sma200_validity_period = IntParameter(1, 72, default=72, space='buy')  # Window of validity in hours
    close_crossed_below_sma200_validity_period = IntParameter(1, 72, default=72, space='sell')  # Window of validity in hours
    #bands_crossover_validity_period = IntParameter(1, 30, default=24, space='buy')  # Window of validity in hours

    #buy_rsi = IntParameter(10, 40, default=30, space='buy')
    #sell_rsi = IntParameter(60, 90, default=70, space='sell')

    # The percentage of profit at which the trailing profit starts to activate.
    # Start trailing when 3% profit is reached
    trailing_profit_start_percent = 0.03

    # The distance (in percentage) from the maximum price that the trailing profit level should be set.
    # Trail by 1% below the highest price reached
    trailing_profit_percent = 0.01 

    # Optional order type mapping.
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
        'main_plot': {
            'upper_bband': {'color': 'green'},
            'middle_bband': {'color': 'orange'},
            'lower_bband': {'color': 'red'},
            'sma200': {'color': '#00e1ff'},
            'sma50': {'color': '#fff700'}
        },
        'subplots': {
            'RSI': {
                'rsi': {'color': 'red'}
            },
            'MACD': {
                'macd': {'color': 'orange'},
                'macdsignal': {'color': 'red'},
                'macdhist': {'color': 'blue'},
            },
            'Stochastic': {
                'slowk': {'color': 'blue'},
                'slowd': {'color': 'orange'},
            },
            'ADX': {
                'adx': {'color': 'green'}
            }
        }
    }

    use_max_drawdown_protection = BooleanParameter(default=True, space='protection', optimize=True)
    use_stoploss_protection = BooleanParameter(default=True, space='protection', optimize=True)

    cooldown_lookback = IntParameter(2, 48, default=24, space="protection", optimize=False)

    maxdrawdown_loopback = IntParameter(12, 48, default=48, space='protection', optimize=True)
    maxdrawdown_trade_limit = IntParameter(1, 20, default=20, space='protection', optimize=True)
    maxdrawdown_stop_duration = IntParameter(12, 200, default=12, space='protection', optimize=True)
    maxdrawdown_max_allowed_drawdown = DecimalParameter(0.01, 0.2, default=0.2, space='protection', optimize=True)

    stoploss_lookback = IntParameter(2, 60, default=10, space="protection", optimize=True)
    stoploss_trade_limit = IntParameter(1, 2, default=1, space="protection", optimize=True)
    stoploss_stop_duration = IntParameter(12, 200, default=20, space="protection", optimize=True)
    stoploss_only_per_pair = BooleanParameter(default=True, space="protection", optimize=True)


    @property
    def protections(self):
        prot = []

        prot.append({
            "method": "CooldownPeriod",
            "stop_duration_candles": self.cooldown_lookback.value
        })

        if self.use_max_drawdown_protection.value:
            prot.append(({
                "method": "MaxDrawdown",
                "lookback_period_candles": self.maxdrawdown_loopback.value,
                "trade_limit": self.maxdrawdown_trade_limit.value,
                "stop_duration_candles": self.maxdrawdown_stop_duration.value,
                "max_allowed_drawdown": self.maxdrawdown_max_allowed_drawdown.value,
            }))


        if self.use_stoploss_protection.value:
            prot.append({
                "method": "StoplossGuard",
                "lookback_period_candles": self.stoploss_lookback.value,
                "trade_limit": self.stoploss_trade_limit.value,
                "stop_duration_candles": self.stoploss_stop_duration.value,
                "only_per_pair": self.stoploss_only_per_pair.value,
            })

        return prot


    """
    Add TA indicators to the given dataframe
    """
    def populate_indicators(self, dataframe: DataFrame, metadata: dict) -> DataFrame:

        def isFriday(date):
            return date.weekday() == 4
        
        def isFridayNight(date):
            return date.weekday() == 4 & date.hour == 23 & date.minute == 59
        
        def isEndOfMonth(date):
            return date.day == monthrange(date.year, date.month)[1]
        
        dataframe['isFriday'] = dataframe['date'].apply(isFriday)
        dataframe['isFridayNight'] = dataframe['date'].apply(isFridayNight)
        dataframe['isEndOfMonth'] = dataframe['date'].apply(isEndOfMonth)

        # Momentum
        #dataframe['mom'] = ta.MOM(dataframe,14)

        # Calculate the N-period SMA
        dataframe['sma200'] = ta.SMA(dataframe['close'], timeperiod=200)
        dataframe['sma50'] = ta.SMA(dataframe['close'], timeperiod=50)

        # RSI
        dataframe['rsi'] = ta.RSI(dataframe, timeperiod=14)

        # MACD
        dataframe['macd'], dataframe['macdsignal'], dataframe['macdhist'] = ta.MACD(dataframe, fastperiod=12, slowperiod=26, signalperiod=9)
        
        # Bollinger Bands
        bollinger = ta.BBANDS(dataframe, timeperiod=20)
        
        dataframe['upper_bband'] = bollinger['upperband']
        dataframe['middle_bband'] = bollinger['middleband']
        dataframe['lower_bband'] = bollinger['lowerband']

        # Stochastic Oscillator
        stoch = ta.STOCH(dataframe)
        dataframe['slowk'] = stoch['slowk']
        dataframe['slowd'] = stoch['slowd']

        # ADX
        dataframe['adx'] = ta.ADX(dataframe)

        # sma / price crossover events
        dataframe['golden_cross'] = qtpylib.crossed_above(dataframe['sma50'], dataframe['sma200'])
        dataframe['death_cross'] = qtpylib.crossed_below(dataframe['sma50'], dataframe['sma200'])
        
        dataframe['close_crossed_above_sma200'] = qtpylib.crossed_above(dataframe['close'], dataframe['sma200'])
        dataframe['close_crossed_below_sma200'] = qtpylib.crossed_below(dataframe['close'], dataframe['sma200'])

        dataframe['upper_bband_crossed'] = qtpylib.crossed_above(dataframe['close'], dataframe['upper_bband'])
        dataframe['lower_bband_crossed'] = qtpylib.crossed_below(dataframe['close'], dataframe['lower_bband'])

        # track the maximum favorable price movement since entry
        dataframe['highest_price_since_entry'] = dataframe['close'].cummax()

        # @ todo for shorts, not implemented yet
        # dataframe['lowest_price_since_entry'] = dataframe['close'].cummin()

        # Identify downtrend by checking if previous 'n' candles had lower close prices
        n = 3  # Number of previous candles to check for a downtrend
        dataframe['downtrend'] = (
            (dataframe['close'].shift(n) > dataframe['close'].shift(n-1)) &
            (dataframe['close'].shift(n-1) > dataframe['close'].shift(n-2))
        )

        # Define the number of candles to check for a reversal
        n = 3  # Number of candles to check for reversal

        # Check if the close price has started to increase after the downtrend
        dataframe['downtrend_reversal'] = (
            (dataframe['close'] > dataframe['close'].shift(1)) &
            (dataframe['close'].shift(1) > dataframe['close'].shift(2)) &
            (dataframe['close'].shift(2) <= dataframe['close'].shift(3))  # Ensure the previous trend was a downtrend
        )
        
        # Calculate the rolling mean of volume and fill NaNs with 0
        great_volume_threshold = 2.5  # This represents 2.5x the average volume

        dataframe['average_volume'] = dataframe['volume'].rolling(window=20, min_periods=1).mean().fillna(0)

        # Check if the last volume is greater than 2.5 times the average volume for the  last 1 candle
        dataframe['has_great_volume'] = dataframe['volume'].shift(1) > (dataframe['average_volume'].shift(1) * great_volume_threshold)

        dataframe['price_trending_up_above_sma200_end_of_month'] = (
            (dataframe['close_crossed_above_sma200']) & (dataframe['close'] > dataframe['close'].shift(1)) & dataframe['has_great_volume']
        )
        
        # % distance from sma200    
        # ex: 10 (%) distant from sma200
        # use the values of the last candle
        dataframe['current_price_distance_from_sma200'] = (dataframe['sma200'].shift(1) - dataframe['close'].shift(1)) / dataframe['sma200'].shift(1) * 100

        return dataframe

    def populate_entry_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:

        dataframe['enter_tag'] = None

        # Define an entry condition based on golden cross
        dataframe.loc[
            (
                (dataframe['golden_cross']) &  # Confirm a golden cross occurred
                (dataframe['close'] > dataframe['sma200']) &  # Ensure price is above SMA200
                (dataframe['close'] < dataframe['upper_bband']) &  # Price below upper Bollinger Band
                (dataframe['volume'] > dataframe['average_volume'] * 2.5)  # Ensure volume is significantly high
            ),
            ['enter_long', 'enter_tag']
        ] = (1, 'golden_cross_price_above_sma200_high_volume')


        # Entry condition for price far from SMA200 and ending of a downtrend
        dataframe.loc[
            (
                (dataframe['current_price_distance_from_sma200'] >= 2) &
                (dataframe['close'] > dataframe['close'].shift(3)) &  # Ensure price is trending up
                (dataframe['close'] < dataframe['sma200']) &  # Ensure price is below SMA200
                (dataframe['downtrend'])  # Confirm previous downtrend
            ),
            ['enter_long', 'enter_tag']
        ] = (1, 'price_far_from_sma200_great_volume')
        
        
        if dataframe['price_trending_up_above_sma200_end_of_month'].all():
            dataframe.loc[:, ['enter_long', 'enter_tag']] = (1, 'price_trending_up_price_above_sma200_great_volume')

        dataframe.loc[
            (
                (dataframe['golden_cross'])
                & (dataframe['close'] > dataframe['close'].shift(1)) # Ensure price is trending up
                & (dataframe['close'] < dataframe['upper_bband']) # price below upper band
                & dataframe['has_great_volume']
            ),
            ['enter_long', 'enter_tag']
        ] = (1, 'golden_cross_price_trending_up_price_below_upper_band_great_volume')

        # Stochastic and ADX
        dataframe.loc[
            (
                (dataframe['slowk'] < 20) &  # Stochastic K below 20 (oversold)
                (dataframe['slowd'] < 20) &  # Stochastic D below 20 (oversold)
                (dataframe['adx'] > 25) &  # Strong trend
                (dataframe['close'] > dataframe['sma200'])  # Price above SMA200
            ),
            ['enter_long', 'enter_tag']
        ] = (1, 'stochastic_oversold_adx_strong_trend')


        # RSI and price above SMA200
        dataframe.loc[
            (
                (dataframe['rsi'] < 30) &  # RSI below 30 (oversold)
                (dataframe['close'] > dataframe['sma200'])  # Price above SMA200
            ),
            ['enter_long', 'enter_tag']
        ] = (1, 'rsi_oversold_price_above_sma200')

        return dataframe

    def populate_exit_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        dataframe['exit_tag'] = None

        # Start trailing profit only after a certain profit level is reached
        #trailing_profit_start_price = dataframe['close'] * (1 + self.trailing_profit_start_percent)

        # Calculate the trailing stop level
        #trailing_profit_level = dataframe['highest_price_since_entry'] * (1 - self.trailing_profit_percent)

        #dataframe.loc[
        #    (
        #        (dataframe['close'] < trailing_profit_level) &  # Exit if price falls below the trailing profit level
        #        (dataframe['close'] > trailing_profit_start_price)  # Ensure we're in profit before trailing),
        #    ),
        #    ['exit_long', 'exit_tag']
        #] = (1, 'trailing_stop_price_hit')

        # exit condition based on death cross
        dataframe.loc[
            (
                (dataframe['death_cross']) &  # Confirm a death cross occurred
                (dataframe['sma50'] < dataframe['sma200']) # Ensure the death cross happened on the last candle
            ),
            ['exit_long', 'exit_tag']
        ] = (1, 'death_cross_price_below_sma200')

        dataframe.loc[
            (
                (dataframe['golden_cross'])
                & (dataframe['close'] > (dataframe['sma200']))
            ),
            ['exit_long', 'enter_tag']
        ] = (1, 'death_cross_price_trending_down')

        return dataframe
