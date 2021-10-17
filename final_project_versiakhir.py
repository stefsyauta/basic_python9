#source terinspirasi dari https://github.com/nikeaprh/Basic_Python9/blob/master/Final-Project/final_project.py


import smtplib
import getpass

gmail_user = input(str("Masukkan alamat gmail Anda: "))
gmail_app_password = getpass.getpass("Masukkan password gmail Anda: ")

with open('receiver_list.txt', 'r') as filex:
    listpenerima = filex.read()
    penerima = listpenerima.split("\n")

for i in range(len(penerima)): 
    sent_to = penerima[i]
        
sent_from = gmail_user
sent_to = penerima
sent_subject = input(str("Masukkan subjek email: "))
sent_body = input(str("Masukkan pesan: "))

email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(sent_to), sent_subject, sent_body)

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_app_password)
    server.sendmail(sent_from, sent_to, email_text)
    server.close()

    print('Email terkirim!')
except Exception as exception:
    print("Error: %s!\n\n" % exception)

