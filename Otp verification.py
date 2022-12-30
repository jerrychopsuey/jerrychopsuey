from email.message import EmailMessage
import math
import random
import smtplib
import ssl

email_sender = 'stardustmass73@gmail.com'
email_password = 'ylnuitzaktxgqqfi'
email_reciever = input("Enter your Email : ")

digits="0123456789"
OTP=""
for i in range(6):
    OTP+=digits[math.floor(random.random()*10)]
otp = OTP + " is your OTP"
subject = 'YOUR OTP : ' + OTP

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_reciever
em['Subject'] = subject
em.set_content(otp)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com',465, context = context) as smtp:
  smtp.login(email_sender ,email_password )
  smtp.sendmail(email_sender,email_reciever,em.as_string())

k = True
c = 0
while k == True:
    a = input("Enter Your OTP >>: ")
    if a == OTP:
        print("Verified")
        break
    else:
        print("Please Check your OTP again")
        c+=1
        if c == 3:
            k=False
            alert = "Error Entered Wrong Otp 3 times"
            print(alert)

            