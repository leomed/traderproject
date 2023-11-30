import requests
from news import *
from stock import *
from twilio.rest import Client

"""News_completed is the new formatted from news.py file"""


account_sid = 'AC67cac865522cd16c383d7fa85e635f26'
auth_token = '3037426c28f396a82f218d04b56ebfe0'

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

