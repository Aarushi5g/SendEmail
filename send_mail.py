import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

users_email = 'domain@gmail.com'
receivers_email = 'email@gmail.com'

subject = 'subject'

msg = MIMEMultipart()
msg['From'] = users_email
msg['To'] = receivers_email
msg['Subject'] = subject

body = 'Hi there, sending this email from Python!'
msg.attach(MIMEText(body, 'plain'))

filename = 'file_path'
attachment = open(filename, 'rb')

part = MIMEBase('application','octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= "+filename)

msg.attach(part)
text = msg.as_string()
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(users_email, "password")


server.sendmail(users_email, receivers_email, text)
server.quit()
print(f"Sent a mail to {receivers_email}")