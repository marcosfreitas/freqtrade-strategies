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


# Backtesting results - 20230102-20240804

`freqtrade backtesting --strategy BusyGuy --timeframe 1h --timerange 20230102-20240804 --config ./user_data/configs/config.json --config ./user_data/configs/BusyGuy.config.json`

```
===================================================== BACKTESTING REPORT =====================================================
|        Pair |   Trades |   Avg Profit % |   Tot Profit USDT |   Tot Profit % |      Avg Duration |   Win  Draw  Loss  Win% |
|-------------+----------+----------------+-------------------+----------------+-------------------+-------------------------|
|    RAY/USDT |       25 |           4.75 |            87.787 |          87.79 |   5 days, 9:24:00 |    25     0     0   100 |
|   DOGE/USDT |       13 |           4.87 |            50.371 |          50.37 |  6 days, 10:14:00 |    13     0     0   100 |
| PEOPLE/USDT |       13 |           3.83 |            45.310 |          45.31 |  22 days, 5:14:00 |    13     0     0   100 |
|   CTSI/USDT |       14 |           4.45 |            32.826 |          32.83 |   3 days, 8:21:00 |    14     0     0   100 |
|    BTC/USDT |       13 |           3.33 |            29.810 |          29.81 |  20 days, 9:46:00 |    13     0     0   100 |
|   BAKE/USDT |       10 |           5.41 |            28.760 |          28.76 |   6 days, 1:42:00 |    10     0     0   100 |
|    SOL/USDT |        9 |           3.79 |            27.327 |          27.33 | 10 days, 20:20:00 |     9     0     0   100 |
|    BNB/USDT |        9 |           5.00 |            26.454 |          26.45 |   4 days, 9:27:00 |     9     0     0   100 |
|    LTC/USDT |       10 |           3.58 |            21.369 |          21.37 |   4 days, 7:18:00 |    10     0     0   100 |
|    ETH/USDT |        9 |           3.43 |            16.023 |          16.02 |  7 days, 14:27:00 |     9     0     0   100 |
|    XRP/USDT |        8 |           4.12 |            15.736 |          15.74 |  2 days, 23:52:00 |     8     0     0   100 |
|   IOTA/USDT |        9 |           2.16 |             0.294 |           0.29 |   5 days, 8:47:00 |     8     0     1  88.9 |
|    BCH/USDT |       14 |           0.53 |           -28.125 |         -28.13 | 18 days, 20:47:00 |    13     0     1  92.9 |
|    ADA/USDT |        9 |          -1.10 |           -36.891 |         -36.89 | 49 days, 13:27:00 |     8     0     1  88.9 |
|   LINK/USDT |        8 |          -1.58 |           -37.806 |         -37.81 | 35 days, 21:08:00 |     7     0     1  87.5 |
|       TOTAL |      173 |           3.32 |           279.244 |         279.24 | 12 days, 16:57:00 |   169     0     4  97.7 |
================================================== LEFT OPEN TRADES REPORT ==================================================
|      Pair |   Trades |   Avg Profit % |   Tot Profit USDT |   Tot Profit % |       Avg Duration |   Win  Draw  Loss  Win% |
|-----------+----------+----------------+-------------------+----------------+--------------------+-------------------------|
| IOTA/USDT |        1 |         -20.00 |           -29.481 |         -29.48 |   7 days, 12:00:00 |     0     0     1     0 |
| LINK/USDT |        1 |         -40.63 |           -53.062 |         -53.06 |  130 days, 4:00:00 |     0     0     1     0 |
|  ADA/USDT |        1 |         -49.84 |           -62.824 |         -62.82 | 141 days, 17:00:00 |     0     0     1     0 |
|  BCH/USDT |        1 |         -46.62 |           -64.543 |         -64.54 |  117 days, 8:00:00 |     0     0     1     0 |
|     TOTAL |        4 |         -39.27 |          -209.911 |        -209.91 |   99 days, 4:15:00 |     0     0     4     0 |
=================================================================== ENTER TAG STATS ====================================================================
|                            Enter Tag |   Entries |   Avg Profit % |   Tot Profit USDT |   Tot Profit % |      Avg Duration |   Win  Draw  Loss  Win% |
|--------------------------------------+-----------+----------------+-------------------+----------------+-------------------+-------------------------|
| stochastic_oversold_adx_strong_trend |       117 |           3.78 |           230.839 |         230.84 |   9 days, 0:52:00 |   115     0     2  98.3 |
|      rsi_oversold_price_above_sma200 |        11 |           4.89 |            35.261 |          35.26 | 18 days, 10:05:00 |    11     0     0   100 |
|   price_far_from_sma200_great_volume |        45 |           1.74 |            13.144 |          13.14 | 20 days, 20:25:00 |    43     0     2  95.6 |
|                                TOTAL |       173 |           3.32 |           279.244 |         279.24 | 12 days, 16:57:00 |   169     0     4  97.7 |
============================================================== EXIT REASON STATS ===============================================================
|                    Exit Reason |   Exits |   Avg Profit % |   Tot Profit USDT |   Tot Profit % |      Avg Duration |   Win  Draw  Loss  Win% |
|--------------------------------+---------+----------------+-------------------+----------------+-------------------+-------------------------|
|                            roi |     117 |           5.04 |           387.017 |         387.02 | 13 days, 15:29:00 |   117     0     0   100 |
|             trailing_stop_loss |      25 |           3.99 |            75.913 |          75.91 |           4:43:00 |    25     0     0   100 |
|                    exit_signal |      25 |           1.54 |            24.316 |          24.32 |  7 days, 21:22:00 |    25     0     0   100 |
| death_cross_price_below_sma200 |       2 |           1.86 |             1.908 |           1.91 |    1 day, 9:00:00 |     2     0     0   100 |
|                     force_exit |       4 |         -39.27 |          -209.911 |        -209.91 |  99 days, 4:15:00 |     0     0     4     0 |
|                          TOTAL |     173 |           3.32 |           279.244 |         279.24 | 12 days, 16:57:00 |   169     0     4  97.7 |
==================================================================================== MIXED TAG STATS ====================================================================================
|                            Enter Tag |                    Exit Reason |   Trades |   Avg Profit % |   Tot Profit USDT |   Tot Profit % |       Avg Duration |   Win  Draw  Loss  Win% |
|--------------------------------------+--------------------------------+----------+----------------+-------------------+----------------+--------------------+-------------------------|
| stochastic_oversold_adx_strong_trend |                            roi |       87 |           5.05 |           281.952 |         281.95 |   8 days, 11:21:00 |    87     0     0   100 |
|   price_far_from_sma200_great_volume |                            roi |       22 |           5.00 |            81.938 |          81.94 |   30 days, 0:52:00 |    22     0     0   100 |
| stochastic_oversold_adx_strong_trend |             trailing_stop_loss |       21 |           3.92 |            59.703 |          59.70 |            4:37:00 |    21     0     0   100 |
|      rsi_oversold_price_above_sma200 |                            roi |        8 |           5.00 |            23.127 |          23.13 |  24 days, 19:38:00 |     8     0     0   100 |
|   price_far_from_sma200_great_volume |                    exit_signal |       17 |           1.68 |            16.731 |          16.73 |   7 days, 10:35:00 |    17     0     0   100 |
|      rsi_oversold_price_above_sma200 |             trailing_stop_loss |        1 |           8.30 |             9.754 |           9.75 |            1:00:00 |     1     0     0   100 |
| stochastic_oversold_adx_strong_trend |                    exit_signal |        7 |           1.13 |             6.789 |           6.79 |   9 days, 18:51:00 |     7     0     0   100 |
|   price_far_from_sma200_great_volume |             trailing_stop_loss |        3 |           3.06 |             6.456 |           6.46 |            6:40:00 |     3     0     0   100 |
|      rsi_oversold_price_above_sma200 | death_cross_price_below_sma200 |        1 |           3.45 |             1.584 |           1.58 |    1 day, 19:00:00 |     1     0     0   100 |
|      rsi_oversold_price_above_sma200 |                    exit_signal |        1 |           2.09 |             0.795 |           0.80 |    2 days, 6:00:00 |     1     0     0   100 |
|   price_far_from_sma200_great_volume | death_cross_price_below_sma200 |        1 |           0.26 |             0.324 |           0.32 |           23:00:00 |     1     0     0   100 |
|   price_far_from_sma200_great_volume |                     force_exit |        2 |         -34.92 |           -92.305 |         -92.31 |  74 days, 14:30:00 |     0     0     2     0 |
| stochastic_oversold_adx_strong_trend |                     force_exit |        2 |         -43.62 |          -117.605 |        -117.61 | 123 days, 18:00:00 |     0     0     2     0 |
|                                TOTAL |                                |      173 |           3.32 |           279.244 |         279.24 |  12 days, 16:57:00 |   169     0     4  97.7 |
================== SUMMARY METRICS ==================
| Metric                      | Value               |
|-----------------------------+---------------------|
| Backtesting from            | 2023-01-02 00:00:00 |
| Backtesting to              | 2024-08-04 00:00:00 |
| Max open trades             | 4                   |
|                             |                     |
| Total/Daily Avg Trades      | 173 / 0.3           |
| Starting balance            | 100 USDT            |
| Final balance               | 379.244 USDT        |
| Absolute profit             | 279.244 USDT        |
| Total profit %              | 279.24%             |
| CAGR %                      | 131.38%             |
| Sortino                     | 0.66                |
| Sharpe                      | 1.05                |
| Calmar                      | 25.82               |
| Profit factor               | 2.33                |
| Expectancy (Ratio)          | 1.61 (0.03)         |
| Avg. daily profit %         | 0.48%               |
| Avg. stake amount           | 68.512 USDT         |
| Total trade volume          | 11852.544 USDT      |
|                             |                     |
| Best Pair                   | RAY/USDT 87.79%     |
| Worst Pair                  | LINK/USDT -37.81%   |
| Best trade                  | RAY/USDT 9.99%      |
| Worst trade                 | ADA/USDT -49.84%    |
| Best day                    | 23.831 USDT         |
| Worst day                   | -209.911 USDT       |
| Days win/draw/lose          | 120 / 458 / 1       |
| Avg. Duration Winners       | 10 days, 15:49:00   |
| Avg. Duration Loser         | 99 days, 4:15:00    |
| Max Consecutive Wins / Loss | 169 / 4             |
| Rejected Entry signals      | 3014                |
| Entry/Exit Timeouts         | 0 / 0               |
|                             |                     |
| Min balance                 | 100.384 USDT        |
| Max balance                 | 589.155 USDT        |
| Max % of account underwater | 35.63%              |
| Absolute Drawdown (Account) | 35.63%              |
| Absolute Drawdown           | 209.911 USDT        |
| Drawdown high               | 489.155 USDT        |
| Drawdown low                | 279.244 USDT        |
| Drawdown Start              | 2024-07-27 08:00:00 |
| Drawdown End                | 2024-08-04 00:00:00 |
| Market change               | 240.39%             |
=====================================================

Backtested 2023-01-02 00:00:00 -> 2024-08-04 00:00:00 | Max open trades : 4
================================================================= STRATEGY SUMMARY =================================================================
|   Strategy |   Trades |   Avg Profit % |   Tot Profit USDT |   Tot Profit % |      Avg Duration |   Win  Draw  Loss  Win% |             Drawdown |
|------------+----------+----------------+-------------------+----------------+-------------------+-------------------------+----------------------|
|    BusyGuy |      173 |           3.32 |           279.244 |         279.24 | 12 days, 16:57:00 |   169     0     4  97.7 | 209.911 USDT  35.63% |
====================================================================================================================================================

```