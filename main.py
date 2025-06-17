from auth import get_mailbox
from fetcher import fetch_email

from dotenv import load_dotenv
import os

load_dotenv()  # Laadt alle variabelen uit .env

mail_username = os.getenv("MAIL_USERNAME")
mail_password = os.getenv("MAIL_PASSWORD")
mail_server = os.getenv("MAIL_SERVER")


mailbox = get_mailbox(mail_username, mail_password, mail_server)

