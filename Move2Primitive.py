import  os
import imaplib, getpass, re
pattern_uid = re.compile('\d+ \(UID (?P<uid>\d+)\)')
user = os.environ.get('GMAIL')
Pass = os.environ.get('GmailPass')


def connect(email):
    imap = imaplib.IMAP4_SSL("imap.gmail.com")
    password = Pass
    imap.login(user, password)
    return imap

def disconnect(imap):
    imap.logout()

def parse_uid(data):
    match = pattern_uid.match(data)
    return match.group('uid')

if __name__ == '__main__':
    imap = connect(user)
    imap.select(mailbox = 'Inbox', readonly = False)
    resp, items = imap.search(None, 'All')
    email_ids  = items[0].split()
    latest_email_id = email_ids[-1] # Assuming that you are moving the latest email.

    resp, data = imap.fetch(latest_email_id, "(UID)")
    msg_uid = parse_uid(data[0])

    result = imap.uid('COPY', msg_uid, 'Personal')

    if result[0] == 'OK':
        mov, data = imap.uid('STORE', msg_uid , '+FLAGS', '(\Deleted)')
        imap.expunge()

    disconnect(imap)