# BusyGuy Strategy v1.0.0 @ 2024-08-08

Strategy's logic explained:

With low timeframes, the strategy is designed to be active and agressive, providing a high number of trades.
The strategy uses the 200 SMA as a reference to determine the market's direction and the 50 SMA to confirm the trend.
The strategy also uses the RSI and Bollinger Bands to provide additional confirmation for the signals.

A buffer margin is used to ensure that trades can be executed even when the price is near the 200 SMA, enhancing the strategy's responsiveness and trade frequency.

Checkout buy and sell signal functions for more details on the strategy's logic. 

**This is a strategy for High Season and is still on improvement and it is not a guarantee of profits.**
**Use at your own risk.**

- **BusyGuy.py** - This is a version for FreqTrade framework.
- **BusyGuy.pine** - This is a version for TradingView ecossistem but is not finished yet.

# Commands

```
# bull market from feb-2023 to july-2024 (YYYYMMDD)

freqtrade download-data --timeframes 15m 1h 4h 1d --timerange 20230102-20240804 --config ./user_data/configs/config.json --config ./user_data/configs/BusyGuy.config.json && \
--config ./user_data/configs/config_pairs_a.json --config ./user_data/configs/config_pairs_b.json --config ./user_data/configs/config_pairs_c.json

# Backtesting and Optimization
# Change the timerange to correspond to the backtesting interval, so you will get similar results

freqtrade backtesting --strategy BusyGuy --timeframe 1h --timerange 20230102-2024084 --config ./user_data/configs/config.json --config ./user_data/configs/BusyGuy.config.json

freqtrade lookahead-analysis --strategy BusyGuy --timeframe 1h --cache none --dry-run-wallet 10000000 --stake-amount 1000 --enable-protections --timerange 20230102-20240804 --config ./user_data/configs/config.json --config ./user_data/configs/BusyGuy.config.json

freqtrade lookahead-analysis --strategy BusyGuy --timeframe 1h --cache none --dry-run-wallet 10000000 --stake-amount 1000 --enable-protections --timerange 20240101-20240804 --config ./user_data/configs/config.json --config ./user_data/configs/BusyGuy.config.json

# Attention to the limit of job workers your machine can handle.

freqtrade hyperopt --job-workers 2 --hyperopt-loss SharpeHyperOptLossDaily --spaces buy sell --strategy BusyGuy -e 200 --timeframe 1h --timerange 20230102-20240804 --config ./user_data/configs/config.json --config ./user_data/configs/BusyGuy.config.json

```


# Backtesting results - 20230102-20240804

`freqtrade backtesting --strategy BusyGuy --timeframe 1h --timerange 20230102-20240804 --config ./user_data/configs/config.json --config ./user_data/configs/BusyGuy.config.json`

