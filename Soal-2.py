#Zullinira Dwi Utami

#mencari luas lingkaran
#inisiasi
pi=22/7

#inputan
r=input("Masukkan jari-jari lingkaran =")
s=float(r)

#rumusan luas lingkaran
l= pi*(s*s)

#2 angka dibelakang koma
l2="{:.2f}".format(l)

#output
print("Luas lingkaran dengan jari-jari " , s ,"cm adalah ", l2 ,"cm\u00b2")

