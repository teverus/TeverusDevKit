import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from time import sleep


def send_email(recipient_email, subject, email_body):
    """
    A simple way to send an email. 
    email_body can take HTML tags.
    """
    # Constants
    SENDER_EMAIL = "TeverusAutomation@gmail.com"
    SENDER_PASSWORD = "HailSatan666"

    # To, From, Subject info
    message = MIMEMultipart()
    message['To'] = recipient_email
    message['From'] = SENDER_EMAIL
    message['Subject'] = subject

    # Attaching email.body
    message.attach(MIMEText(email_body, "html"))

    # Sending an email
    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.starttls()
    session.login(SENDER_EMAIL, SENDER_PASSWORD)
    session.sendmail(SENDER_EMAIL, recipient_email, message.as_string())
    session.quit()

    # Sleeping so that Gmail servers wouldn't think we are spamming if we send many emails in a row
    sleep(4)
