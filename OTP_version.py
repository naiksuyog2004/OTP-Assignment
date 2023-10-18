from twilio.rest import Client
import math
import smtplib
import random
import re

account_sid = "AC74d3234c1b27da3f53a19340e214c05f"
auth_token = "07124dff1c5ee5945fe0179b0adbaa5d"

input_no = '+14705162791'


def validate_mobile_no(mobile_no):
    return len(mobile_no) == 10 and mobile_no.isdigit()


def validate_email(email):
    validation_condition = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    if re.search(validation_condition, email):
        return True
    else:
        return False


def generate_otp():
    digits = "0123456789"
    length = len(digits)
    otp = ""

    for i in range(6):
        otp += digits[math.floor(random.random()*length)]

    return otp


def send_email(email, otp):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()  # transfer layer security
    server.login('naiksuyogsudhir@gmail.com', 'kajzazcwvvnbhgxg')
    message = 'Your 6 digit OTP is '+str(otp)
    server.sendmail('naiksuyogsudhir@gmail.com',
                    email, message)
    server.quit()


def send_otp_over_mobile(mobile_no, otp):
    client = Client(account_sid, auth_token)
    Message = client.messages.create(
        body="Your 6 digit OTP is "+otp,
        from_=input_no,
        to='+91'+str(mobile_no),
    )
    print(Message.body)


if __name__ == "__main__":

    otp = generate_otp()
    mobile_no = input("Enter the Mobile number:")
    if (validate_mobile_no(mobile_no)):
        send_otp_over_mobile(mobile_no, otp)
    else:
        print("Invalid Mobile no")

    email = input("Enter the Email:")
    if (validate_email(email)):
        send_email(email, otp)
    else:
        print("Invalid Email ")
