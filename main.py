import requests
from news import *
from stock import *
from twilio.rest import Client
import os

"""News_completed is the new formatted from news.py file"""


account_sid = os.environ.get("account_sid")
auth_token = os.environ.get("auth_token")

client = Client(account_sid,auth_token)


if percent_check:
    message = client.messages.create(
        body=f"{STOCK_NAME} {up_down} {diff_percent}%\n {news_completed}",
        from_='+17278003537',
        to='+541168251975'
    )









#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

