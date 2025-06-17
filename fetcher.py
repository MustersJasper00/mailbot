from imap_tools import AND
from datetime import datetime

def fetch_email(mailbox, start_date, end_date, labels=None, only_unread=False):
    if isinstance(start_date, str):
        start_date = datetime.strptime(start_date, "%d-%m-%Y").date()
    if isinstance(end_date, str):
        end_date = datetime.strptime(end_date, "%d-%m-%Y").date()

    filters = {
        "date_gte": start_date,
        "date_lt": end_date,
        "gmail_label": labels
    }

    if only_unread:
        filters["seen"] = False

    criteria = AND(**filters)

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
