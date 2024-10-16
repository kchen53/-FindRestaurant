import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
import os

load_dotenv()

sender_email = os.getenv("EMAIL")
sender_email_pass = os.getenv("EMAIL_PASS")
test_email = os.getenv("TEST_EMAIL")

msg = EmailMessage()
msg['Subject'] = 'Stir or Dine'
msg['From'] = sender_email
msg['To'] = test_email

msg.set_content("Hello")

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(sender_email, sender_email_pass)
    smtp.send_message(msg)