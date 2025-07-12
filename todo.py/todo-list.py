# fungsi menampilkan menu
def tampilkan_menu(): 
    print("\n=== TO-DO LIST ===")
    print("1. tambah tugas")
    print("2. lihat tugas")
    print("3. hapus tugas")
    print("4. keluar")

# fungsi untuk menambah tugas ke list
def tambah_tugas(tugas_list):
    tugas_baru = input("masukkan tugas baru: ")
    tugas_list.append(tugas_baru)
    print(" tugas berhasil ditambahkan")

# fungsi untuk menampilkan semua tugas
def lihat_tugas(tugas_list):
    if not tugas_list: 
        print("tidak ada tugas")
    else:
        print("\n daftar tugas")
        for index, tugas in enumerate(tugas_list, start=1):
            print(f"{index}. {tugas}")

# fungsi untuk menghapus tugas berdaasarkan nomor 
def hapus_tugas(tugas_list):
    lihat_tugas(tugas_list) 
    if not tugas_list:
        return
    try:
        nomor = int(input("masukkan nomor tugas yang ingin dihapus"))
        if 1 <= nomor <= len(tugas_list):
            tugas_terhapus = tugas_list.pop(nomor - 1)
            print(f" tugas '{tugas_terhapus}' telah dihapus.")
        else: 
            print("nomor tidak valid.")
    except ValueError:
        print(" harus angka ya!")
# fungsi utama untuk menjalankan program
def main():
    daftar_tugas = []
    while True:
        tampilkan_menu()
        pilihan = input("pilih menu (1-4): ")

        if pilihan == '1':
            tambah_tugas(daftar_tugas)
        elif pilihan == '2':
            lihat_tugas (daftar_tugas)
        elif pilihan == '3':
            hapus_tugas(daftar_tugas)
        elif pilihan == '4':
            print(" Terima kasih! sampai jumpa.")
            break
        else:
            print("pilihan tidak tersedia.")
        
# jalankan program
if __name__== "__main__":
    main()


                  
                