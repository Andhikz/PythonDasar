class Contact:
    def __init__(self, nama,  nomor_telpon, email):
        self.nama = nama
        self.nomor_telpon = nomor_telpon
        self.email = email

    def tampilkan_info(self):
        print(f"Nama: {self.nama}")
        print(f"Nomor Telepon: {self.nomor_telpon}")
        print(f"Email: {self.email}")
        print()

class AddressBook:
    def __init__(self):
        self.daftar_kontak = []

    def tambah_kontak(self, kontak):
        self.daftar_kontak.append(kontak)

    def tampilan_semua_kontak(self):
        print("Daftar Kontak:")
        for kontak in self.daftar_kontak:
            kontak.tampilan_info()

if __name__ =="__main__":
    address_book = AddressBook()

    while True:
        print("Menu:")
        print("1. Tambah Kontak")
        print("2, Tampilkan semua kontak")
        print("3. Keluar")

        pilihan = input("Pilih menu (1/2/3): ")

        if pilihan == "1":
            nama = input("Nama: ")
            nomor_telepon = input("Nomor Telepon: ")
            email = input("Email: ")
            kontak_baru = Contact(nama, nomor_telepon, email)
            address_book.tambah_kontak(kontak_baru)
        elif pilihan == "2":
            address_book.tampilan_semua_kontak()
        elif pilihan == "3":
            break
        else:
            print("Pilihan tidak valid. Silahkan pilih menu yang benar.")