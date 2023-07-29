import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from alpha_vantage.timeseries import TimeSeries

api_key = 'CCN1N30ZCC7XBZIH'
ts = TimeSeries(key=api_key, output_format='pandas')

symbol = 'AAPL'
start = "2010-01-01"
end = "2020-12-31"

# variable unpacking, first value is used the rest is ingorned
# also getting all data
df , _ = ts.get_daily(symbol=symbol, outputsize='full')

# convert the index to datetime
df.index = pd.to_datetime(df.index)

df = df.sort_index(ascending=True)

# filter the data based of specified start and end times
df = df.loc[start:end]

# rename columns and sort by index
df = df.rename(columns={"1. open": "Open", "2. high": "High", "3. low": "Low", "4. close": "Close", "5. volume": "Volume"})


st.write(df.head())
