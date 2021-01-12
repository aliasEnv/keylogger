import datetime as dt
import time
import smtplib
from email.message import EmailMessage


FROM_EMAIL = 'enter_email_here'
TO_EMAIL = 'enter_email_here'
USERNAME = 'enter_email_here'
PASSWORD = 'enter_email_password_here'
filename = 'logger.txt'

def send_email():
    #email formatting + attaching log file
    msg = EmailMessage()
    msg["From"] = FROM_EMAIL
    msg["Subject"] = "Subject"
    msg["To"] = TO_EMAIL
    msg.set_content("This is the message body")
    msg.add_attachment(open(filename, "r").read(), filename="logger.txt")

    #connection to gmail provider
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(USERNAME, PASSWORD)
    s.send_message(msg)

    #sending the email
def send_email_at(send_time):
    time.sleep(10) #interval of how often to send an email in seconds
    send_email()
    print('email sent')

first_email_time = dt.datetime.now() 


send_time = first_email_time
while True:
    send_email_at(send_time)
    send_time = send_time