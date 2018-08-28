import smtplib                           
print ("E-mail i girin : ")
mail=smtplib.SMTP("smtp.gmail.com",587)
mail.ehlo()
mail.starttls()
mail.login("metearduino@gmail.com","mete2002")
mail.sendmail("metearduino@gmail.com","meteeker2350@gmail.com",mesaj)
