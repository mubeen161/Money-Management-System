import streamlit as st
import requests
from bs4 import BeautifulSoup

def get_live_stock_data(symbol):
    url = f'https://finance.yahoo.com/quote/{symbol}'
    
    # Send an HTTP request to the URL
    response = requests.get(url)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract the relevant information
        stock_price = soup.find('div', {'class': 'D(ib) Mend(20px)'}).find('span').text
        stock_name = soup.find('h1', {'class': 'D(ib)'}).text.strip()
        
        # Additional data
        previous_close = soup.find('td', {'data-test': 'OPEN-value'}).text
        day_range = soup.find('td', {'data-test': 'DAYS_RANGE-value'}).text
        market_cap = soup.find('td', {'data-test': 'MARKET_CAP-value'}).text
        
        return {
            "Stock Name": stock_name,
            "Stock Symbol": symbol,
            "Stock Price": stock_price,
            "Previous Close": previous_close,
            "Day Range": day_range,
            "Market Cap": market_cap
        }
    else:
        return {"error": f"Failed to retrieve data. Status Code: {response.status_code}"}

# Streamlit App
st.title("Live Stock Data App")

# User Input
symbol = st.text_input("Enter the stock symbol:")

if st.button("Get Live Stock Data"):
    # Fetch and display stock data
    stock_data = get_live_stock_data(symbol)
    
    if "error" in stock_data:
        st.error(stock_data["error"])
    else:
        st.success("Data retrieved successfully!")
        st.write(stock_data)
