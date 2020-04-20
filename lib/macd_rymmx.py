from lib.ema import ema
import pandas as pd


def macd(df=pd.DataFrame()):
    """MACD"""

    df['ema12'] = ema(close=df['close'], length=12, offset=None)
    df['ema26'] = ema(close=df['close'], length=26, offset=None)

    # MACD
    df['DIF'] = df['ema12'] - df['ema26']
    df['DEA'] = df['DIF'].rolling(9).mean()
    df['BAR'] = (df['DIF'] - df['DEA']) * 2

    # MACD_judgment
    # for i in df.iterrows():
    #     df['MACD_judgment'] = 1 if (i['DIF'] - i['DEA']) > 0 else 0

    return df
