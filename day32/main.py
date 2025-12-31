import smtplib

my_email = "vectorcampus1@gmail.com"
password = input("Input details for sender email")

# connection = smtplib.SMTP("smtp.gmail.com", port=587)
# connection.starttls()
# connection.login(user=my_email, password=password)
# connection.sendmail(
#     from_addr=my_email,
#     to_addrs="punitvector@gmail.com",
#     msg="Subject: Test email \n\n This is test email body",
# )
# connection.close()

with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="punitvector@gmail.com",
        msg="Subject: Test email \n\n This is test email body"
    )
