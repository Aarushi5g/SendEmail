import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

users_email = input("Enter your mail: ")
password = input("Enter your password: ")
receivers_email = input("Mail to? ")

subject = input("Enter the subject of the mail: ")

msg = MIMEMultipart()
msg['From'] = users_email
msg['To'] = receivers_email
msg['Subject'] = subject

body = input("Enter the body of the mail: ")
msg.attach(MIMEText(body, 'plain'))

text = msg.as_string()
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(users_email, password)


server.sendmail(users_email, receivers_email, text)
server.quit()
print(f"Sent a mail to {receivers_email}")