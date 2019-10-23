# sending emails with python
# using smtplib

import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


smtp_server = 'smtp.gmail.com'
port = 465

sender = 'mailerpytester@gmail.com'
password = input('Enter your password here: ')
receiver = 'tpierce65@gmail.com'

message = MIMEMultipart('alternative')
message['subject'] = 'Multipart Test'
message['From'] = sender
message['To'] = receiver

text = """\
Hey! How are you?
Real Python has many great and awesome tutorials!
www.realpython.com
"""

html = """\
<html>
    <body>
        <p>Hi!<br>
            How are you?<br>
            <a href="http//www.realpython.com">Real Python!</a>
        </p>
    </body>
</html>
"""

part1 = MIMEText(text, 'plain')
part2 = MIMEText(html, 'html')

message.attach(part1)
message.attach(part2)


context = ssl.create_default_context()

with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender, password)
    print('Login Successful!')
    # Send Email
    server.sendmail(sender, receiver, message.as_string())