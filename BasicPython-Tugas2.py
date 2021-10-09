#Tugas-2
DataKontak = [];
DataNomor = [];

def show_menu():
    print ("\n")
    print ("Selamat Datang!")
    print ("--- Menu ---")
    print ("[1] Daftar Kontak")
    print ("[2] Tambah Kontak")
    print ("[3] Keluar")

    menu = int(input("Pilih menu:"))
    print ("\n")

    if menu==1:
        daftar_kontak()
    elif menu==2:
        tambah_kontak()
    elif menu==3:
       print ("Program selesai, sampai jumpa! ")
       exit ()
    else :
        print ("Menu tidak tersedia")
    return show_menu()

def daftar_kontak():
    if len(DataKontak) <= 0 :
        print ("Belum ada kontak")
    else :
        for Indeks in range(len(DataKontak)) :
            print(f"Nama: {DataKontak[Indeks]}")
            print(f"Nomor: {DataNomor[Indeks]}")
            print()

def tambah_kontak():
    data = input("Nama : ")
    nomor = int(input("No. Telepon: "))
    DataKontak.append(data)
    DataNomor.append(nomor)
    print("Kontak berhasil ditambahkan")
  
if __name__ == "__main__":
    show_menu()