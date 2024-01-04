# Inisialisasi data buku dan status peminjaman
buku = {
    "B01": "Biologi",
    "B02": "Pai",
    "B03": "Ips",
    "B04": "Matematika",
    "B05": "Ipa",
}
status_peminjaman = {}


# Fungsi untuk menampilkan daftar buku yang tersedia
def tampilkan_daftar_buku():
    print("Daftar Buku Tersedia:")
    for kode, judul in buku.items():
        if kode not in status_peminjaman:
            print(f"{kode}: {judul}")


# Fungsi untuk input buku oleh admin
def input_buku(admin):
    if admin:
        kode = input("Masukkan kode buku: ")
        judul = input("Masukkan judul buku: ")
        buku[kode] = judul
        print("Buku berhasil ditambahkan.")
    else:
        print("Hanya admin yang dapat menambahkan buku.")


# Fungsi untuk melakukan peminjaman buku oleh user
def pinjam_buku(user):
    if not user:
        print("Hanya user yang dapat melakukan peminjaman buku.")
        return

    tampilkan_daftar_buku()
    kode_buku = input("Masukkan kode buku yang ingin dipinjam: ")

    if kode_buku in buku and kode_buku not in status_peminjaman:
        user_id = input("Masukkan ID pengguna: ")
        status_peminjaman[kode_buku] = user_id
        print("Buku berhasil dipinjam.")
    else:
        print("Buku tidak tersedia atau sudah dipinjam.")


# Fungsi untuk mengembalikan buku oleh user
def kembalikan_buku(user):
    if not user:
        print("Hanya user yang dapat mengembalikan buku.")
        return

    tampilkan_daftar_buku()
    kode_buku = input("Masukkan kode buku yang ingin dikembalikan: ")

    if kode_buku in status_peminjaman:
        user_id = input("Masukkan ID pengguna: ")
        if status_peminjaman[kode_buku] == user_id:
            del status_peminjaman[kode_buku]
            print("Buku berhasil dikembalikan.")
        else:
            print("Anda tidak dapat mengembalikan buku ini.")
    else:
        print("Buku tidak valid atau belum dipinjam.")


# Fungsi utama
def main():
    admin = False
    user = False

    while True:
        print("\nMenu:")
        print("1. Login sebagai admin")
        print("2. Login sebagai user")
        print("3. Keluar")
        pilihan = input("Masukkan pilihan: ")

        if pilihan == "1":
            admin = True
            user = False
            print("Admin login berhasil.")
        elif pilihan == "2":
            admin = False
            user = True
            print("User login berhasil.")
        elif pilihan == "3":
            break
        else:
            print("Pilihan tidak valid.")

        while admin or user:
            print("\nAksi yang tersedia:")
            print("1. Tampilkan daftar buku")
            print("2. Input buku")
            print("3. Pinjam buku")
            print("4. Kembalikan buku")
            print("5. Logout")
            aksi = input("Pilih aksi: ")

            if aksi == "1":
                tampilkan_daftar_buku()
            elif aksi == "2":
                input_buku(admin)
            elif aksi == "3":
                pinjam_buku(user)
            elif aksi == "4":
                kembalikan_buku(user)
            elif aksi == "5":
                admin = False
                user = False
                print("Logout berhasil.")
                break
            else:
                print("Aksi tidak valid.")


if __name__ == "__main__":
    main()
