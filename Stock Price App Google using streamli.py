import yfinance as yf
import streamlit as st
import pandas as pd
st.write('''
# Simple Stock Price App

Shown are the stock **closing price** and ***volume*** of Google!




''')

# define the ticker symbol
ticker_symbol = 'GOOGL'

# get data on this ticker
tick_data = yf.Ticker(ticker_symbol)

# get the historical prices for this ticker
ticker_df = tick_data.history(period = '1d', start = '2010-5-31', end = '2020-5-31')

st.write("""
## Closing Price
""")
st.line_chart(ticker_df.Close)


st.write("""
## Volume Price
""")
st.line_chart(ticker_df.Volume)

#streamlit run myapp.py use this command in terminal to run app locally