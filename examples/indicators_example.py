""" Examples of how to use the indicators module """

# Import used libraries
import riskoptimix as ro
from riskoptimix.indicators import prepare_data

def main():
    # Fetch some data
    df = ro.get_data('AAPL', start='2024-01-01', end='2024-12-31', interval='1d')

    print(f"Original columns:", df.columns.tolist())
    print(f"Original shape: {df.shape}")

    # Example 1: Basic profile
    print("\n" + "="*50)
    print("BASIC PROFILE")
    df_basic = prepare_data(df, profile='basic')
    print(f"Shape after basic indicators: {df_basic.shape}")
    print("New columns:", [col for col in df_basic.columns if col not in df.columns])
    
    # Example 2: Momentum profile
    print("\n" + "="*50)
    print("MOMENTUM PROFILE")
    df_momentum = prepare_data(df, profile='momentum')
    print(f"Shape after momentum indicators: {df_momentum.shape}")
    print("New columns:", [col for col in df_momentum.columns if col not in df.columns])
    
    # Example 3: Custom indicators
    print("\n" + "="*50)
    print("CUSTOM PROFILE")
    df_custom = prepare_data(
        df, 
        profile='custom',
        custom_indicators=['sma_10', 'sma_30', 'rsi_21', 'bb', 'vwap']
    )
    print(f"Shape after custom indicators: {df_custom.shape}")
    print("New columns:", [col for col in df_custom.columns if col not in df.columns])
    
    # Example 4: All indicators
    print("\n" + "="*50)
    print("ALL INDICATORS")
    df_full = prepare_data(df, profile='all')
    print(f"Shape after all indicators: {df_full.shape}")
    print(f"Total indicators added: {len(df_full.columns) - len(df.columns)}")


if __name__ == "__main__":
    main()