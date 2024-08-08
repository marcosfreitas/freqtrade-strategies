
## Details

This strategy had best performance on:
- with OR on buy condition, using indicators:

**bull market period:** interval of 15m and 1h and with a really volatily coin that was recently launched (2024).
Used indicators are very strict and may have too long periods without a buy signal, however it may means that the signal is really strong to buy.
**bear market period:** no enough results, no buy signals were generated.

- with AND on buy condition withou macd indicator:

**bull market period:** interval of 15m and 1h
**bear market period:** no enough results, no buy signals were generated.

## How to run the backtesting

```bash

freqtrade backtesting --strategy LowRider --timeframe 1h --config ./user_data/configs/config.json --config ./user_data/configs/low-rider.config.json --config ./user_data/configs/config_pairs_a.json

```

Intervals 15m, 1h, 4h, 1d, 1w

## Comparison results:


### 15m


Result for strategy LowRider
==================================================== BACKTESTING REPORT ===================================================
|        Pair |   Trades |   Avg Profit % |   Tot Profit USDT |   Tot Profit % |   Avg Duration |   Win  Draw  Loss  Win% |
|-------------+----------+----------------+-------------------+----------------+----------------+-------------------------|
|    WIF/USDT |       80 |           0.67 |             1.062 |           1.06 |       13:18:00 |    61     7    12  76.2 |
|    STG/USDT |        0 |           0.00 |             0.000 |           0.00 |           0:00 |     0     0     0     0 |
|   ARKM/USDT |        0 |           0.00 |             0.000 |           0.00 |           0:00 |     0     0     0     0 |
|    DYM/USDT |        0 |           0.00 |             0.000 |           0.00 |           0:00 |     0     0     0     0 |
|   HIFI/USDT |        0 |           0.00 |             0.000 |           0.00 |           0:00 |     0     0     0     0 |
|    ZEN/USDT |        0 |           0.00 |             0.000 |           0.00 |           0:00 |     0     0     0     0 |
|   LINK/USDT |        0 |           0.00 |             0.000 |           0.00 |           0:00 |     0     0     0     0 |
|    TRU/USDT |        0 |           0.00 |             0.000 |           0.00 |           0:00 |     0     0     0     0 |
|    XAI/USDT |        0 |           0.00 |             0.000 |           0.00 |           0:00 |     0     0     0     0 |
|    UMA/USDT |        0 |           0.00 |             0.000 |           0.00 |           0:00 |     0     0     0     0 |
|    GTC/USDT |        0 |           0.00 |             0.000 |           0.00 |           0:00 |     0     0     0     0 |
|   MOVR/USDT |        0 |           0.00 |             0.000 |           0.00 |           0:00 |     0     0     0     0 |
|   TNSR/USDT |        0 |           0.00 |             0.000 |           0.00 |           0:00 |     0     0     0     0 |
|   DYDX/USDT |        0 |           0.00 |             0.000 |           0.00 |           0:00 |     0     0     0     0 |
|   API3/USDT |        0 |           0.00 |             0.000 |           0.00 |           0:00 |     0     0     0     0 |
|    JUP/USDT |        0 |           0.00 |             0.000 |           0.00 |           0:00 |     0     0     0     0 |
|    FIL/USDT |        0 |           0.00 |             0.000 |           0.00 |           0:00 |     0     0     0     0 |
|  BEAMX/USDT |        0 |           0.00 |             0.000 |           0.00 |           0:00 |     0     0     0     0 |
|    ENJ/USDT |        0 |           0.00 |             0.000 |           0.00 |           0:00 |     0     0     0     0 |
|    MKR/USDT |        0 |           0.00 |             0.000 |           0.00 |           0:00 |     0     0     0     0 |
|   BAKE/USDT |        0 |           0.00 |             0.000 |           0.00 |           0:00 |     0     0     0     0 |
|   NEAR/USDT |        0 |           0.00 |             0.000 |           0.00 |           0:00 |     0     0     0     0 |
|    KEY/USDT |        0 |           0.00 |             0.000 |           0.00 |           0:00 |     0     0     0     0 |
|    ACE/USDT |        0 |           0.00 |             0.000 |           0.00 |           0:00 |     0     0     0     0 |
|   FIDA/USDT |        0 |           0.00 |             0.000 |           0.00 |           0:00 |     0     0     0     0 |
| PORTAL/USDT |        0 |           0.00 |             0.000 |           0.00 |           0:00 |     0     0     0     0 |
|    CKB/USDT |        0 |           0.00 |             0.000 |           0.00 |           0:00 |     0     0     0     0 |
|    CRV/USDT |        0 |           0.00 |             0.000 |           0.00 |           0:00 |     0     0     0     0 |
|   AEVO/USDT |        0 |           0.00 |             0.000 |           0.00 |           0:00 |     0     0     0     0 |
|    FTM/USDT |        0 |           0.00 |             0.000 |           0.00 |           0:00 |     0     0     0     0 |
|   HBAR/USDT |        0 |           0.00 |             0.000 |           0.00 |           0:00 |     0     0     0     0 |
|    ELF/USDT |        0 |           0.00 |             0.000 |           0.00 |           0:00 |     0     0     0     0 |
|    BTC/USDT |        0 |           0.00 |             0.000 |           0.00 |           0:00 |     0     0     0     0 |
|     AI/USDT |        0 |           0.00 |             0.000 |           0.00 |           0:00 |     0     0     0     0 |
|   OMNI/USDT |        0 |           0.00 |             0.000 |           0.00 |           0:00 |     0     0     0     0 |
|  MATIC/USDT |        0 |           0.00 |             0.000 |           0.00 |           0:00 |     0     0     0     0 |
|    GAS/USDT |        0 |           0.00 |             0.000 |           0.00 |           0:00 |     0     0     0     0 |
|   SAND/USDT |        0 |           0.00 |             0.000 |           0.00 |           0:00 |     0     0     0     0 |
|    BCH/USDT |        0 |           0.00 |             0.000 |           0.00 |           0:00 |     0     0     0     0 |
|   BICO/USDT |        0 |           0.00 |             0.000 |           0.00 |           0:00 |     0     0     0     0 |
|     ZK/USDT |        0 |           0.00 |             0.000 |           0.00 |           0:00 |     0     0     0     0 |
|    XLM/USDT |        0 |           0.00 |             0.000 |           0.00 |           0:00 |     0     0     0     0 |
|   MINA/USDT |        0 |           0.00 |             0.000 |           0.00 |           0:00 |     0     0     0     0 |
|    IMX/USDT |        0 |           0.00 |             0.000 |           0.00 |           0:00 |     0     0     0     0 |
|    INJ/USDT |        0 |           0.00 |             0.000 |           0.00 |           0:00 |     0     0     0     0 |
|       TOTAL |       80 |           0.67 |             1.062 |           1.06 |       13:18:00 |    61     7    12  76.2 |
============================================== LEFT OPEN TRADES REPORT ===============================================
|   Pair |   Trades |   Avg Profit % |   Tot Profit USDT |   Tot Profit % |   Avg Duration |   Win  Draw  Loss  Win% |
|--------+----------+----------------+-------------------+----------------+----------------+-------------------------|
|  TOTAL |        0 |           0.00 |             0.000 |           0.00 |           0:00 |     0     0     0     0 |
===================================================== ENTER TAG STATS ======================================================
|   Enter Tag |   Entries |   Avg Profit % |   Tot Profit USDT |   Tot Profit % |   Avg Duration |   Win  Draw  Loss  Win% |
|-------------+-----------+----------------+-------------------+----------------+----------------+-------------------------|
|       OTHER |        80 |           0.67 |             1.062 |           1.06 |       13:18:00 |    61     7    12  76.2 |
|       TOTAL |        80 |           0.67 |             1.062 |           1.06 |       13:18:00 |    61     7    12  76.2 |
===================================================== EXIT REASON STATS =====================================================
|   Exit Reason |   Exits |   Avg Profit % |   Tot Profit USDT |   Tot Profit % |    Avg Duration |   Win  Draw  Loss  Win% |
|---------------+---------+----------------+-------------------+----------------+-----------------+-------------------------|
|   exit_signal |      61 |           3.57 |             4.371 |           4.37 |         8:41:00 |    61     0     0   100 |
|           roi |       7 |           0.00 |             0.000 |           0.00 | 1 day, 11:26:00 |     0     7     0     0 |
|     stop_loss |      12 |         -13.67 |            -3.309 |          -3.31 |        23:51:00 |     0     0    12     0 |
|         TOTAL |      80 |           0.67 |             1.062 |           1.06 |        13:18:00 |    61     7    12  76.2 |
================================================================= MIXED TAG STATS ==================================================================
|           Enter Tag |   Exit Reason |   Trades |   Avg Profit % |   Tot Profit USDT |   Tot Profit % |    Avg Duration |   Win  Draw  Loss  Win% |
|---------------------+---------------+----------+----------------+-------------------+----------------+-----------------+-------------------------|
| ('', 'exit_signal') |               |       61 |           3.57 |             4.371 |           4.37 |         8:41:00 |    61     0     0   100 |
|         ('', 'roi') |               |        7 |           0.00 |             0.000 |           0.00 | 1 day, 11:26:00 |     0     7     0     0 |
|   ('', 'stop_loss') |               |       12 |         -13.67 |            -3.309 |          -3.31 |        23:51:00 |     0     0    12     0 |
|               TOTAL |               |       80 |           0.67 |             1.062 |           1.06 |        13:18:00 |    61     7    12  76.2 |
================== SUMMARY METRICS ==================
| Metric                      | Value               |
|-----------------------------+---------------------|
| Backtesting from            | 2023-01-02 07:30:00 |
| Backtesting to              | 2024-07-20 00:00:00 |
| Max open trades             | 45                  |
|                             |                     |
| Total/Daily Avg Trades      | 80 / 0.14           |
| Starting balance            | 100 USDT            |
| Final balance               | 101.062 USDT        |
| Absolute profit             | 1.062 USDT          |
| Total profit %              | 1.06%               |
| CAGR %                      | 0.69%               |
| Sortino                     | 24.82               |
| Sharpe                      | 0.26                |
| Calmar                      | 3.38                |
| Profit factor               | 1.32                |
| Expectancy (Ratio)          | 0.01 (-0.04)        |
| Avg. daily profit %         | 0.00%               |
| Avg. stake amount           | 2.009 USDT          |
| Total trade volume          | 160.696 USDT        |
|                             |                     |
| Best Pair                   | WIF/USDT 1.06%      |
| Worst Pair                  | STG/USDT 0.00%      |
| Best trade                  | WIF/USDT 13.85%     |
| Worst trade                 | WIF/USDT -13.67%    |
| Best day                    | 0.362 USDT          |
| Worst day                   | -0.525 USDT         |
| Days win/draw/lose          | 50 / 69 / 11        |
| Avg. Duration Winners       | 8:41:00             |
| Avg. Duration Loser         | 23:51:00            |
| Max Consecutive Wins / Loss | 14 / 3              |
| Rejected Entry signals      | 0                   |
| Entry/Exit Timeouts         | 0 / 0               |
|                             |                     |
| Min balance                 | 100.047 USDT        |
| Max balance                 | 101.967 USDT        |
| Max % of account underwater | 1.07%               |
| Absolute Drawdown (Account) | 1.07%               |
| Absolute Drawdown           | 1.087 USDT          |
| Drawdown high               | 1.967 USDT          |
| Drawdown low                | 0.88 USDT           |
| Drawdown Start              | 2024-06-12 04:15:00 |
| Drawdown End                | 2024-07-07 23:30:00 |
| Market change               | 122.07%             |
=====================================================

