This strategy will use three indicators to identify buying opportunities during low seasons and will sell after achieving a 1-5% profit. 

1. **Relative Strength Index (RSI)**: To identify overbought or oversold conditions.
2. **Moving Average Convergence Divergence (MACD)**: To determine the trend direction and strength.
3. **Bollinger Bands**: To identify volatility and potential reversal points.

Additionally, we'll add some custom rules to ensure better trade management.


### Strategy Explanation:

1. **Indicators**:
    - **RSI**: Buy when RSI < 30 (indicating oversold), and sell when RSI > 70 (indicating overbought).
    - **MACD**: Buy when MACD crosses above the signal line, indicating a bullish trend.
    - **Bollinger Bands**: Buy when the price is below the lower Bollinger Band (indicating potential price reversal).

2. **Buy Condition**:
    - RSI is less than 30.
    - MACD is above the signal line.
    - Price is below the lower Bollinger Band.

3. **Sell Condition**:
    - RSI is greater than 70.
    - Price is above the upper Bollinger Band.

4. **Minimal ROI**:
    - 5% profit target initially, but if the trade lasts for 30 minutes, the target reduces to 3%, and if it lasts for 60 minutes, the target reduces to 1%.

5. **Stoploss and Trailing Stop**:
    - 5% stoploss to limit losses.
    - Trailing stop to lock in profits once the price moves 2% in the desired direction with a trailing threshold of 1%.

### Backtesting