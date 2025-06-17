from imap_tools import MailBox, AND
from datetime import datetime, timedelta, time



mail_password = "frra xzja ablq cehs"
mail_username = "jaspermusters@gmail.com"
mail_server = "imap.gmail.com"

def get_mailbox(username,password,server,inbox="INBOX"):
    mailbox = MailBox(server)
    mailbox.login(username,password,inbox)
    return mailbox


start = datetime.combine(datetime(2025, 6, 17), time.min)  # 2025-06-17 00:00:00
end = datetime.combine(datetime(2025, 6, 18), time.min)


def fetch_email(mailbox,start_date,end_date,labels=None,only_unread=False):

    if isinstance(start_date, str):
        start_date = datetime.strptime(start_date, "%d-%m-%Y").date()
    if isinstance(end_date, str):
        end_date = datetime.strptime(end_date, "%d-%m-%Y").date()

    criteria = AND(
        date_gte=start_date,
        date_lt=end_date,
        gmail_label=labels,
        seen=only_unread
    )
    retrieved_mail = []
    for msg in mailbox.fetch(criteria, reverse=True):
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

    return retrieved_mail

mailbox = get_mailbox(mail_username, mail_password, mail_server)

print(fetch_email(
    mailbox,
    "17-06-2025",
    "18-06-2025",
    ["important","subs/ai"],
    False
)   )