Backtested 2023-01-02 07:30:00 -> 2024-07-20 00:00:00 | Max open trades : 45
============================================================== STRATEGY SUMMARY ==============================================================
|   Strategy |   Trades |   Avg Profit % |   Tot Profit USDT |   Tot Profit % |   Avg Duration |   Win  Draw  Loss  Win% |          Drawdown |
|------------+----------+----------------+-------------------+----------------+----------------+-------------------------+-------------------|
|    LowRide |       80 |           0.67 |             1.062 |           1.06 |       13:18:00 |    61     7    12  76.2 | 1.087 USDT  1.07% |
==============================================================================================================================================

#### GPT Analysis

**Based on the backtesting results for the 15m interval, here are some insights:**

1. **Performance Overview**:
   - The strategy yielded a modest absolute profit of 1.062 USDT from a starting balance of 100 USDT over a period of approximately 1.5 years, translating to a total profit percentage of 1.06%. This suggests a conservative strategy with low risk and low return.

2. **Risk Metrics**:
   - The Sortino ratio is significantly high at 24.82, indicating a favorable risk-adjusted return, primarily due to the low downside volatility.
   - The Sharpe ratio is 0.26, which is relatively low, suggesting that the excess return over the risk-free rate is minimal.
   - The Calmar ratio is 3.38, showing that the annual return rate is over three times the maximum drawdown, which is a good indicator of risk-adjusted performance.

