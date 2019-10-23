import csv, smtplib, ssl

message = """\
From: {sender}
To: {email}
Subject: Your Grades

Hi {name} your grade is {grade}.
"""

sender = input("Enter sender email: ")
password = input("Enter sender password: ")

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context = context) as server:
    server.login(sender, password)
    with open('contacts.csv') as file:
        reader = csv.reader(file)
        next(reader)  # skip first (header) of csv file
        for name, email, grade in reader:
            server.sendmail(
                sender,
                email,
                message.format(
                    sender = sender,
                    email = email,
                    name = name,
                    grade = grade
                )
            )
