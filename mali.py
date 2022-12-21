import os
import smtplib
import imghdr
from email.message import EmailMessage


#https://www.youtube.com/watch?v=JRCJ6RtE3xU

EMAIL_ADDRESS = os.environ.get('GMAIL')
EMAIL_PASS = os.environ.get('GmailPass')

EBRYAN = 'bryan.koch@gmx.ch'
EDAVE = 'david.sanchez@hotmail.ch'

contacts = [EBRYAN,EDAVE]

#version2
msg = EmailMessage()
msg['Subject'] = 'Algotest'
msg['From'] = EMAIL_ADDRESS
msg['To'] = contacts
msg.set_content('This message was generated from the IT department of Pay2Win')

with open('/media/Dave/Volume/Users/david/Desktop/Pay2Win/pcs/Lgoo.jpeg', 'rb') as f:
    file_data = f.read()
    file_type = imghdr.what(f.name)

msg.add_attachment(file_data, maintype='image', subtype=file_type)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    #only needed for SMTP class
    #smtp.ehlo()
    #smtp.starttls()
    #smtp.ehlo()
    smtp.login(EMAIL_ADDRESS, EMAIL_PASS)
    #subject = 'AlgoTest'
    #body = 'Diese Nachricht wurde von der Pay2Win EDV-Abteilung generiert'
    #version 1
    #msg = f'Subject: {subject}\n\n{body}'
    #smtp.sendmail(EMAIL_ADDRESS, EDAVE, msg)
    smtp.send_message(msg)
