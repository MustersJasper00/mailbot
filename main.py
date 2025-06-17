from imap_tools import MailBox, AND
from datetime import datetime, timedelta, time

start = datetime.combine(datetime(2025, 6, 17), time.min)  # 2025-06-17 00:00:00
end = datetime.combine(datetime(2025, 6, 18), time.min)

mail_password = "frra xzja ablq cehs"
mail_username = "jaspermusters@gmail.com"
mail_server = "imap.gmail.com"

def get_mailbox(username,password,server,inbox="INBOX"):
    mailbox = MailBox(server)
    mailbox.login(username,passowrd,inbox)
    return mailbox


with MailBox(mail_server).login(mail_username, mail_password, "INBOX") as mb:
    criteria = AND(date_gte=start.date(), date_lt=end.date(), gmail_label=[])
    retrieved_mail = []
    for msg in mb.fetch(criteria, reverse=True):
        mail_data = {
            "uid": msg.uid,
            "subject": msg.subject,
            "from_": msg.from_,
            "to": msg.to,
            "cc": msg.cc,
            "date": msg.date,
            "body_plain": msg.text,
            "body_html": msg.html,
            "size": msg.size,
            "flags": msg.flags,
            "is_read": '\\Seen' in msg.flags,
            "attachments": msg.attachments,
            "thread_id": None,
            "raw": None
        }

        retrieved_mail.append(mail_data)


print(retrieved_mail)
