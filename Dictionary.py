#Dictionary tidak memiliki urutan
# changeble
#ditulis dengan curly barkets = kurung kurawal
#lisr ditulis dengan kurung siku
#punya keys dan value

#contoh
pelanggan = {
    "Nama" : "Nira",
    "Umur" : "18"
}

print("Nama: {}".format(pelanggan["Nama"]))


#code belum slesai

#contoh dictionary
#dictionary data tidak berurut
dictionary = {'makan, minum, pergi'} 
print(dictionary)

for i in dictionary: #jika angka bisa berurutan ke bawah tapi kalau kata masih kesamping
    print(i)

#dictionary changeable
#mengubah nilai
#dictionary["makan"]= makann
#print(dictionary)

#dictionary data tdk terurut, dapat diubah, dan memiliki index
dict = {"brand":"Ford","model":"Mustang","year":1964}
print(dict)

for x in dict:
    print(x)

#change value
dict["year"] = 2021
print(dict)

x = dict["year"]
print(x)