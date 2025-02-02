import requests

# Step 2: Define Constants
API_KEY = 'FNEL5EBKM4AQFBB6'  # Replace with your actual Alpha Vantage API key
BASE_URL = 'https://www.alphavantage.co/query'
SYMBOL = 'AAPL'  # Stock symbol to trade
TIME_INTERVAL = '1min'  # Time interval for the stock data
OUTPUTSIZE = 'compact'  # Use 'full' for more data

# Step 3: Fetch Stock Data
def fetch_stock_data(symbol):
    params = {
        'function': 'TIME_SERIES_INTRADAY',
        'symbol': symbol,
        'interval': TIME_INTERVAL,
        'apikey': API_KEY,
        'outputsize': OUTPUTSIZE
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    return data

# Step 4: Analyze Stock Data
def analyze_data(data):
    time_series_key = 'Time Series (' + TIME_INTERVAL + ')'
    
    if time_series_key not in data:
        print("Error: Invalid response from Alpha Vantage.")
        return None

    time_series = data[time_series_key]
    prices = [(timestamp, float(values['1. open'])) for timestamp, values in time_series.items()]
    
    # Calculate a simple moving average for the last 5 prices
    if len(prices) < 5:
        print("Not enough data to analyze.")
        return None
    
    average_price = sum(price[1] for price in prices[:5]) / 5  # Simple moving average
    current_price = prices[0][1]  # Current price
    return average_price, current_price

# Step 5: Trade Decision
def make_trade_decision(average_price, current_price):
    if current_price < average_price:
        return "Buy"
    elif current_price > average_price:
        return "Sell"
    else:
        return "Hold"

# Step 6: Execute Trading Orders (Placeholder)
def execute_trade(decision):
    print(f"Executing trade: {decision}")

# Main execution
if __name__ == "__main__":
    stock_data = fetch_stock_data(SYMBOL)
    analysis_result = analyze_data(stock_data)
    
    if analysis_result is not None:
        average_price, current_price = analysis_result
        print(f"Average Price: {average_price}, Current Price: {current_price}")
        trade_decision = make_trade_decision(average_price, current_price)
        execute_trade(trade_decision)