3. **Trade Dynamics**:
   - A total of 80 trades were executed, with an average profit of 0.67% per trade. This indicates a strategy that prioritizes precision over volume.
   - The win rate is high at 76.2%, with 61 wins out of 80 trades, showcasing the strategy's effectiveness in selecting profitable trades.
   - The average duration for winning trades is significantly shorter (8:41:00) compared to losing trades (23:51:00), suggesting that the strategy is quicker to take profits than to cut losses.

4. **Drawdowns**:
   - The maximum drawdown observed is relatively low at 1.07%, indicating a strategy that effectively manages losses and protects the account balance.
   - The drawdown period lasted from 2024-06-12 to 2024-07-07, which is relatively short, showing the strategy's ability to recover from losses quickly.

5. **Market Conditions**:
   - Despite the market experiencing a significant change of 122.07%, the strategy managed to maintain a positive, albeit modest, return. This suggests that the strategy may be more conservative and less responsive to major market movements.

6. **Best and Worst Performance**:
   - The best-performing pair was WIF/USDT with a profit of 1.06%, indicating specific market conditions or pairs where the strategy excels.
   - The worst-performing pair was STG/USDT with no profit, which could indicate areas for strategy improvement or pairs that are less compatible with the strategy.

7. **Profitability and Efficiency**:
   - The strategy's profitability is quite low in comparison to the overall market change, suggesting there might be room for optimization to capture more significant gains.
   - The profit factor of 1.32 indicates that the total gross profit is only slightly higher than the total gross loss, which, combined with a low average daily profit of 0.00%, points towards a very conservative strategy.

