data = open("data.txt","a")
print ("Hallo, selamat datang !")

nama = input("Masukkan nama =")
data.write(nama +"\n")

phone = input("Masukkan no Telepon =")
data.write(phone+"\n")

print("Data berhasil di tambahkan !")
data.close()

read = open("data.txt","r")
data = read.readlines()

for x in range(0,len(data),2):
    print("Nama\t\t: {}\nNo.Telepon\t: {}".format(data[x],data[x+1]))
read.close()
