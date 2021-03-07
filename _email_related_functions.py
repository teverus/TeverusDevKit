import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from time import sleep


def send_email(recipient_email, subject, email_body):
    """
    A simple way to send an email.
    
    """
    SENDER_EMAIL = "TeverusAutomation@gmail.com"
    SENDER_PASSWORD = "HailSatan666"

    message = MIMEMultipart()
    message['To'] = recipient_email
    message['From'] = SENDER_EMAIL
    message['Subject'] = subject

    message.attach(MIMEText(email_body, "html"))

    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.starttls()
    session.login(SENDER_EMAIL, SENDER_PASSWORD)
    session.sendmail(SENDER_EMAIL, recipient_email, message.as_string())
    session.quit()

    sleep(4)
