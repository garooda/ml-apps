import yfinance as yf
import pandas as pd 
import streamlit as st


st.write("""
# Stock Price App

Shown are the closing price and volume of the Google

"""
)

tickerSymbol = "GOOGL"

tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(period='1d', start='2015-5-31', end='2020-5-31')

st.write("""

#### Google Stock Price

""")

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)


tickerSymbol2 = "AAPL"

tickerDataApp  = yf.Ticker(tickerSymbol2)

tickerDf2 = tickerDataApp.history(period='1d', start='2015-5-31', end='2020-5-31')

st.write("""

#### Apple Stock Price

""")


st.line_chart(tickerDf2.Close)
st.line_chart(tickerDf2.Volume)
