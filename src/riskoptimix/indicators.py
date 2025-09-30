""" Technical indicators for trading """

# Import used libraries
import pandas as pd

from .exceptions import ValidationError

def sma(prices: pd.Series, period: int = 20) -> pd.Series:
    """ Calculate the Simple Moving Average (SMA) 
    
    Parameters
    ----------
    prices: pd.Series
        The prices to calculate the SMA for
    period: int, default 20
        The number of periods to calculate the SMA for

    Returns
    -------
    pd.Series
        The SMA values

    Raises
    ------
    ValidationError
        If the period is less than 1

    Examples
    --------
    >>> sma_20 = sma(df['close'], period=20)
    """

    if period < 1:
        raise ValidationError("Period must be at least 1")

    return prices.rolling(window=period).mean()


def ema(prices: pd.Series, period: int = 20) -> pd.Series:
    """ Calculate the Exponential Moving Average (EMA) 
    
    Parameters
    ----------
    prices: pd.Series
        The prices to calculate the EMA for
    period: int, default 20
        The number of periods to calculate the EMA for


    Returns
    ------- 
    pd.Series
        The EMA values

    Raises
    ------
    ValidationError
        If the period is less than 1

    Examples
    --------
    >>> ema_20 = ema(df['close'], period=20)
    """

    if period < 1:
        raise ValidationError("Period must be at least 1")
    
    return prices.ewm(span=period, adjust=False).mean()
    
    
def rsi(prices: pd.Series, period: int = 14) -> pd.Series:
    """ 
    Calculate the Relative Strength Index (RSI)

    Parameters
    ----------
    prices: pd.Series
        Series of prices
    period: int, default 14
        The number of periods to calculate the RSI for

    Returns
    -------
    pd.Series
        The RSI values (0-100)

    Raises
    ------
    ValidationError
        If the period is less than 1
    
    Examples
    --------
    >>> rsi_14 = rsi(df['close'], period=14)
    """

    if period < 1:
        raise ValidationError("Period must be at least 1")
    
    delta = prices.diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    return rsi
    