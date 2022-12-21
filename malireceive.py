import  os
import imaplib, email
#https://www.youtube.com/watch?v=e-OZeAHFpkw&t=616s
#https://www.devdungeon.com/content/read-and-send-email-python

user = os.environ.get('GMAIL')
Pass = os.environ.get('GmailPass')

imap_url = 'imap.gmail.com'

def get_body(msg):
    if msg.is_multipart():
        return get_body(msg.get_payload(0))
    else:
        return msg.get_payload(None, True)

def search(key,value,con):
    result, data = con.search(None,key,'"()"'.format(value))
    return data
def get_emails(result_bytes):
    msgs = []
    for num in result_bytes[0].split():
        typ, data = con.fetch(num, '(RFC822)')
        msgs.append(data)
    return msgs

con = imaplib.IMAP4_SSL(imap_url)
con.login(user, Pass)
print(con.list())
con.select('INBOX')

result, data = con.fetch(b'3','(RFC822)')

print(result)
print(data)
print()
#raw = email.message_from_bytes(data[0][1])
#print(get_body(raw))

print(con.list())
con.select('INBOX')
