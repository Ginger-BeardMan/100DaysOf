import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STK_API_KEY = # ADD KEY
NWS_API_KEY = # ADD KEY
account_sid = ''
auth_token = ''


# ------------------------------------ API ------------------------------------
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

stocks_url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK}&interval=5min&apikey={STK_API_KEY}'
stocks_r = requests.get(stocks_url, headers={'Authorization': STK_API_KEY})
stocks_data = stocks_r.json()['Time Series (Daily)']


# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

news_url = f'https://newsapi.org/v2/everything?q={COMPANY_NAME}&apiKey={NWS_API_KEY}'
news_r = requests.get(news_url, headers={'Authorization': NWS_API_KEY})
news_data = news_r.json()


# ------------------------------ FUNCTION & CALL ------------------------------


def compare_stocks():
    daily_prices = [value for (key, value) in stocks_data.items()]

    yesterday_price = float(daily_prices[0]['4. close'])

    day_before_price = float(daily_prices[1]['4. close'])

    percent_change = round((yesterday_price - day_before_price) * 100 / yesterday_price, 2)

    article_one = f"Headline: {news_data['articles'][0]['title']}\n" \
                  f"Brief: {news_data['articles'][0]['description']}\n"

    article_two = f"Headline: {news_data['articles'][1]['title']}\n" \
                  f"Brief: {news_data['articles'][1]['description']}\n"

    article_three = f"Headline: {news_data['articles'][2]['title']}\n" \
                    f"Brief: {news_data['articles'][2]['description']}\n"

    if percent_change <= 5:

        text_message = (f"{COMPANY_NAME}: {percent_change}%\n"
                        f"{article_one}{article_two}{article_three}")

# Send a separate message with the percentage change and each article's title and description to your phone number.
        
        client = Client(account_sid, auth_token)
        message = client.messages.create(body=f"{text_message}", from='+18009995454', to='Your verified number')
        print(message.status)


compare_stocks()
