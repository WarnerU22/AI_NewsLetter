import os
import smtplib
from dotenv import load_dotenv
from email.mime.text import MIMEText

load_dotenv()

EMAIL = os.getenv("EMAIL_ADDRESS")
PASSWORD = os.getenv("EMAIL_PASSWORD")

def send_email(to_email, subject, html_body):
    msg = MIMEText(html_body, 'html')
    msg['Subject'] = subject
    msg['From'] = EMAIL
    msg['To'] = to_email

    with smtplib.SMTP_SSL('smtp.zoho.com', 465) as server:  # Change if you're using Outlook/etc
        server.login(EMAIL, PASSWORD)
        server.send_message(msg)
