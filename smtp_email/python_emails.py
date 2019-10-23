# sending emails with python
# using smtplib

import email, smtplib, ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


smtp_server = 'smtp.gmail.com'
port = 465

sender = input('Enter sender email here: ')
password = input('Enter your password here: ')
receiver = input('Enter recipient email here: ')

message = MIMEMultipart('alternative')
message['subject'] = 'Cookies!'
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

filename = input("Do you have a file attachment? Please type filename here: ")
if filename:
    with open(filename, 'rb') as attachment:
        part_a = MIMEBase('application', 'octet-stream')
        part_a.set_payload(attachment.read())
        encoders.encode_base64(part_a)
        part_a.add_header(
            'Content-Disposition',
            "attachment; filename = {}".format(filename),
        )
        message.attach(part_a)



message.attach(part1)
message.attach(part2)



context = ssl.create_default_context()

with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender, password)
    print('Login Successful!')
    # Send Email
    server.sendmail(sender, receiver, message.as_string())