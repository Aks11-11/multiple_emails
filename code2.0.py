import smtplib as s

ob = s.SMTP("smtp.gmail.com",587,25)
ob.ehlo()
ob.starttls()
ob.login('akshatvashishtt@gmail.com','+++++++')
subject = "Daily reminder"
body = "Hello, How are you Akshat. If you read this, the python code is successful"
message = "subject: {}\n\n{}".format(subject, body)  # Corrected formatting here
listadd = ["aksshatvashisht@gmail.com", 'akshatvashisht1101@gmail.com']
ob.sendmail('akshatvashishtt@gmail.com', listadd, message)
print("mail sent")
ob.quit()
