# -*- encoding: utf-8 -*-
import smtplib
import random
import collections

from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText


participantes = {
    'diogo':'',
    'nanda':'',
    'alice':'',
    'tico':'',
    'lorena':'',
    'kleyton':'',
    'pedro':'',
    'regina':'',
    'arthur':'',
    'duda':''
        }

for nome in participantes.keys():
    a = random.choice(participantes.keys())
    while (a == nome) or (a in participantes.values()):
            a = random.choice(participantes.keys())
    participantes[nome] = a

for a, b in sorted(participantes.items()):
    print("Participante: "+a+" Tirou: "+b)


fromaddr = "diogopython123@gmail.com"

for nome, sorteado in participantes.items():
    if nome == "diogo":
        toaddr = "diogoas.bsi@gmail.com"
    elif nome == "fernanda":
        toaddr = "diogoas.bsi@gmail.com"
    elif nome == "tico":
        toaddr = "diogoas.bsi@gmail.com"
    elif nome == "alice":
        toaddr = "diogoas.bsi@gmail.com"
    elif nome == "duda":
        toaddr = "diogoas.bsi@gmail.com"
    elif nome == "regina":
        toaddr = "diogoas.bsi@gmail.com"
    elif nome == "pedro":
        toaddr = "diogoas.bsi@gmail.com"
    elif nome == "lorena":
        toaddr = "diogoas.bsi@gmail.com"
    elif nome == "kleyton":
        toaddr = "diogoas.bsi@gmail.com"
    elif nome == "arthur":
        toaddr = "diogoas.bsi@gmail.com"
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Amigo Oculto de Natal"

    body = "Oi, "+nome.title()+" seu amigo oculto é: "+sorteado.title()+" Não conte para ninguem. Presentes de até R$100,00. Seja criativo!"
#    body = stri(body)
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "Ana2605!")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()
    #teste
