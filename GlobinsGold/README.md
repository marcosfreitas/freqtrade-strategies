# Globin's Gold

Working in a 5min time frame;

## Strategies

### 2 SMA Crossover
A shorter-term (yellow) and a longer-term (blue) MA. When this shorter-term crosses the longer-term it is a potential signal of trend change.

Shorter-term MA default period: **5**
Longer-term MA default period: **20**

Example:

![link](./images/2-sma-crossover.png "2 SMAs Crossover")

### 2 Short MA types Crossover(experimental)

A EMA vs SMA shorter-term flowlines crossing each other.

@todo implement tests and description

notes:
seems that PROXIMITY factor can be used to check a uptrend
![link](./images/2-shorter-term-ema-sma.png "2 Short MA types")

#### Backtesting report
**Updated at October 11, 2021**

```
======================================================= SELL REASON STATS ========================================================
|        Sell Reason |   Sells |   Win  Draws  Loss  Win% |   Avg Profit % |   Cum Profit % |   Tot Profit BUSD |   Tot Profit % |
|--------------------+---------+--------------------------+----------------+----------------+-------------------+----------------|
|                roi |     714 |    353   361     0   100 |           1    |         716.4  |           367.824 |         119.4  |
| trailing_stop_loss |      18 |      2     0    16  11.1 |         -24.61 |        -442.92 |          -252.498 |         -73.82 |
|        sell_signal |       9 |      1     0     8  11.1 |          -7.23 |         -65.1  |           -33.467 |         -10.85 |
|         force_sell |       6 |      0     0     6     0 |          -6.25 |         -37.48 |           -20.31  |          -6.25 |


=============== SUMMARY METRICS ================
| Metric                 | Value               |
|------------------------+---------------------|
| Backtesting from       | 2021-08-01 00:00:00 |
| Backtesting to         | 2021-10-07 03:05:00 |
| Max open trades        | 6                   |
|                        |                     |
| Total/Daily Avg Trades | 747 / 11.15         |
| Starting balance       | 250.000 BUSD        |
| Final balance          | 311.550 BUSD        |
| Absolute profit        | 61.550 BUSD         |
| Total profit %         | 24.62%              |
| Avg. stake amount      | 51.562 BUSD         |
| Total trade volume     | 38517.037 BUSD      |
|                        |                     |
| Best Pair              | XEC/BUSD 29.49%     |
| Worst Pair             | SLP/BUSD -66.07%    |
| Best trade             | TVK/BUSD 17.78%     |
| Worst trade            | SOL/BUSD -28.73%    |
| Best day               | 19.465 BUSD         |
| Worst day              | -76.812 BUSD        |
| Days win/draw/lose     | 45 / 10 / 13        |
| Avg. Duration Winners  | 1:37:00             |
| Avg. Duration Loser    | 4 days, 4:43:00     |
| Rejected Buy signals   | 1286660             |
|                        |                     |
| Min balance            | 250.232 BUSD        |
| Max balance            | 389.633 BUSD        |
| Drawdown               | 169.46%             |
| Drawdown               | 105.073 BUSD        |
| Drawdown high          | 139.633 BUSD        |
| Drawdown low           | 34.560 BUSD         |
| Drawdown Start         | 2021-09-07 12:45:00 |
| Drawdown End           | 2021-09-07 15:05:00 |
| Market change          | 89.73%              |
================================================
```