import smtplib

my_email = "vectorcampus1@gmail.com"
password = "preM@1001"
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="punitvector@gmail.com",
        msg="Subject: Test email \n\n This is test email body"
    )
