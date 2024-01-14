import streamlit as st
import requests

COMMON_API_KEY = "I8GG1KUF0VM2WW45"

def get_gold_rate():
    gold_api_url = f"https://www.goodreturns.in/gold-rates/hyderabad.html=business&apiKey={COMMON_API_KEY}"
    response = requests.get(gold_api_url)
    gold_data = response.json()
    return gold_data.get('rate', "N/A")

def get_currency_exchange_rate(base_currency, target_currency):
    currency_api_url = f"https://www.oanda.com/currency-converter/en/?from=EUR&to=USD&amount=1={base_currency}&target={target_currency}&apiKey={COMMON_API_KEY}"
    response = requests.get(currency_api_url)
    exchange_data = response.json()
    return exchange_data.get('rate', "N/A")

# Streamlit App
st.title("Financial Insights App")

# Gold Rate
gold_rate = get_gold_rate()
st.write(f"Latest Gold Rate: {gold_rate} USD per ounce")

# Currency Exchange Rate
base_currency = st.selectbox("Select Base Currency:", ["USD", "EUR", "GBP", "INR"])
target_currency = st.selectbox("Select Target Currency:", ["USD", "EUR", "GBP", "INR"])
exchange_rate = get_currency_exchange_rate(base_currency, target_currency)
st.write(f"Exchange Rate ({base_currency} to {target_currency}): {exchange_rate}")

# Additional Financial Insights
st.header("Additional Financial Insights")

# Add more insights here based on your requirements
# For example, you can include stock market data, cryptocurrency rates, economic indicators, etc.

# For demonstration purposes, let's show a placeholder additional insight
st.write("Placeholder Additional Insight: This could be stock market data, cryptocurrency rates, economic indicators, etc.")

# You can continue to add more financial insights based on your application's scope

