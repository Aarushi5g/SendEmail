import smtplib
message = "So this is a test message"
mail = smtplib.SMTP("smtp.gmail.com", 587)
mail.ehlo()  # command to SMTP server to identify itself (just like saying hello)
mail.starttls()   # start transfer layer security
# The above command helps secure the below login details
mail.login("senders_address", "password")
mail.sendmail("senders_address", "receivers_address", message)
print ("Successfully sent email")
mail.close()