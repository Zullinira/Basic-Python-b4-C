f = open("file.txt","a")
a = input("Masukkan nama = ")
f.write(a+"\n")

b =input("Masukkan kontak =")
f.write(b+"\n")

f.close()

f = open("file.txt","r")

data = []
for x in f :
    data.append(x)
f.close()