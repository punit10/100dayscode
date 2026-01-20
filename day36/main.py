import os
import requests
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API = os.environ.get("STOCK_KEY")

STOCK_KEY = os.environ.get("STOCK_KEY")
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_KEY,
}

## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
response = requests.get(STOCK_ENDPOINT, params=stock_params, verify=False)
response.raise_for_status()
stock_data = response.json()
# print(stock_data["Time Series (Daily)"])
stock_list = [value for (key, value) in stock_data["Time Series (Daily)"].items()]
# print(stock_list)
yesterday_closing = stock_list[0]["4. close"]

#TODO 2. - Get the day before yesterday's closing stock price
before_yesterday_closing = stock_list[1]["4. close"]

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
diff = abs(float(yesterday_closing) - float(before_yesterday_closing))
print(diff)

#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
percent_diff = diff * 100 / float(before_yesterday_closing)
print(round(percent_diff, 2))

#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
if diff > 1:
    print("Get News")
    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
news_params = {
    "q": COMPANY_NAME,
    "from": "2026-01-19",
    "to": "2026-01-16",
    "sortBy": "popularity",
    "apiKey": NEWS_API
}
response = requests.get(NEWS_ENDPOINT, params=news_params, verify=False)
response.raise_for_status()
news_data = response.json()

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
news_articles = news_data["articles"][0:3]
# print(f"Headline: {news_articles[0]["title"]} \n"
#       f"Brief: {news_articles[0]["description"]} \n"
#       f"Read More at {news_articles[0]["url"]}")


## STEP 3: Use twilio.com/docs/sms/quickstart/python
#to send a separate message with each article's title and description to your phone number.

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.
top_three = [f"Headline: {item["title"]} \n"
      f"Brief: {item["description"]} \n"
      f"Read More at {item["url"]}" for item in news_articles]
print(top_three)

#TODO 9. - Send each article as a separate message via Twilio. 



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