In summary, the strategy demonstrates a conservative approach with a high win rate and low drawdowns but yields modest returns. There may be opportunities to enhance profitability by adjusting the strategy to capture larger market movements or optimizing trade selection and exit criteria.

### 1h

Result for strategy LowRide
==================================================== BACKTESTING REPORT ===================================================
|        Pair |   Trades |   Avg Profit % |   Tot Profit USDT |   Tot Profit % |   Avg Duration |   Win  Draw  Loss  Win% |
|-------------+----------+----------------+-------------------+----------------+----------------+-------------------------|
|    WIF/USDT |       14 |           0.21 |             0.058 |           0.06 | 1 day, 0:39:00 |     6     6     2  42.9 |
|    STG/USDT |        0 |           0.00 |             0.000 |           0.00 |           0:00 |     0     0     0     0 |
|   ARKM/USDT |        0 |           0.00 |             0.000 |           0.00 |           0:00 |     0     0     0     0 |
|    DYM/USDT |        0 |           0.00 |             0.000 |           0.00 |           0:00 |     0     0     0     0 |
|   HIFI/USDT |        0 |           0.00 |             0.000 |           0.00 |           0:00 |     0     0     0     0 |
|    ZEN/USDT |        0 |           0.00 |             0.000 |           0.00 |           0:00 |     0     0     0     0 |
|   LINK/USDT |        0 |           0.00 |             0.000 |           0.00 |           0:00 |     0     0     0     0 |
|    TRU/USDT |        0 |           0.00 |             0.000 |           0.00 |           0:00 |     0     0     0     0 |
|    XAI/USDT |        0 |           0.00 |             0.000 |           0.00 |           0:00 |     0     0     0     0 |
|    UMA/USDT |        0 |           0.00 |             0.000 |           0.00 |           0:00 |     0     0     0     0 |
|    GTC/USDT |        0 |           0.00 |             0.000 |           0.00 |           0:00 |     0     0     0     0 |
|   MOVR/USDT |        0 |           0.00 |             0.000 |           0.00 |           0:00 |     0     0     0     0 |
|   TNSR/USDT |        0 |           0.00 |             0.000 |           0.00 |           0:00 |     0     0     0     0 |
|   DYDX/USDT |        0 |           0.00 |             0.000 |           0.00 |           0:00 |     0     0     0     0 |
|   API3/USDT |        0 |           0.00 |             0.000 |           0.00 |           0:00 |     0     0     0     0 |
|    JUP/USDT |        0 |           0.00 |             0.000 |           0.00 |           0:00 |     0     0     0     0 |
|    FIL/USDT |        0 |           0.00 |             0.000 |           0.00 |           0:00 |     0     0     0     0 |
|  BEAMX/USDT |        0 |           0.00 |             0.000 |           0.00 |           0:00 |     0     0     0     0 |
|    ENJ/USDT |        0 |           0.00 |             0.000 |           0.00 |           0:00 |     0     0     0     0 |
|    MKR/USDT |        0 |           0.00 |             0.000 |           0.00 |           0:00 |     0     0     0     0 |
|   BAKE/USDT |        0 |           0.00 |             0.000 |           0.00 |           0:00 |     0     0     0     0 |
|   NEAR/USDT |        0 |           0.00 |             0.000 |           0.00 |           0:00 |     0     0     0     0 |
|    KEY/USDT |        0 |           0.00 |             0.000 |           0.00 |           0:00 |     0     0     0     0 |
|    ACE/USDT |        0 |           0.00 |             0.000 |           0.00 |           0:00 |     0     0     0     0 |
|   FIDA/USDT |        0 |           0.00 |             0.000 |           0.00 |           0:00 |     0     0     0     0 |
| PORTAL/USDT |        0 |           0.00 |             0.000 |           0.00 |           0:00 |     0     0     0     0 |
|    CKB/USDT |        0 |           0.00 |             0.000 |           0.00 |           0:00 |     0     0     0     0 |
|    CRV/USDT |        0 |           0.00 |             0.000 |           0.00 |           0:00 |     0     0     0     0 |
|   AEVO/USDT |        0 |           0.00 |             0.000 |           0.00 |           0:00 |     0     0     0     0 |
|    FTM/USDT |        0 |           0.00 |             0.000 |           0.00 |           0:00 |     0     0     0     0 |
|   HBAR/USDT |        0 |           0.00 |             0.000 |           0.00 |           0:00 |     0     0     0     0 |
|    ELF/USDT |        0 |           0.00 |             0.000 |           0.00 |           0:00 |     0     0     0     0 |
|    BTC/USDT |        0 |           0.00 |             0.000 |           0.00 |           0:00 |     0     0     0     0 |
|     AI/USDT |        0 |           0.00 |             0.000 |           0.00 |           0:00 |     0     0     0     0 |
|   OMNI/USDT |        0 |           0.00 |             0.000 |           0.00 |           0:00 |     0     0     0     0 |
|  MATIC/USDT |        0 |           0.00 |             0.000 |           0.00 |           0:00 |     0     0     0     0 |
|    GAS/USDT |        0 |           0.00 |             0.000 |           0.00 |           0:00 |     0     0     0     0 |
|   SAND/USDT |        0 |           0.00 |             0.000 |           0.00 |           0:00 |     0     0     0     0 |
|    BCH/USDT |        0 |           0.00 |             0.000 |           0.00 |           0:00 |     0     0     0     0 |
|   BICO/USDT |        0 |           0.00 |             0.000 |           0.00 |           0:00 |     0     0     0     0 |
|     ZK/USDT |        0 |           0.00 |             0.000 |           0.00 |           0:00 |     0     0     0     0 |
|    XLM/USDT |        0 |           0.00 |             0.000 |           0.00 |           0:00 |     0     0     0     0 |
|   MINA/USDT |        0 |           0.00 |             0.000 |           0.00 |           0:00 |     0     0     0     0 |
|    IMX/USDT |        0 |           0.00 |             0.000 |           0.00 |           0:00 |     0     0     0     0 |
|    INJ/USDT |        0 |           0.00 |             0.000 |           0.00 |           0:00 |     0     0     0     0 |
|       TOTAL |       14 |           0.21 |             0.058 |           0.06 | 1 day, 0:39:00 |     6     6     2  42.9 |
============================================== LEFT OPEN TRADES REPORT ===============================================
|   Pair |   Trades |   Avg Profit % |   Tot Profit USDT |   Tot Profit % |   Avg Duration |   Win  Draw  Loss  Win% |
|--------+----------+----------------+-------------------+----------------+----------------+-------------------------|
|  TOTAL |        0 |           0.00 |             0.000 |           0.00 |           0:00 |     0     0     0     0 |
===================================================== ENTER TAG STATS ======================================================
|   Enter Tag |   Entries |   Avg Profit % |   Tot Profit USDT |   Tot Profit % |   Avg Duration |   Win  Draw  Loss  Win% |
|-------------+-----------+----------------+-------------------+----------------+----------------+-------------------------|
|       OTHER |        14 |           0.21 |             0.058 |           0.06 | 1 day, 0:39:00 |     6     6     2  42.9 |
|       TOTAL |        14 |           0.21 |             0.058 |           0.06 | 1 day, 0:39:00 |     6     6     2  42.9 |
==================================================== EXIT REASON STATS =====================================================
|   Exit Reason |   Exits |   Avg Profit % |   Tot Profit USDT |   Tot Profit % |   Avg Duration |   Win  Draw  Loss  Win% |
|---------------+---------+----------------+-------------------+----------------+----------------+-------------------------|
|           roi |      11 |           2.35 |             0.515 |           0.52 | 1 day, 2:55:00 |     5     6     0   100 |
|   exit_signal |       1 |           4.50 |             0.090 |           0.09 |       19:00:00 |     1     0     0   100 |
|     stop_loss |       2 |         -13.67 |            -0.547 |          -0.55 |       15:00:00 |     0     0     2     0 |
|         TOTAL |      14 |           0.21 |             0.058 |           0.06 | 1 day, 0:39:00 |     6     6     2  42.9 |
============================================================= MIXED TAG STATS =============================================================
|   Enter Tag |   Exit Reason |   Trades |   Avg Profit % |   Tot Profit USDT |   Tot Profit % |   Avg Duration |   Win  Draw  Loss  Win% |
|-------------+---------------+----------+----------------+-------------------+----------------+----------------+-------------------------|
|             |           roi |       11 |           2.35 |             0.515 |           0.52 | 1 day, 2:55:00 |     5     6     0   100 |
|             |   exit_signal |        1 |           4.50 |             0.090 |           0.09 |       19:00:00 |     1     0     0   100 |
|             |     stop_loss |        2 |         -13.67 |            -0.547 |          -0.55 |       15:00:00 |     0     0     2     0 |
|       TOTAL |               |       14 |           0.21 |             0.058 |           0.06 | 1 day, 0:39:00 |     6     6     2  42.9 |
================== SUMMARY METRICS ==================
| Metric                      | Value               |
|-----------------------------+---------------------|
| Backtesting from            | 2023-01-02 00:00:00 |
| Backtesting to              | 2024-07-20 00:00:00 |
| Max open trades             | 45                  |
|                             |                     |
| Total/Daily Avg Trades      | 14 / 0.02           |
| Starting balance            | 100 USDT            |
| Final balance               | 100.058 USDT        |
| Absolute profit             | 0.058 USDT          |
| Total profit %              | 0.06%               |
| CAGR %                      | 0.04%               |
| Sortino                     | 1.98                |
| Sharpe                      | 0.02                |
| Calmar                      | 0.43                |
| Profit factor               | 1.11                |
| Expectancy (Ratio)          | 0.00 (-0.41)        |
| Avg. daily profit %         | 0.00%               |
| Avg. stake amount           | 1.993 USDT          |
| Total trade volume          | 27.908 USDT         |
|                             |                     |
| Best Pair                   | WIF/USDT 0.06%      |
| Worst Pair                  | STG/USDT 0.00%      |
| Best trade                  | WIF/USDT 6.89%      |
| Worst trade                 | WIF/USDT -13.67%    |
| Best day                    | 0.138 USDT          |
| Worst day                   | -0.274 USDT         |
| Days win/draw/lose          | 6 / 83 / 2          |
| Avg. Duration Winners       | 19:20:00            |
| Avg. Duration Loser         | 15:00:00            |
| Max Consecutive Wins / Loss | 3 / 4               |
| Rejected Entry signals      | 0                   |
| Entry/Exit Timeouts         | 0 / 0               |
|                             |                     |
| Min balance                 | 100 USDT            |
| Max balance                 | 100.464 USDT        |
| Max % of account underwater | 0.45%               |
| Absolute Drawdown (Account) | 0.45%               |
| Absolute Drawdown           | 0.457 USDT          |
| Drawdown high               | 0.464 USDT          |
| Drawdown low                | 0.007 USDT          |
| Drawdown Start              | 2024-06-15 08:00:00 |
| Drawdown End                | 2024-07-04 01:00:00 |
| Market change               | 121.74%             |
=====================================================

