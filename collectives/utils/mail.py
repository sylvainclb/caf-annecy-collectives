import smtplib
from flask import current_app
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from sys import stderr

# To use it:
# send_mail(subject="test", email="user@example.org", message="TEST")
def send_mail(**kwargs):
    config = current_app.config
    s = smtplib.SMTP(host=config['SMTP_HOST'], port=config['SMTP_PORT'])

    s.starttls()
    s.login(config['SMTP_ADDRESS'], config['SMTP_PASSWORD'])
    
    msg = MIMEMultipart()

    msg['From']=config['SMTP_ADDRESS']
    msg['To']=kwargs['email']
    msg['Subject']=kwargs['subject']

    msg.attach(MIMEText(kwargs['message'], 'plain'))

    s.send_message(msg)