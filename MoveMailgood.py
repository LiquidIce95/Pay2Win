import  os
import imaplib, email
from email.header import decode_header
#https://www.youtube.com/watch?v=e-OZeAHFpkw&t=616s
#https://stackoverflow.com/questions/25234862/how-to-copy-email-in-inbox-into-important-mailbox-with-imaplib

user = os.environ.get('GMAIL')
Pass = os.environ.get('GmailPass')

imap_url = 'imap.gmail.com'

con = imaplib.IMAP4_SSL(imap_url)
con.login(user, Pass)
con.select('Inbox')

con = imaplib.IMAP4_SSL(imap_url)
con.login(user, Pass)
con.select('Inbox')
typ, data = con.search(None, 'SUBJECT','CR' )

num = data[0].split()

for item in num:
    print(str(item))

status, messages = con.select('Inbox')

N = 10

messages = int(messages[0])

for i in range(messages, messages-N, -1):
    res, msg = con.fetch(str(i), '(RFC822)')
    for response in msg:
        if isinstance(response, tuple):
            # parse a bytes email into a message object
            msg = email.message_from_bytes(response[1])
            # decode the email subject
            subject = decode_header(msg["Subject"])[0][0]
            From = decode_header(msg["From"])[0][0]
            if isinstance(subject, bytes):
                # if it's a bytes, decode to str
                subject = subject.decode()
                From = From.decode()
            print('*******new messge**********')
            print(subject)
            print(From)
            if msg.is_multipart():
                #print('Multipart types:')
                #for part in msg.walk():
                    #print(f'- {part.get_content_type()}')
                multipart_payload = msg.get_payload()
                index = 0
                for sub_message in multipart_payload:
                    # The actual text/HTML email contents, or attachment data
                    if(index == 0):
                        print(f'Payload\n{sub_message.get_payload()}')

                    index = index+1
            else:  # Not a multipart message, payload is simple string
                print(f'Payload\n{msg.get_payload()}')