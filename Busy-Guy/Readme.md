# BusyGuy Strategy v1.1.0 @ 2024-08-09

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

## Data Download
### Bull Market from feb-2023 to july-2024 (YYYYMMDD)

`freqtrade download-data --timeframes 15m 1h 4h 1d --timerange 20230102-20240804 --config ./user_data/configs/config.json --config ./user_data/configs/BusyGuy.config.json`

## Backtesting and Optimization
### Change the timerange to correspond to the backtesting interval, so you will get similar results
```

freqtrade backtesting --strategy BusyGuy --timeframe 1h --timerange 20230102-2024084 --config ./user_data/configs/config.json --config ./user_data/configs/BusyGuy.config.json

freqtrade lookahead-analysis --strategy BusyGuy --timeframe 1h --cache none --dry-run-wallet 10000000 --stake-amount 1000 --enable-protections --timerange 20230102-20240804 --config ./user_data/configs/config.json --config ./user_data/configs/BusyGuy.config.json

freqtrade lookahead-analysis --strategy BusyGuy --timeframe 1h --cache none --dry-run-wallet 10000000 --stake-amount 1000 --enable-protections --timerange 20240101-20240804 --config ./user_data/configs/config.json --config ./user_data/configs/BusyGuy.config.json

```

### Attention to the limit of job workers your machine can handle.

```
freqtrade hyperopt --job-workers 2 --hyperopt-loss SharpeHyperOptLossDaily --spaces buy sell --strategy BusyGuy -e 200 --timeframe 1h --timerange 20230102-20240804 --config ./user_data/configs/config.json --config ./user_data/configs/BusyGuy.config.json

```


# Backtesting results - 20230102-20240804

`freqtrade backtesting --strategy BusyGuy --timeframe 1h --timerange 20230102-20240804 --config ./user_data/configs/config.json --config ./user_data/configs/BusyGuy.config.json`