Backtested 2023-01-02 00:00:00 -> 2024-07-20 00:00:00 | Max open trades : 45
============================================================== STRATEGY SUMMARY ==============================================================
|   Strategy |   Trades |   Avg Profit % |   Tot Profit USDT |   Tot Profit % |   Avg Duration |   Win  Draw  Loss  Win% |          Drawdown |
|------------+----------+----------------+-------------------+----------------+----------------+-------------------------+-------------------|
|    LowRide |       14 |           0.21 |             0.058 |           0.06 | 1 day, 0:39:00 |     6     6     2  42.9 | 0.457 USDT  0.45% |
==============================================================================================================================================

### GPT Analysis

Based on the backtesting results for the 1h interval, here are some insights:

1. **Performance Overview**:
   - The strategy yielded an absolute profit of 0.058 USDT from a starting balance of 100 USDT over approximately 1.5 years, resulting in a total profit percentage of 0.06%. This indicates a very conservative strategy with minimal returns.

2. **Risk Metrics**:
   - The Sortino ratio is 1.98, suggesting a reasonable risk-adjusted return considering the strategy's conservative nature.
   - The Sharpe ratio is very low at 0.02, indicating that the risk-adjusted returns are barely above the risk-free rate.
   - The Calmar ratio is 0.43, showing a low annual return rate compared to the maximum drawdown, which suggests a cautious strategy with limited downside risk.

