# Technical Indicators Documentation

This document provides documentation for all technical indicators available in the RiskOptimix library.

## Table of Contents

1. [Basic Indicators](#basic-indicators)
2. [Momentum Indicators](#momentum-indicators)
3. [Volatility Indicators](#volatility-indicators)
4. [Volume Indicators](#volume-indicators)
5. [Trend Indicators](#trend-indicators)
6. [Usage Examples](#usage-examples)

---

## Basic Indicators

### Simple Moving Average (SMA)

The Simple Moving Average is the arithmetic mean of prices over a specified period.

**Mathematical Formula:**

$$SMA_n = \frac{1}{n} \sum_{i=0}^{n-1} P_{t-i}$$

Where:
- $SMA_n$ = Simple Moving Average for period $n$
- $P_t$ = Price at time $t$
- $n$ = Number of periods

**Purpose:**
- Smooths price data to identify trend direction
- Reduces noise in price movements
- Acts as dynamic support/resistance levels

**Parameters:**
- `period` (int, default=20): Number of periods for calculation

**Usage:**
```python
from riskoptimix.indicators import sma
df['SMA_20'] = sma(df['close'], period=20)
```

---

### Exponential Moving Average (EMA)

The Exponential Moving Average gives more weight to recent prices, making it more responsive to new information than SMA.

**Mathematical Formula:**

$$EMA_t = \alpha \cdot P_t + (1 - \alpha) \cdot EMA_{t-1}$$

Where:
- $\alpha = \frac{2}{n + 1}$ (smoothing factor)
- $P_t$ = Price at time $t$
- $n$ = Period
- $EMA_0 = P_0$ (first EMA value equals first price)

**Purpose:**
- More responsive to recent price changes than SMA
- Better for trend following in volatile markets
- Commonly used in other indicators (MACD, etc.)

**Parameters:**
- `period` (int, default=20): Number of periods for calculation

**Usage:**
```python
from riskoptimix.indicators import ema
df['EMA_20'] = ema(df['close'], period=20)
```

---

## Momentum Indicators

### Relative Strength Index (RSI)

RSI measures the magnitude of recent price changes to evaluate overbought or oversold conditions.

**Mathematical Formula:**

$$RSI = 100 - \frac{100}{1 + RS}$$

$$RS = \frac{Average\ Gain}{Average\ Loss}$$

Where:
- Average Gain = $\frac{1}{n} \sum_{i=0}^{n-1} \max(P_{t-i} - P_{t-i-1}, 0)$
- Average Loss = $\frac{1}{n} \sum_{i=0}^{n-1} \max(P_{t-i-1} - P_{t-i}, 0)$

**Purpose:**
- Identifies overbought (RSI > 70) and oversold (RSI < 30) conditions
- Momentum oscillator ranging from 0 to 100
- Divergence analysis for trend reversal signals

**Parameters:**
- `period` (int, default=14): Number of periods for calculation

**Usage:**
```python
from riskoptimix.indicators import rsi
df['RSI_14'] = rsi(df['close'], period=14)
```

---

### Moving Average Convergence Divergence (MACD)

MACD shows the relationship between two moving averages of a security's price.

**Mathematical Formula:**

$$MACD = EMA_{fast} - EMA_{slow}$$
$$Signal = EMA(MACD, signal\_period)$$
$$Histogram = MACD - Signal$$

**Purpose:**
- Trend following momentum indicator
- Buy signals when MACD crosses above signal line
- Sell signals when MACD crosses below signal line
- Histogram shows momentum strength

**Parameters:**
- `fast_period` (int, default=12): Fast EMA period
- `slow_period` (int, default=26): Slow EMA period  
- `signal_period` (int, default=9): Signal line EMA period

**Returns:** DataFrame with columns: `macd`, `signal`, `histogram`

**Usage:**
```python
from riskoptimix.indicators import macd
macd_data = macd(df['close'])
df['MACD'] = macd_data['macd']
df['MACD_Signal'] = macd_data['signal']
df['MACD_Histogram'] = macd_data['histogram']
```

---

### Stochastic Oscillator

The Stochastic Oscillator compares a particular closing price to a range of prices over time.

**Mathematical Formula:**

$$\%K = \frac{C - L_n}{H_n - L_n} \times 100$$
$$\%D = SMA(\%K, smooth\_d)$$

Where:
- $C$ = Current closing price
- $L_n$ = Lowest price over last $n$ periods
- $H_n$ = Highest price over last $n$ periods

**Purpose:**
- Momentum oscillator ranging from 0 to 100
- Overbought when > 80, oversold when < 20
- %K line crossovers with %D line generate signals

**Parameters:**
- `period` (int, default=14): Lookback period
- `smooth_k` (int, default=3): %K smoothing periods
- `smooth_d` (int, default=3): %D smoothing periods

**Returns:** DataFrame with columns: `k`, `d`

**Usage:**
```python
from riskoptimix.indicators import stochastic
stoch_data = stochastic(df['high'], df['low'], df['close'])
df['Stoch_K'] = stoch_data['k']
df['Stoch_D'] = stoch_data['d']
```

---

### Rate of Change (ROC)

ROC measures the percentage change in price from n periods ago.

**Mathematical Formula:**

$$ROC = \frac{P_t - P_{t-n}}{P_{t-n}} \times 100$$

Where:
- $P_t$ = Current price
- $P_{t-n}$ = Price $n$ periods ago

**Purpose:**
- Momentum oscillator around zero line
- Positive values indicate upward momentum
- Negative values indicate downward momentum
- Divergences can signal trend reversals

**Parameters:**
- `period` (int, default=10): Number of periods for calculation

**Usage:**
```python
from riskoptimix.indicators import rate_of_change
df['ROC_10'] = rate_of_change(df['close'], period=10)
```

---

## Volatility Indicators

### Bollinger Bands

Bollinger Bands consist of a middle band (SMA) and two outer bands at standard deviations above and below.

**Mathematical Formula:**

$$Middle\ Band = SMA_n$$
$$Upper\ Band = SMA_n + (k \times \sigma_n)$$
$$Lower\ Band = SMA_n - (k \times \sigma_n)$$

Where:
- $\sigma_n$ = Standard deviation over $n$ periods
- $k$ = Number of standard deviations (typically 2)

**Purpose:**
- Identify overbought/oversold conditions
- Price tends to return to middle band
- Band width indicates volatility
- Squeeze patterns signal potential breakouts

**Parameters:**
- `period` (int, default=20): Period for SMA and standard deviation
- `std_dev` (int, default=2): Number of standard deviations

**Returns:** DataFrame with columns: `middle`, `upper`, `lower`

**Usage:**
```python
from riskoptimix.indicators import bollinger_bands
bb_data = bollinger_bands(df['close'])
df['BB_Middle'] = bb_data['middle']
df['BB_Upper'] = bb_data['upper']
df['BB_Lower'] = bb_data['lower']
```

---

### Average True Range (ATR)

ATR measures market volatility by decomposing the entire range of an asset price for that period.

**Mathematical Formula:**

$$TR = \max(H_t - L_t, |H_t - C_{t-1}|, |L_t - C_{t-1}|)$$
$$ATR = SMA(TR, n)$$

Where:
- $H_t$ = Current high
- $L_t$ = Current low  
- $C_{t-1}$ = Previous close
- $TR$ = True Range

**Purpose:**
- Measures volatility, not price direction
- Higher ATR indicates higher volatility
- Used for position sizing and stop-loss placement
- Trend strength indicator

**Parameters:**
- `period` (int, default=14): Number of periods for ATR calculation

**Usage:**
```python
from riskoptimix.indicators import atr
df['ATR_14'] = atr(df['high'], df['low'], df['close'], period=14)
```

---

### Volatility (Standard Deviation of Returns)

Calculates the standard deviation of price returns over a specified period.

**Mathematical Formula:**

$$Volatility = \sqrt{\frac{1}{n-1} \sum_{i=1}^{n} (r_i - \bar{r})^2}$$

Where:
- $r_i = \frac{P_i - P_{i-1}}{P_{i-1}}$ (return at period $i$)
- $\bar{r}$ = Mean return over $n$ periods

**Annualized Volatility:**
$$Annualized\ Volatility = Volatility \times \sqrt{252}$$

**Purpose:**
- Direct measure of price volatility
- Risk assessment tool
- Portfolio optimization input
- Market regime identification

**Parameters:**
- `period` (int, default=20): Number of periods
- `annualized` (bool, default=False): Whether to annualize the result

**Usage:**
```python
from riskoptimix.indicators import volatility
df['Volatility_20'] = volatility(df['close'], period=20)
df['Vol_Annualized'] = volatility(df['close'], period=20, annualized=True)
```

---

## Volume Indicators

### On-Balance Volume (OBV)

OBV uses volume flow to predict changes in stock price.

**Mathematical Formula:**

$$OBV_t = \begin{cases}
OBV_{t-1} + Volume_t & \text{if } Close_t > Close_{t-1} \\
OBV_{t-1} - Volume_t & \text{if } Close_t < Close_{t-1} \\
OBV_{t-1} & \text{if } Close_t = Close_{t-1}
\end{cases}$$

**Purpose:**
- Confirms price trends with volume
- Divergences can signal trend reversals
- Rising OBV suggests accumulation
- Falling OBV suggests distribution

**Usage:**
```python
from riskoptimix.indicators import obv
df['OBV'] = obv(df['close'], df['volume'])
```

---

### Volume Weighted Average Price (VWAP)

VWAP gives average price weighted by volume, typically calculated from market open.

**Mathematical Formula:**

$$VWAP = \frac{\sum_{i=1}^{n} (P_i \times V_i)}{\sum_{i=1}^{n} V_i}$$

Where:
- $P_i$ = Typical price = $\frac{High_i + Low_i + Close_i}{3}$
- $V_i$ = Volume at period $i$

**Purpose:**
- Institutional trading benchmark
- Support/resistance levels
- Trend confirmation
- Execution quality measurement

**Usage:**
```python
from riskoptimix.indicators import vwap
df['VWAP'] = vwap(df['high'], df['low'], df['close'], df['volume'])
```

---

### Volume Ratio

Compares current volume to average volume over a specified period.

**Mathematical Formula:**

$$Volume\ Ratio = \frac{Volume_t}{SMA(Volume, n)}$$

**Purpose:**
- Identifies unusual volume activity
- Confirms breakouts and breakdowns
- Values > 1 indicate above-average volume
- Values < 1 indicate below-average volume

**Parameters:**
- `period` (int, default=20): Period for average volume calculation

**Usage:**
```python
from riskoptimix.indicators import volume_ratio
df['Volume_Ratio'] = volume_ratio(df['volume'], period=20)
```

---

## Trend Indicators

### Average Directional Index (ADX)

ADX measures the strength of a trend without regard to trend direction.

**Mathematical Formula:**

1. **True Range (TR):**
   $$TR = \max(H_t - L_t, |H_t - C_{t-1}|, |L_t - C_{t-1}|)$$

2. **Directional Movements:**
   $$+DM = \begin{cases}
   H_t - H_{t-1} & \text{if } H_t - H_{t-1} > L_{t-1} - L_t \text{ and } H_t - H_{t-1} > 0 \\
   0 & \text{otherwise}
   \end{cases}$$
   
   $$-DM = \begin{cases}
   L_{t-1} - L_t & \text{if } L_{t-1} - L_t > H_t - H_{t-1} \text{ and } L_{t-1} - L_t > 0 \\
   0 & \text{otherwise}
   \end{cases}$$

3. **Smoothed values using Wilder's smoothing:**
   $$+DI = 100 \times \frac{Smoothed\ +DM}{Smoothed\ TR}$$
   $$-DI = 100 \times \frac{Smoothed\ -DM}{Smoothed\ TR}$$

4. **Directional Index (DX):**
   $$DX = 100 \times \frac{|+DI - (-DI)|}{+DI + (-DI)}$$

5. **Average Directional Index:**
   $$ADX = Smoothed\ DX$$

**Purpose:**
- Measures trend strength (0-100 scale)
- ADX > 25 indicates strong trend
- ADX < 20 indicates weak/sideways trend
- Does not indicate trend direction

**Parameters:**
- `period` (int, default=14): Period for calculation

**Usage:**
```python
from riskoptimix.indicators import adx
df['ADX_14'] = adx(df['high'], df['low'], df['close'], period=14)
```

---

## Usage Examples

### Basic Usage

```python
import riskoptimix as ro
from riskoptimix.indicators import sma, ema, rsi, bollinger_bands

# Fetch data
df = ro.get_data('AAPL', start='2024-01-01', end='2024-12-31')

# Calculate individual indicators
df['SMA_20'] = sma(df['close'], period=20)
df['EMA_20'] = ema(df['close'], period=20)
df['RSI_14'] = rsi(df['close'], period=14)

# Multi-column indicators
bb_data = bollinger_bands(df['close'], period=20, std_dev=2)
df['BB_Upper'] = bb_data['upper']
df['BB_Middle'] = bb_data['middle']
df['BB_Lower'] = bb_data['lower']
```

### Batch Processing

```python
from riskoptimix.indicators import prepare_data

# Apply momentum indicators
df_momentum = prepare_data(df, profile='momentum')

# Apply custom indicators
df_custom = prepare_data(
    df, 
    profile='custom',
    custom_indicators=['sma_10', 'sma_50', 'rsi_21', 'bb', 'macd']
)

# Apply all indicators
df_full = prepare_data(df, profile='all')
```

### Strategy Example

```python
# Simple crossover strategy
df['SMA_Fast'] = sma(df['close'], period=10)
df['SMA_Slow'] = sma(df['close'], period=30)

# Generate signals
df['Signal'] = 0
df.loc[df['SMA_Fast'] > df['SMA_Slow'], 'Signal'] = 1  # Buy
df.loc[df['SMA_Fast'] < df['SMA_Slow'], 'Signal'] = -1  # Sell

# Add RSI filter
df.loc[df['RSI_14'] > 70, 'Signal'] = 0  # No position when overbought
df.loc[df['RSI_14'] < 30, 'Signal'] = 0  # No position when oversold
```

---

## Notes

- All indicators handle missing data appropriately
- Period parameters must be positive integers
- Some indicators require multiple price series (high, low, close, volume)
- Results may contain NaN values for initial periods where insufficient data exists
- For financial analysis, consider the market context and combine multiple indicators
- Always validate results and consider transaction costs in practical applications

---
