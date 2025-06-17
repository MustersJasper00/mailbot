from imap_tools import MailBox

def get_mailbox(username,password,server,inbox="INBOX"):
    mailbox = MailBox(server)
    mailbox.login(username,password,inbox)
    return mailbox




