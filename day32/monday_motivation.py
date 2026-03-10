import smtplib
import datetime as dt
import random

MY_EMAIL = "vectorcampus1@gmail.com"
MY_PASS = input("Enter details of sender email: ")

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 2:
    with open("quotes.txt") as quotes_file:
        all_quotes = quotes_file.readlines()
        quote = random.choice(all_quotes)
        # print(quote)
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASS)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg=f"Subject: Monday Motivation \n\n {quote}"
            )