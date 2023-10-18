import math
import random
import smtplib
from twilio.rest import Client
import sms


def Validate_MobileNo(MobileNo):
    if len(MobileNo) != 10:
        print("Please enter valid Mobile number!!")
        MobileNo = input("Enter the Mobile number:")
        Validate_MobileNo(MobileNo)
    return MobileNo


def Validate_Email(Email):
    if "@gmail.com" not in Email:
        print("Please Enter Valid Email address!!")
        Email = input("Enter the Email:")
        Validate_Email(Email)
    return Email


def Generate_OTP():
    digits = "0123456789"
    length = len(digits)
    otp = ""

    for i in range(6):
        otp += digits[math.floor(random.random()*length)]

    return otp


def send_email(Checked_email, OTP):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()  # transfer layer security
    server.login('naiksuyogsudhir@gmail.com', 'kajzazcwvvnbhgxg')
    message = 'Your 6 digit OTP is '+str(OTP)
    server.sendmail('naiksuyogsudhir@gmail.com',
                    Checked_email, message)
    server.quit()


def send_OTP(Checked_MobileNo, OTP):
    client = Client(sms.account_sid, sms.auth_token)
    Message = client.messages.create(
        body="Your 6 digit OTP is "+OTP,

        from_=sms.inputNO,
        to='+91'+str(Checked_MobileNo),
    )
    print(Message.body)


MobileNo = input("Enter the Mobile number:")
Checked_MobileNo = Validate_MobileNo(MobileNo)

Email = input("Enter the Email:")
Checked_email = Validate_Email(Email)

# will Generate OTP
OTP = Generate_OTP()

# send OTP to Number
send_OTP(Checked_MobileNo, OTP)

# send to email
send_email(Checked_email, OTP)
