import smtplib
senders_address = "test@domain.com"
receivers_address = "address@domain.com"
message = (f"From: {senders_address}\n"
           f"To: {receivers_address}\n"
           f"Subject: SMTP e-mail test\n"
           f"\n"
           f"This is a test e-mail message.\n")
mail = smtplib.SMTP("smtp.gmail.com", 587)
mail.ehlo()  # command to SMTP server to identify itself (just like saying hello)
mail.starttls()   # start transfer layer security
# The above command helps secure the below login details
mail.login(senders_address, "password")
mail.sendmail(senders_address, receivers_address, message)
print(f"Successfully sent email to {receivers_address}")
mail.close()
