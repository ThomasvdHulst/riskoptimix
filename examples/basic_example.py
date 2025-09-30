""" Basic example of how to use the riskoptimix package """

# Import used libraries
import riskoptimix as ro
from riskoptimix.indicators import sma, ema, rsi

def main():
    # Fetch data
    print("Fetching data...")
    df = ro.get_data('AAPL', start='2024-01-01', end='2024-12-31', interval='1d')
    print(f"Fetched {len(df)} rows of data")

    # Calculate indicators
    df['SMA_20'] = sma(df['close'], period=20)
    df['EMA_20'] = ema(df['close'], period=20)
    df['RSI_14'] = rsi(df['close'], period=14)

    # Simple strategy, buy when price crosses above SMA_20
    df['signal'] = 0
    df.loc[df['close'] > df['SMA_20'], 'signal'] = 1
    df.loc[df['close'] < df['SMA_20'], 'signal'] = -1

    # Print strategy
    print(df[['close', 'SMA_20', 'EMA_20', 'RSI_14', 'signal']].tail())


if __name__ == "__main__":
    main()