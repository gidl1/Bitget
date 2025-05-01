import numpy as np
import pandas as pd

def calculate_rsi(data, period: int = 14):
    """
    Berechnet den RSI (Relative Strength Index) auf Basis eines Preis-Datenarrays.

    :param data: List of close prices
    :param period: Lookback-Periode für RSI
    :return: RSI-Wert als float
    """
    if len(data) < period:
        return None

    df = pd.DataFrame(data, columns=["timestamp", "open", "high", "low", "close", "volume"])
    close = df["close"]

    delta = close.diff()
    gain = delta.clip(lower=0)
    loss = -1 * delta.clip(upper=0)

    avg_gain = gain.rolling(window=period).mean()
    avg_loss = loss.rolling(window=period).mean()

    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))

    return round(rsi.iloc[-1], 2)
