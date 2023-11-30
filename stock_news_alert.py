import requests

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STK_API_KEY = # ADD KEY
NWS_API_KEY = # ADD KEY


# ------------------------------------ API ------------------------------------
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

stocks_url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK}&interval=5min&apikey={STK_API_KEY}'
stocks_r = requests.get(stocks_url, headers={'Authorization': STK_API_KEY})
stocks_data = stocks_r.json()

daily_prices = []

# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

news_url = f'https://newsapi.org/v2/everything?q={COMPANY_NAME}&apiKey={NWS_API_KEY}'
news_r = requests.get(news_url, headers={'Authorization': NWS_API_KEY})
news_data = news_r.json()

print((daily_prices[0] - daily_prices[1]) * 100 / daily_prices[0])

# Send a separate message with the percentage change and each article's title and description to your phone number.



# ------------------------------ FUNCTION & CALL ------------------------------


def compare_stocks():
    for date in stocks_data['Time Series (Daily)']:
        daily_prices.append(float(stocks_data['Time Series (Daily)'][date]['4. close']))

    if (daily_prices[0] - daily_prices[1]) * 100 / daily_prices[0] >= 5:
        for article in range(3):
            print(f"Headline: {news_data['articles'][article]['title']}")
            print(f"Brief: {news_data['articles'][article]['description']}")


compare_stocks()


# STEP 3: Use https://www.twilio.com





# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file
by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the 
coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file
by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the 
coronavirus market crash.
"""

