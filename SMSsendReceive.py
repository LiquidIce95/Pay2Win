import os
from twilio.rest import Client

account_sid = "AC246050aa98ec9fe1de1a0f9bea7c5c42"
auth_token = "fa67cfde624ee75da423a370f945afe9"

client = Client(account_sid, auth_token)
k = 0
#client.messages.create(to="+41764409375", from_="+12058783722", body="******Pay2Win********")
for sms in client.messages.list():
    print(sms.to)
    print(sms.from_)
    print(sms.body)
    print(sms.date_sent)
    print(sms)
    k= k+1
    print(k)
    print('***********************************************')