```

===================================================== BACKTESTING REPORT =====================================================
|        Pair |   Trades |   Avg Profit % |   Tot Profit USDT |   Tot Profit % |      Avg Duration |   Win  Draw  Loss  Win% |
|-------------+----------+----------------+-------------------+----------------+-------------------+-------------------------|
|    RAY/USDT |       17 |           4.89 |            43.784 |          43.78 |   4 days, 3:32:00 |    17     0     0   100 |
|   NEAR/USDT |       14 |           4.84 |            41.938 |          41.94 |    1 day, 3:04:00 |    14     0     0   100 |
|   BAKE/USDT |       11 |           5.07 |            33.215 |          33.21 | 12 days, 10:33:00 |    11     0     0   100 |
|    INJ/USDT |       13 |           3.98 |            33.164 |          33.16 |   9 days, 1:28:00 |    13     0     0   100 |
| PEOPLE/USDT |       10 |           4.40 |            32.116 |          32.12 |  32 days, 4:18:00 |    10     0     0   100 |
|   DOGE/USDT |        8 |           5.07 |            29.340 |          29.34 |   1 day, 19:22:00 |     8     0     0   100 |
|    SOL/USDT |       11 |           4.48 |            26.714 |          26.71 | 10 days, 12:16:00 |    11     0     0   100 |
|   PEPE/USDT |        6 |           3.64 |            20.097 |          20.10 |   3 days, 1:20:00 |     6     0     0   100 |
|    BCH/USDT |        8 |           4.40 |            19.274 |          19.27 | 15 days, 13:00:00 |     8     0     0   100 |
|    WIF/USDT |        2 |           5.28 |            12.201 |          12.20 |          11:00:00 |     2     0     0   100 |
|    XRP/USDT |        4 |           4.18 |            10.533 |          10.53 |  48 days, 0:00:00 |     3     0     1  75.0 |
|    LTC/USDT |        6 |           4.51 |            10.006 |          10.01 | 24 days, 21:30:00 |     6     0     0   100 |
|    ETH/USDT |        6 |           3.68 |             8.579 |           8.58 | 24 days, 13:30:00 |     6     0     0   100 |
|   SHIB/USDT |        2 |           6.18 |             8.240 |           8.24 |  4 days, 15:00:00 |     2     0     0   100 |
|    NOT/USDT |        0 |           0.00 |             0.000 |           0.00 |              0:00 |     0     0     0     0 |
|    BTC/USDT |        6 |           1.98 |            -2.023 |          -2.02 | 54 days, 22:50:00 |     5     0     1  83.3 |
|    BNB/USDT |        8 |           1.96 |            -4.423 |          -4.42 |  10 days, 8:08:00 |     7     0     1  87.5 |
|   CTSI/USDT |       15 |          -0.52 |           -49.766 |         -49.77 |  27 days, 2:44:00 |    14     0     1  93.3 |
|       TOTAL |      147 |           3.80 |           272.988 |         272.99 |  15 days, 7:55:00 |   143     0     4  97.3 |
================================================= LEFT OPEN TRADES REPORT ==================================================
|     Pair |   Trades |   Avg Profit % |   Tot Profit USDT |   Tot Profit % |       Avg Duration |   Win  Draw  Loss  Win% |
|----------+----------+----------------+-------------------+----------------+--------------------+-------------------------|
| ETH/USDT |        1 |           1.37 |             0.947 |           0.95 |            2:00:00 |     1     0     0   100 |
| XRP/USDT |        1 |          -3.62 |            -4.029 |          -4.03 | 146 days, 17:00:00 |     0     0     1     0 |
| BTC/USDT |        1 |         -13.10 |           -14.215 |         -14.21 |  147 days, 8:00:00 |     0     0     1     0 |
| BNB/USDT |        1 |         -15.09 |           -18.090 |         -18.09 |  54 days, 15:00:00 |     0     0     1     0 |
|    TOTAL |        4 |          -7.61 |           -35.386 |         -35.39 |   87 days, 4:30:00 |     1     0     3  25.0 |
=================================================================== ENTER TAG STATS ====================================================================
|                            Enter Tag |   Entries |   Avg Profit % |   Tot Profit USDT |   Tot Profit % |      Avg Duration |   Win  Draw  Loss  Win% |
|--------------------------------------+-----------+----------------+-------------------+----------------+-------------------+-------------------------|
| stochastic_oversold_adx_strong_trend |       116 |           4.54 |           296.539 |         296.54 | 12 days, 13:56:00 |   116     0     0   100 |
|      rsi_oversold_price_above_sma200 |         7 |           2.01 |             1.852 |           1.85 | 31 days, 10:51:00 |     6     0     1  85.7 |
|   price_far_from_sma200_great_volume |        24 |           0.70 |           -25.404 |         -25.40 | 23 days, 22:00:00 |    21     0     3  87.5 |
|                                TOTAL |       147 |           3.80 |           272.988 |         272.99 |  15 days, 7:55:00 |   143     0     4  97.3 |
========================================================= EXIT REASON STATS =========================================================
|        Exit Reason |   Exits |   Avg Profit % |   Tot Profit USDT |   Tot Profit % |       Avg Duration |   Win  Draw  Loss  Win% |
|--------------------+---------+----------------+-------------------+----------------+--------------------+-------------------------|
|                roi |     102 |           5.08 |           284.838 |         284.84 |  16 days, 10:58:00 |   102     0     0   100 |
| trailing_stop_loss |      32 |           4.13 |            98.142 |          98.14 |            4:26:00 |    32     0     0   100 |
|        exit_signal |       8 |           1.00 |             3.410 |           3.41 |   9 days, 15:45:00 |     8     0     0   100 |
|         force_exit |       4 |          -7.61 |           -35.386 |         -35.39 |   87 days, 4:30:00 |     1     0     3  25.0 |
|          stop_loss |       1 |         -70.06 |           -78.017 |         -78.02 | 142 days, 23:00:00 |     0     0     1     0 |
|              TOTAL |     147 |           3.80 |           272.988 |         272.99 |   15 days, 7:55:00 |   143     0     4  97.3 |
======================================================================================== MIXED TAG STATS =========================================================================================
|                                                      Enter Tag |   Exit Reason |   Trades |   Avg Profit % |   Tot Profit USDT |   Tot Profit % |       Avg Duration |   Win  Draw  Loss  Win% |
|----------------------------------------------------------------+---------------+----------+----------------+-------------------+----------------+--------------------+-------------------------|
|                ('stochastic_oversold_adx_strong_trend', 'roi') |               |       83 |           5.06 |           223.046 |         223.05 |  16 days, 14:59:00 |    83     0     0   100 |
| ('stochastic_oversold_adx_strong_trend', 'trailing_stop_loss') |               |       26 |           3.90 |            70.878 |          70.88 |            4:09:00 |    26     0     0   100 |
|                  ('price_far_from_sma200_great_volume', 'roi') |               |       16 |           5.23 |            54.995 |          55.00 |   14 days, 6:22:00 |    16     0     0   100 |
|   ('price_far_from_sma200_great_volume', 'trailing_stop_loss') |               |        4 |           5.16 |            18.789 |          18.79 |            8:15:00 |     4     0     0   100 |
|      ('rsi_oversold_price_above_sma200', 'trailing_stop_loss') |               |        2 |           5.05 |             8.474 |           8.47 |            0:30:00 |     2     0     0   100 |
|                     ('rsi_oversold_price_above_sma200', 'roi') |               |        3 |           5.00 |             6.797 |           6.80 |  23 days, 12:20:00 |     3     0     0   100 |
|        ('stochastic_oversold_adx_strong_trend', 'exit_signal') |               |        7 |           0.84 |             2.615 |           2.61 |  10 days, 17:09:00 |     7     0     0   100 |
|             ('rsi_oversold_price_above_sma200', 'exit_signal') |               |        1 |           2.09 |             0.795 |           0.80 |    2 days, 6:00:00 |     1     0     0   100 |
|              ('rsi_oversold_price_above_sma200', 'force_exit') |               |        1 |         -13.10 |           -14.215 |         -14.21 |  147 days, 8:00:00 |     0     0     1     0 |
|           ('price_far_from_sma200_great_volume', 'force_exit') |               |        3 |          -5.78 |           -21.172 |         -21.17 |   67 days, 3:20:00 |     1     0     2  33.3 |
|            ('price_far_from_sma200_great_volume', 'stop_loss') |               |        1 |         -70.06 |           -78.017 |         -78.02 | 142 days, 23:00:00 |     0     0     1     0 |
|                                                          TOTAL |               |      147 |           3.80 |           272.988 |         272.99 |   15 days, 7:55:00 |   143     0     4  97.3 |
================== SUMMARY METRICS ==================
| Metric                      | Value               |
|-----------------------------+---------------------|
| Backtesting from            | 2023-01-02 00:00:00 |
| Backtesting to              | 2024-08-09 00:00:00 |
| Max open trades             | 4                   |
|                             |                     |
| Total/Daily Avg Trades      | 147 / 0.25          |
| Starting balance            | 100 USDT            |
| Final balance               | 372.988 USDT        |
| Absolute profit             | 272.988 USDT        |
| Total profit %              | 272.99%             |
| CAGR %                      | 127.35%             |
| Sortino                     | 0.31                |
| Sharpe                      | 1.24                |
| Calmar                      | 40.00               |
| Profit factor               | 3.39                |
| Expectancy (Ratio)          | 1.86 (0.06)         |
| Avg. daily profit %         | 0.47%               |
| Avg. stake amount           | 59.16 USDT          |
| Total trade volume          | 8696.497 USDT       |
|                             |                     |
| Best Pair                   | RAY/USDT 43.78%     |
| Worst Pair                  | CTSI/USDT -49.77%   |
| Best trade                  | XRP/USDT 10.33%     |
| Worst trade                 | CTSI/USDT -70.06%   |
| Best day                    | 22.038 USDT         |
| Worst day                   | -78.017 USDT        |
| Days win/draw/lose          | 98 / 484 / 2        |
| Avg. Duration Winners       | 12 days, 7:42:00    |
| Avg. Duration Loser         | 122 days, 21:45:00  |
| Max Consecutive Wins / Loss | 140 / 2             |
| Rejected Entry signals      | 2934                |
| Entry/Exit Timeouts         | 0 / 0               |
|                             |                     |
| Min balance                 | 101.25 USDT         |
| Max balance                 | 479.972 USDT        |
| Max % of account underwater | 22.29%              |
| Absolute Drawdown (Account) | 22.29%              |
| Absolute Drawdown           | 106.984 USDT        |
| Drawdown high               | 379.972 USDT        |
| Drawdown low                | 272.988 USDT        |
| Drawdown Start              | 2024-06-15 06:00:00 |
| Drawdown End                | 2024-08-09 00:00:00 |
| Market change               | 309.92%             |
=====================================================

Backtested 2023-01-02 00:00:00 -> 2024-08-09 00:00:00 | Max open trades : 4
================================================================= STRATEGY SUMMARY ================================================================
|   Strategy |   Trades |   Avg Profit % |   Tot Profit USDT |   Tot Profit % |     Avg Duration |   Win  Draw  Loss  Win% |             Drawdown |
|------------+----------+----------------+-------------------+----------------+------------------+-------------------------+----------------------|
|    BusyGuy |      147 |           3.80 |           272.988 |         272.99 | 15 days, 7:55:00 |   143     0     4  97.3 | 106.984 USDT  22.29% |
===================================================================================================================================================

```