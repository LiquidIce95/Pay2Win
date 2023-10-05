import os
from twilio.rest import Client

account_sid = "youraccountsidhere"
auth_token = "yourauthtokenhere"

client = Client(account_sid, auth_token)
k = 0
#client.messages.create(to="+00000", from_="+12058783722", body="******Pay2Win********")
for sms in client.messages.list():
    print(sms.to)
    print(sms.from_)
    print(sms.body)
    print(sms.date_sent)
    print(sms)
    k= k+1
    print(k)
    print('***********************************************')
