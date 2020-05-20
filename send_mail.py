import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

users_email = 'address@gmail.com'
receivers_email = 'email@gmail.com'

subject = 'subject'

msg = MIMEMultipart()
msg['From'] = users_email
msg['To'] = receivers_email
msg['Subject'] = subject

body = 'Hi there, sending this email from Python!'
msg.attach(MIMEText(body, 'plain'))
text = msg.as_string()

mail = smtplib.SMTP('smtp.gmail.com', 587)
mail.starttls()
mail.login(users_email, "password")
mail.sendmail(users_email, receivers_email, text)
mail.quit()
print(f"Sent a mail to {receivers_email}")