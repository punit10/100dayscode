##################### Hard Starting Project ######################
import datetime as dt
import pandas
import random
import smtplib

my_email = "vectorcampus1@gmail.com"
password = input("Input details for sender email:")
birthday_df = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in birthday_df.iterrows()}

now = dt.datetime.now()
if (now.month, now.day) in birthdays_dict:
    birthday_name = birthdays_dict[(now.month, now.day)]
    letter_choice = random.randint(1, 3)
    file_path = f"./letter_templates/letter_{letter_choice}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        personalized_letter = contents.replace("[NAME]", birthday_name["name"])
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=birthday_name["email"],
            msg=f"Subject: Happy Birthday!! \n\n {personalized_letter}"
        )