```

===================================================== BACKTESTING REPORT =====================================================
|        Pair |   Trades |   Avg Profit % |   Tot Profit USDT |   Tot Profit % |      Avg Duration |   Win  Draw  Loss  Win% |
|-------------+----------+----------------+-------------------+----------------+-------------------+-------------------------|
|    RAY/USDT |       23 |           4.85 |            71.834 |          71.83 |  5 days, 19:55:00 |    23     0     0   100 |
|   DOGE/USDT |       10 |           4.84 |            38.980 |          38.98 |   2 days, 4:18:00 |    10     0     0   100 |
|    SOL/USDT |       12 |           4.26 |            35.205 |          35.20 |  10 days, 6:00:00 |    12     0     0   100 |
| PEOPLE/USDT |        9 |           4.34 |            32.825 |          32.83 | 41 days, 22:53:00 |     9     0     0   100 |
|   BAKE/USDT |       10 |           5.26 |            28.242 |          28.24 |   6 days, 4:48:00 |    10     0     0   100 |
|    BTC/USDT |        9 |           4.17 |            23.912 |          23.91 |  23 days, 1:47:00 |     9     0     0   100 |
|    BNB/USDT |        8 |           5.00 |            23.506 |          23.51 |  3 days, 12:00:00 |     8     0     0   100 |
|   CTSI/USDT |       11 |           4.30 |            20.606 |          20.61 |   5 days, 0:38:00 |    11     0     0   100 |
|    LTC/USDT |        8 |           3.86 |            18.442 |          18.44 |   5 days, 3:22:00 |     8     0     0   100 |
|   IOTA/USDT |        9 |           4.51 |            13.302 |          13.30 |   4 days, 9:20:00 |     8     0     1  88.9 |
|    XRP/USDT |        6 |           4.36 |            11.796 |          11.80 |  20 days, 7:40:00 |     6     0     0   100 |
|    ETH/USDT |        6 |           3.57 |             7.790 |           7.79 | 25 days, 22:40:00 |     6     0     0   100 |
|    BCH/USDT |       14 |           0.65 |           -19.192 |         -19.19 | 15 days, 16:04:00 |    13     0     1  92.9 |
|   LINK/USDT |        7 |          -1.63 |           -31.472 |         -31.47 | 25 days, 15:34:00 |     6     0     1  85.7 |
|    ADA/USDT |        9 |          -1.10 |           -33.676 |         -33.68 | 48 days, 23:47:00 |     8     0     1  88.9 |
|       TOTAL |      151 |           3.54 |           242.099 |         242.10 | 14 days, 14:51:00 |   147     0     4  97.4 |
================================================== LEFT OPEN TRADES REPORT ==================================================
|      Pair |   Trades |   Avg Profit % |   Tot Profit USDT |   Tot Profit % |       Avg Duration |   Win  Draw  Loss  Win% |
|-----------+----------+----------------+-------------------+----------------+--------------------+-------------------------|
| IOTA/USDT |        1 |         -20.00 |           -26.701 |         -26.70 |   7 days, 12:00:00 |     0     0     1     0 |
| LINK/USDT |        1 |         -40.63 |           -48.667 |         -48.67 |  130 days, 4:00:00 |     0     0     1     0 |
|  ADA/USDT |        1 |         -49.84 |           -57.577 |         -57.58 | 141 days, 17:00:00 |     0     0     1     0 |
|  BCH/USDT |        1 |         -46.62 |           -58.502 |         -58.50 |  117 days, 8:00:00 |     0     0     1     0 |
|     TOTAL |        4 |         -39.27 |          -191.447 |        -191.45 |   99 days, 4:15:00 |     0     0     4     0 |
=================================================================== ENTER TAG STATS ====================================================================
|                            Enter Tag |   Entries |   Avg Profit % |   Tot Profit USDT |   Tot Profit % |      Avg Duration |   Win  Draw  Loss  Win% |
|--------------------------------------+-----------+----------------+-------------------+----------------+-------------------+-------------------------|
| stochastic_oversold_adx_strong_trend |       115 |           3.82 |           215.710 |         215.71 | 10 days, 14:10:00 |   113     0     2  98.3 |
|      rsi_oversold_price_above_sma200 |         9 |           4.87 |            28.851 |          28.85 |  9 days, 16:07:00 |     9     0     0   100 |
|   price_far_from_sma200_great_volume |        27 |           1.91 |            -2.461 |          -2.46 | 33 days, 10:16:00 |    25     0     2  92.6 |
|                                TOTAL |       151 |           3.54 |           242.099 |         242.10 | 14 days, 14:51:00 |   147     0     4  97.4 |
============================================================== EXIT REASON STATS ===============================================================
|                    Exit Reason |   Exits |   Avg Profit % |   Tot Profit USDT |   Tot Profit % |      Avg Duration |   Win  Draw  Loss  Win% |
|--------------------------------+---------+----------------+-------------------+----------------+-------------------+-------------------------|
|                            roi |     111 |           5.04 |           341.735 |         341.73 |  15 days, 2:08:00 |   111     0     0   100 |
|             trailing_stop_loss |      21 |           5.27 |            76.370 |          76.37 |           4:46:00 |    21     0     0   100 |
|                    exit_signal |      13 |           1.37 |            13.588 |          13.59 |  9 days, 22:09:00 |    13     0     0   100 |
| death_cross_price_below_sma200 |       2 |           1.86 |             1.854 |           1.85 |    1 day, 9:00:00 |     2     0     0   100 |
|                     force_exit |       4 |         -39.27 |          -191.447 |        -191.45 |  99 days, 4:15:00 |     0     0     4     0 |
|                          TOTAL |     151 |           3.54 |           242.099 |         242.10 | 14 days, 14:51:00 |   147     0     4  97.4 |
============================================================================================= MIXED TAG STATS ==============================================================================================
|                                                                Enter Tag |   Exit Reason |   Trades |   Avg Profit % |   Tot Profit USDT |   Tot Profit % |       Avg Duration |   Win  Draw  Loss  Win% |
|--------------------------------------------------------------------------+---------------+----------+----------------+-------------------+----------------+--------------------+-------------------------|
|                          ('stochastic_oversold_adx_strong_trend', 'roi') |               |       88 |           5.05 |           267.297 |         267.30 |   10 days, 4:57:00 |    88     0     0   100 |
|                            ('price_far_from_sma200_great_volume', 'roi') |               |       17 |           5.00 |            56.845 |          56.85 |  40 days, 19:21:00 |    17     0     0   100 |
|           ('stochastic_oversold_adx_strong_trend', 'trailing_stop_loss') |               |       18 |           4.09 |            49.172 |          49.17 |            4:57:00 |    18     0     0   100 |
|             ('price_far_from_sma200_great_volume', 'trailing_stop_loss') |               |        2 |          14.32 |            18.258 |          18.26 |            5:00:00 |     2     0     0   100 |
|                               ('rsi_oversold_price_above_sma200', 'roi') |               |        6 |           5.00 |            17.593 |          17.59 |  13 days, 19:50:00 |     6     0     0   100 |
|                ('rsi_oversold_price_above_sma200', 'trailing_stop_loss') |               |        1 |           8.30 |             8.941 |           8.94 |            1:00:00 |     1     0     0   100 |
|                    ('price_far_from_sma200_great_volume', 'exit_signal') |               |        5 |           1.55 |             6.416 |           6.42 |  11 days, 15:36:00 |     5     0     0   100 |
|                  ('stochastic_oversold_adx_strong_trend', 'exit_signal') |               |        7 |           1.13 |             6.411 |           6.41 |   9 days, 18:51:00 |     7     0     0   100 |
|    ('rsi_oversold_price_above_sma200', 'death_cross_price_below_sma200') |               |        1 |           3.45 |             1.556 |           1.56 |    1 day, 19:00:00 |     1     0     0   100 |
|                       ('rsi_oversold_price_above_sma200', 'exit_signal') |               |        1 |           2.09 |             0.761 |           0.76 |    2 days, 6:00:00 |     1     0     0   100 |
| ('price_far_from_sma200_great_volume', 'death_cross_price_below_sma200') |               |        1 |           0.26 |             0.298 |           0.30 |           23:00:00 |     1     0     0   100 |
|                     ('price_far_from_sma200_great_volume', 'force_exit') |               |        2 |         -34.92 |           -84.277 |         -84.28 |  74 days, 14:30:00 |     0     0     2     0 |
|                   ('stochastic_oversold_adx_strong_trend', 'force_exit') |               |        2 |         -43.62 |          -107.169 |        -107.17 | 123 days, 18:00:00 |     0     0     2     0 |
|                                                                    TOTAL |               |      151 |           3.54 |           242.099 |         242.10 |  14 days, 14:51:00 |   147     0     4  97.4 |
================== SUMMARY METRICS ==================
| Metric                      | Value               |
|-----------------------------+---------------------|
| Backtesting from            | 2023-01-02 00:00:00 |
| Backtesting to              | 2024-08-04 00:00:00 |
| Max open trades             | 4                   |
|                             |                     |
| Total/Daily Avg Trades      | 151 / 0.26          |
| Starting balance            | 100 USDT            |
| Final balance               | 342.099 USDT        |
| Absolute profit             | 242.099 USDT        |
| Total profit %              | 242.10%             |
| CAGR %                      | 116.84%             |
| Sortino                     | 0.62                |
| Sharpe                      | 0.92                |
| Calmar                      | 22.22               |
| Profit factor               | 2.26                |
| Expectancy (Ratio)          | 1.60 (0.03)         |
| Avg. daily profit %         | 0.42%               |
| Avg. stake amount           | 65.066 USDT         |
| Total trade volume          | 9824.99 USDT        |
|                             |                     |
| Best Pair                   | RAY/USDT 71.83%     |
| Worst Pair                  | LINK/USDT -31.47%   |
| Best trade                  | IOTA/USDT 26.12%    |
| Worst trade                 | ADA/USDT -49.84%    |
| Best day                    | 21.846 USDT         |
| Worst day                   | -191.447 USDT       |
| Days win/draw/lose          | 110 / 466 / 1       |
| Avg. Duration Winners       | 12 days, 7:38:00    |
| Avg. Duration Loser         | 99 days, 4:15:00    |
| Max Consecutive Wins / Loss | 147 / 4             |
| Rejected Entry signals      | 2673                |
| Entry/Exit Timeouts         | 0 / 0               |
|                             |                     |
| Min balance                 | 101.25 USDT         |
| Max balance                 | 533.546 USDT        |
| Max % of account underwater | 35.88%              |
| Absolute Drawdown (Account) | 35.88%              |
| Absolute Drawdown           | 191.447 USDT        |
| Drawdown high               | 433.546 USDT        |
| Drawdown low                | 242.099 USDT        |
| Drawdown Start              | 2024-07-27 08:00:00 |
| Drawdown End                | 2024-08-04 00:00:00 |
| Market change               | 240.39%             |
=====================================================

Backtested 2023-01-02 00:00:00 -> 2024-08-04 00:00:00 | Max open trades : 4
================================================================= STRATEGY SUMMARY =================================================================
|   Strategy |   Trades |   Avg Profit % |   Tot Profit USDT |   Tot Profit % |      Avg Duration |   Win  Draw  Loss  Win% |             Drawdown |
|------------+----------+----------------+-------------------+----------------+-------------------+-------------------------+----------------------|
|    BusyGuy |      151 |           3.54 |           242.099 |         242.10 | 14 days, 14:51:00 |   147     0     4  97.4 | 191.447 USDT  35.88% |
====================================================================================================================================================


```