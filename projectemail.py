#Zullinira Dwi Utami
#sumber :pythonindo.com

import smtplib
import getpass

#server = smtplib.SMTP('smtp.gmail.com:587')#definisi sever
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

#list untuk penerima
receiver_list=[]

fromaddr = input("Masukkan alamat email Anda = ")
passwordanda = getpass.getpass(prompt='Masukkan password email anda=')
toaddr = input ("Masukkan alamat email tujuan anda =")
receiver_list.append(toaddr)

#membuat file penerima
penerima = open("Receiver__list.txt","w")
penerima.write("\n Daftar e-mail penerima =" + toaddr)
penerima.close()

#membuat subject dan isi pada pyhton
subjek=input("Masukkan subject e-mail=")


msg = MIMEMultipart ()

msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject']= subjek

#tanya=input("Apakah ")
def cumaisi():
    isi = input("Masukkan isi e-mail =")
    body = isi
    msg.attach(MIMEText(body, 'plain'))

    print("--- Email berhasil dikirimkan---")


def lampiran():
    filename = "CV Nira2.pdf" #contoh file yang akan dilampirkan
    attachment = open ("D:\Magister ITB\CV\CV Nira2.pdf","rb") #path lokasi file

    part = MIMEBase('application','octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('content-Disposition', "attachment; filename=%s" %filename)

    msg.attach(part)


def selesai():
    print("program selesai, sampai jumpa!")
    exit(menu)

def menu():
    print("-----Menu Pengiriman E-mail-----")
    print("\n 1.Hanya isi tanpa lampiran \n 2.Isi dan lampiran \n 3.Keluar")
    angka=int(input("Pilih menu="))
    if angka==1:
        cumaisi()
    elif angka==2:
        cumaisi()
        lampiran()
    elif angka==3:
        selesai()
    else:
        print("Menu tidak tersedia")

menu()

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, passwordanda )
text =msg.as_string()
server.sendmail(fromaddr,toaddr,text)
server.quit()

