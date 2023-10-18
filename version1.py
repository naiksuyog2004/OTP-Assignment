import smtplib
from twilio.rest import Client
import math
import random

account_sid = "AC74d3234c1b27da3f53a19340e214c05f"
auth_token = "07124dff1c5ee5945fe0179b0adbaa5d"

inputNO = '+14705162791'
sendNo = '+917666143540'
# send to sms
client = Client(sms.account_sid, sms.auth_token)
data = "0123456789"
leng = len(data)
otp = ""

for i in range(6):
    otp += data[math.floor(random.random()*leng)]

message = client.messages.create(
    body="Your 6 digit OTP is "+otp,

    from_=sms.inputNO,
    to=sms.sendNo
)

print(message.body)
# send to email
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()  # transfer layer security
server.login('naiksuyogsudhir@gmail.com', 'kajzazcwvvnbhgxg')
msg = 'Your 6 digit OTP is '+str(otp)
server.sendmail('naiksuyogsudhir@gmail.com', 'naiksuyog2004@gmail.com', msg)
server.quit()
