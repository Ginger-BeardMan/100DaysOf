import smtplib
import datetime as dt
import random

with open('quotes.txt') as ins_quotes:
    quotes = [quote for quote in ins_quotes]

now = dt.datetime.now()

day_of_week = now.weekday() #starts at monday and counts from 0 - 6
# date_of_birth = dt.datetime(year=1984, month=12, day=15)

my_email = 'bungus8484@gmail.com'
password = 'abcd1234()'

if day_of_week == 2:

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs='chungus8484@gmail.com',
        msg=f'Subject:Inspiration\n\n{random.choice(quotes)}')
