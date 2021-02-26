#Zullinira Dwi Utami

#variabel global untuk menyimpan kontak

namakontak =[]
nokontak =[]

#fungsi untuk menampilkan daftar kontak
def daftar_kontak():
    if len(namakontak)<=0:
        print("Belum ada data kontak siapapun")
    else:
        #for jumlah in (namakontak):
            print("Nama = {}".format(namakontak))
            print("No Telepon = {}".format(nokontak))
        
#fungsi untuk menambahkan kontak
def tambah_kontak():
    nama_kontak=input("Masukkan nama kontak =")
    no_kontak = (input("Masukkan nomor hp ="))
    namakontak.append(nama_kontak)
    nokontak.append(no_kontak)
    print("Kontak berhasil ditambahkan")

def selesai():
    print("program selesai, sampai jumpa!")
    exit(menu)

#main
#kata sambutan
print(" Hallo selamat datang pada website nomor telepon !")
print("Silahkan pilih menu yang diinginkan dengan menekan nomor yang diinginkan :)")
print(" ")
print("---------------------------------------------------------------------------")

def menu ():
    print("==== Menu ====")
    print(" 1. Daftar Kontak \n 2. Tambah Kontak \n 3. Keluar")
    #input nomor yang diinginkan
    menu=int(input("Pilih menu ="))
    #print(menu)

    if menu==1:
        daftar_kontak()
    elif menu==2:
        tambah_kontak()
    elif menu==3:
        selesai()
    else :
        print("Menu tidak tersedia")
    
while(True):
    menu()