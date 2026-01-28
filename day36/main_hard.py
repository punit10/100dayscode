import os
import requests
from twilio.rest import Client
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_KEY = os.environ.get("STOCK_KEY")
NEWS_API = os.environ.get("NEWS_API_KEY")
account_sid = os.environ.get("TWILIO_ACC_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_KEY,
}

response = requests.get(STOCK_ENDPOINT, params=stock_params, verify=False)
response.raise_for_status()
stock_data = response.json()
# print(stock_data["Time Series (Daily)"])
stock_list = [value for (key, value) in stock_data["Time Series (Daily)"].items()]
# print(stock_list)
yesterday_closing = stock_list[0]["4. close"]
before_yesterday_closing = stock_list[1]["4. close"]
diff = abs(float(yesterday_closing) - float(before_yesterday_closing))
print(diff)

percent_diff = diff * 100 / float(before_yesterday_closing)
percent_diff = round(percent_diff, 2)

def get_three_articles()-> list:
    news_params = {
        "q": COMPANY_NAME,
        "from": "2026-01-26",
        "to": "2026-01-25",
        "sortBy": "popularity",
        "apiKey": NEWS_API
    }
    response = requests.get(NEWS_ENDPOINT, params=news_params, verify=False)
    response.raise_for_status()
    news_data = response.json()
    news_articles = news_data["articles"][0:3]

    top_three = [f"{news_params["q"]}: {percent_diff}\n Headline: {item["title"]}\n"
                 f"Brief: {item["description"]} \n"
                 f"Read More at {item["url"]}\n\n" for item in news_articles]
    # print(top_three)
    return top_three


if percent_diff > 5:
    print("Get News")
    top_three_articles = get_three_articles()
    for article in top_three_articles:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body=f"{article}",
            from_="+15017122000",  # number you got in twilio
            to="+15558675310",  # The number registered with twilio
        )
        print(message.body)


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

