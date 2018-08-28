import smtplib                           
print ("E-mail i girin : ")
mail=smtplib.SMTP("smtp.gmail.com",587)
mail.ehlo()
mail.starttls()
mail.login("gonderen@gmail.com","gonderensifre")
mail.sendmail("gonderen@gmail.com","alan@gmail.com",mesaj)
