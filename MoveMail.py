import  os
import imaplib, email
import ImapClientClass
#https://www.youtube.com/watch?v=e-OZeAHFpkw&t=616s
#https://stackoverflow.com/questions/25234862/how-to-copy-email-in-inbox-into-important-mailbox-with-imaplib

user = os.environ.get('GMAIL')
Pass = os.environ.get('GmailPass')

imap_url = 'imap.gmail.com'

con = imaplib.IMAP4_SSL(imap_url)
con.login(user, Pass)
con.select('Inbox')
typ, data = con.search(None, 'SUBJECT','CR' )
num = data[0].split()
i = 0
for item in num:
    i += 1
    print(item)
    typ, msg_dta = con.fetch(str(i),'(RFC822)')
    print(str(i))
    print(item[0])
    #if (i == 114):
        #con.copy(item, 'Personal')
        #con.delete(item)


