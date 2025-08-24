# ===============================
# Program Pengelolaan Nilai Mahasiswa
# ===============================

# Dictionary untuk nyimpen data mahasiswa
# Format: {"nama": nilai}
data_mahasiswa = {}

def tambah_data():
    nama = input("Masukkan nama mahasiswa: ").strip()
    if not nama:
        print("Nama tidak boleh kosong!")
        return
    try:
        nilai = float(input("Masukkan nilai mahasiswa: "))
    except ValueError:
        print("Nilai harus berupa angka!")
        return
    data_mahasiswa[nama] = nilai
    print(f"Data {nama} berhasil ditambahkan!")

def lihat_data():
    if not data_mahasiswa:
        print("Data masih kosong!")
        return
    print("\n=== Daftar Nilai Mahasiswa ===")
    print("Nama\tNilai")
    print("-----------------------")
    for nama, nilai in data_mahasiswa.items():
        print(f"{nama}\t{nilai}")

def cari_data():
    nama = input("Masukkan nama mahasiswa yang dicari: ").strip()
    if nama in data_mahasiswa:
        print(f"{nama}: {data_mahasiswa[nama]}")
    else:
        print("Data tidak ditemukan!")

def update_nilai():
    nama = input("Masukkan nama mahasiswa yang ingin diupdate: ").strip()
    if nama not in data_mahasiswa:
        print("Data tidak ditemukan!")
        return
    try:
        nilai_baru = float(input("Masukkan nilai baru: "))
    except ValueError:
        print("Nilai harus berupa angka!")
        return
    data_mahasiswa[nama] = nilai_baru
    print(f"Data {nama} berhasil diupdate!")

def hapus_data():
    nama = input("Masukkan nama mahasiswa yang ingin dihapus: ").strip()
    if nama in data_mahasiswa:
        del data_mahasiswa[nama]
        print(f"Data {nama} berhasil dihapus!")
    else:
        print("Data tidak ditemukan!")

# Menu utama
while True:
    print("\n=== Sistem Nilai Mahasiswa ===")
    print("1. Tambah Data")
    print("2. Lihat Data")
    print("3. Cari Data")
    print("4. Update Nilai")
    print("5. Hapus Data")
    print("6. Keluar")

    pilihan = input("Pilih menu (1-6): ")

    if pilihan == "1":
        tambah_data()
    elif pilihan == "2":
        lihat_data()
    elif pilihan == "3":
        cari_data()
    elif pilihan == "4":
        update_nilai()
    elif pilihan == "5":
        hapus_data()
    elif pilihan == "6":
        print("Keluar dari program...")
        break
    else:
        print("Inputan tidak valid! Coba lagi.")
