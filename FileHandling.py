#Zullinira Dwi Utami

#membuat file handling no telepon
file1=open("No_telepon.txt","w")
nama=input("Masukkan nama =")
file1.write("\n" + " Nama =" + nama)

no=input("Masukkan no telepon =")
file1.write("\n" + "No. Telepon =" + no)
file1.close()

file1=open("No_telepon.txt","r")
print(file1.read())
file1.close()