import requests

STOCK_NAME = "TSLA"


STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_API_KEY = "K6YF6TOKZDBACI6R"

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    # "interval": "30min",
    "outputsize": "compact",
    "apikey": STOCK_API_KEY

}

response = requests.get(STOCK_ENDPOINT,params=stock_params)
data_stock = response.json()


new_dict = data_stock["Time Series (Daily)"]

new_list = [(key,value) for (key, value) in new_dict.items()]


yesterday_closed = float(new_list[0][1]["4. close"])
day_before_yesterday_closed = float(new_list[1][1]["4. close"])


difference = yesterday_closed - day_before_yesterday_closed

up_down = None

if difference > 0:
    up_down = "🔼"
else:
    up_down = "🔽"

diff_percent = round((difference / yesterday_closed) * 100,2)

def percent_check():
    if abs(diff_percent) > 5:
      return True





    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]

#TODO 2. - Get the day before yesterday's closing stock price

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp

#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.

#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").