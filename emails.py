import smtplib
from dotenv import load_dotenv
import os

load_dotenv()

sender_email = os.getenv("EMAIL")
sender_email_pass = os.getenv("EMAIL_PASS")
test_email = os.getenv("TEST_EMAIL")

# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS for security
s.starttls()

# Authentication
s.login(sender_email, sender_email_pass)

# message to be sent
message = "Message_you_need_to_send"

# sending the mail
s.sendmail(sender_email, test_email, message)

# terminating the session
s.quit()