3. **Trade Dynamics**:
   - A total of 14 trades were executed, with an average profit of 0.21% per trade. This low number of trades indicates a highly selective strategy.
   - The win rate is 42.9%, with 6 wins out of 14 trades. The strategy also had a significant number of draws (6), indicating that many trades neither won nor lost.

4. **Drawdowns**:
   - The maximum drawdown is minimal at 0.45%, indicating a strategy that effectively manages losses and protects the account balance.
   - The drawdown period was relatively short, lasting from 2024-06-15 to 2024-07-04, showing the strategy's ability to recover from losses quickly.

5. **Market Conditions**:
   - Despite the market experiencing a significant change of 121.74%, the strategy managed to maintain a positive return, albeit very modest. This suggests that the strategy is extremely conservative and may not capitalize on significant market movements.

6. **Best and Worst Performance**:
   - The best-performing pair was WIF/USDT with a profit of 0.06%, indicating specific market conditions or pairs where the strategy performs slightly better.
   - The worst-performing pair was STG/USDT with no profit, which could indicate areas for strategy improvement or pairs that are less compatible with the strategy.

7. **Profitability and Efficiency**:
   - The strategy's profitability is extremely low in comparison to the overall market change, suggesting there might be significant room for optimization to capture more substantial gains.
   - The profit factor of 1.11 indicates that the total gross profit is only slightly higher than the total gross loss, which, combined with an average daily profit of 0.00%, points towards a very conservative strategy.

In summary, the strategy demonstrates an extremely conservative approach with a low win rate and minimal returns. There may be opportunities to enhance profitability by adjusting the strategy to capture larger market movements or optimizing trade selection and exit criteria.


# Optimization

