import requests
import datetime as dt


now = dt.datetime.now()
year = now.year
month = now.month
day = now.day

"""Day - 1 to show the yesterday news before closing the market"""
today = f"{year}-{month}-{day - 1}"

#NEWS WEB
COMPANY_NAME = "Tesla Inc"

NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEW_API = "1fd5c5101e3845f583bd20bff555aac4"


news_params = {
    "q": COMPANY_NAME,
    "from": today,
    "sortBy": "popularity",
    "apiKey": NEW_API
}

news_response = requests.get(NEWS_ENDPOINT, params=news_params)
news_data = news_response.json()


most_popular_new = news_data["articles"][0]

news_title = most_popular_new["title"]
news_content = most_popular_new["content"]
news_url = most_popular_new["url"]

news_completed = f"Title:{news_title},\nContent:{news_content},\nPage: {news_url}"





    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number.

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

#TODO 9. - Send each article as a separate message via Twilio.