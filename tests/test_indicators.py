""" Tests for indicators module """

# Import used libraries
import pytest
import pandas as pd

from riskoptimix.indicators import sma, ema, rsi
from riskoptimix.exceptions import ValidationError


def test_sma():
    """ Test SMA function """
    prices = pd.Series([1, 2, 3, 4, 5])
    result = sma(prices, period=2)

    assert len(result) == len(prices)
    assert result.iloc[-1] == 4.5


def test_sma_invalid_period():
    """ Test SMA function with invalid period """
    prices = pd.Series([1, 2, 3, 4, 5])
    with pytest.raises(ValidationError):
        sma(prices, period=0)


def test_rsi():
    """Test RSI calculation"""
    # Create sample price data
    prices = pd.Series([44, 44.34, 44.09, 43.61, 44.33, 44.83, 45.10, 45.42,
                       45.84, 46.08, 45.89, 46.03, 45.61, 46.28, 46.28])
    
    result = rsi(prices, period=14)
    
    assert len(result) == len(prices)
    assert 0 <= result.iloc[-1] <= 100  # RSI should be between 0 and 100


if __name__ == "__main__":
    pytest.main()