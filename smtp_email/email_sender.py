import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text()) #wrap in Template object
email = EmailMessage()
email['from'] = 'XeroGravity'
email['to'] = 'tpierce65@gmail.com' 
email['subject'] = 'You are the man!'

email.set_content(html.substitute({'name': 'TinTin'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()     # Server awake and greeting
    smtp.starttls() # Secure, encrypted connection to server
    smtp.login('me@me.com', 'password')
    smtp.send_message(email)
    print("All Good Boss!")
