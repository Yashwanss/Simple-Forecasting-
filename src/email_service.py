import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from src.config import Config

def send_email(subject, body):
    msg = MIMEMultipart()
    msg['From'] = Config.SMTP_USERNAME
    msg['To'] = Config.EMAIL_RECEIVER
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'hello '))
    try:
        with smtplib.SMTP(Config.SMTP_SERVER, Config.SMTP_PORT) as server:
            server.starttls()
            server.login(Config.SMTP_USERNAME, Config.SMTP_PASSWORD)
            server.send_message(msg)
            print('E-mail sent')
    except Exception as e:
        print(e)