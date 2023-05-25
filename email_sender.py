import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())

email = EmailMessage()
email['from'] = 'Arturo Macias'
email['to'] = 'johndoe@gmail.com'
email['subject'] = 'You have won $1,000,000,000,000!!!'

email.set_content(html.substitute(name= 'Panfilo'), 'html')

# with smtplib.SMTP_SSL('smtp.gmail.com', 465) as connection: # code from stackoverflow
#     email_address = 'johndoe@gmail.com'
#     email_password = 'nvvjzrqxakxgefdx'
#     connection.login(email_address, email_password )
#     connection.sendmail(from_addr=email_address, to_addrs='receiver_email@something.com',
#     msg="subject:hi \n\n this is my message")

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp: # code from ztm
    smtp.ehlo()
    smtp.starttls()
    smtp.login('johndoe@gmail.com', 'get app password')
    smtp.send_message(email)
