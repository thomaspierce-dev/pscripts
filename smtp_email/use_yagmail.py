# send emails with python
# using yagmail

import yagmail

#sender = ''
reciever = input("Sending email to? ")
subject = input('What is the subject of the email? ')
body = input('What is your message? ')
#filename = ''

yag = yagmail.SMTP("me@somewhere.com", oauth2_file="~/oauth2_creds.json")
yag.send(
    to = reciever,
    subject = subject,
    contents = body,
    #attachments = filename,
)