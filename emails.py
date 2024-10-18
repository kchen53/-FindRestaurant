import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
import os
import recipes

load_dotenv()

def email():

    sender_email = os.getenv("EMAIL")
    sender_email_pass = os.getenv("EMAIL_PASS")
    test_email = os.getenv("TEST_EMAIL")

    msg = EmailMessage()
    msg['Subject'] = 'Stir or Dine'
    msg['From'] = sender_email
    msg['To'] = test_email

    reci = recipes.find_recipes("pizza")

    list_items = ''.join(f'<li>{r}</li>' for r in reci)

    msg.set_content(f"""
        <!DOCTYPE html>
        <html>
        <head>
            <link rel="stylesheet" type="text/css" hs-webfonts="true" href="https://fonts.googleapis.com/css?family=Lato|Lato:i,b,bi">
            <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <style type="text/css">
            h1{{font-size:56px}}
            h2{{font-size:28px;font-weight:900}}
            p{{font-weight:100}}
            td{{vertical-align:top}}
            #email{{margin:auto;width:600px;background-color:#fff}}
            </style>
        </head>
        <body bgcolor="#F5F8FA" style="width: 100%; font-family:Lato, sans-serif; font-size:18px;">
        <div id="email">
            <table role="presentation" width="100%">
                <tr>
                    <td bgcolor="#00A4BD" align="center" style="color: white;">
                        <h1>Dine or Stir</h1>
                    </td>
            </table>
            <table role="presentation" border="0" cellpadding="0" cellspacing="10px" style="padding: 30px 30px 30px 60px;">
                <tr>
                    <td>
                        <h2>Here are some options: </h2>
                        <ul>
                            {list_items}
                        <ul>
                    </td>
                </tr>
            </table>
        </div>
        </body>
        </html>
    """, subtype='html')

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(sender_email, sender_email_pass)
        smtp.send_message(msg)

email()