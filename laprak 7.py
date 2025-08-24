class DataPenduduk:
    def __init__ (self,nik, nama, jns_kelamin,alamat, tgl_lahir, tempat_lahir, RT,RW,
                   kelurahan, kec, agama, statusKawin,PendididkanTerakhir, pekerjaan,
                     kewarganegaraan):
        self.nik= nik
        self.nama=nama
        self.jns_kelamin=jns_kelamin
        self.tgl_lahir=tgl_lahir
        self.tempat_lahir=tempat_lahir
        self.RT= RT
        self.RW = RW
        self.kelurahan=kelurahan
        self.kec=kec
        self.agama=agama
        self.statusKawin=statusKawin
        self.PendididkanTerakhir=PendididkanTerakhir
        self.alamat=alamat
        self.pekerjaan=pekerjaan
        self.kewarganegaraan=kewarganegaraan
    def tampilkan_identitas(self):
        return(f"NIK: {self.nik}, NAMA: {self.nama}, GENDER: {self.jns_kelamin}")
    def Alamat_lengkap(self):
        return f"{self.alamat},RT {self.RT}/ RW {self.RW}, kel. {self.kelurahan}, kec. {self.kec}"
    def Usia(self, tahun_sekarang):
        tahun_lahir=int(self.tgl_lahir.split("-") [0])
        return tahun_sekarang - tahun_lahir
    def cek_status_perkawinan(self):
        if self.statusKawin.lower() == ("kawin"):
            return("sudah menikah")
        else: 
            return "belum menikah"
    def pekerjaan_sesuai_pendidikan(self):
        profesi= {
            "dokter" : "S2",
            "pengacara" : "S1",
            "karyawan": "SMA",
            "guru" : "S1",
            "tukang" : "SD"
        }

        pekerjaan = self.pekerjaan.lower()
        pendidikan = self.PendididkanTerakhir.upper()

        if pekerjaan in profesi:
            return pendidikan >= profesi[pekerjaan].upper()
        return False
    
    
    def info_agama(self):
        return(f"{self.nama} beragama {self.agama}")

    def is_warga_negara(self):
        if self.kewarganegaraan.lower() == "WNI":
            return True
        else:
            return False
    
        
    def ganti_alamat(self,alamat_baru, RT_baru, rw_baru,):
        self.alamat=alamat_baru
        self.RT= RT_baru
        self.RW = rw_baru
        return("alamat berhasil diperbaharui!")

    def update_pekerjaan(self, pekerjaan_baru):
        print (f"{self.nama} sekarang memiliki pekerjaan { self.pekerjaan}")

        self.pekerjaan=pekerjaan_baru
        return(f"{self.nama} berhasil mengganti pekerjaan menjadi {self.pekerjaan}!")


    def __str__(self):
        return(
            f"pendududk: {self.nik}\n"
            f"jenis kelamin: {self.jns_kelamin}\n"
            f"tempat/tgl lahir: {self.tempat_lahir} / {self.tgl_lahir}\n"
            f"alamat: {self.alamat}\n"
            f"agama: {self.agama}\n"
            f"status kawin: {self.statusKawin}\n"
            f"pendidikan: {self.PendididkanTerakhir}\n"
            f"pekerjaan: {self.pekerjaan}\n"
            f"kewarganegaraan:{self.kewarganegaraan}\n "
        )

# Buat objek penduduk
p1 = DataPenduduk(
    "123456789", "Kameria", "Laki-laki", 
    "Jl. Merdeka No.1", "1990-04-12", "Jakarta", 
    "01", "02", "Sukamaju", "Sukasari", "Islam",
    "Kawin", "S1", "pelajar", "WNI"
)

while True:
    print("\n===TAMPILKAN MENU (1/2/3/4/5)===",
          "\n1. tampilkan_identitas",
          "\n2. lamat_lengkap",
          "\n3. berapa usia sekarang ",
          "\n4. status kawin",
          "\n5. Pekerjaan sesuai pendidikan",
          "\n6. info_agama",
          "\n7. info_agama",
          "\n8. is_warga_negara ",
          "\n8. ganti_alamat"
          "\n9. update_pekerjaan",
          "\n10. Data Lengkap"
          )
    pilihan = input("pilih(1/2/3/4/5/6/7/8/9/10):\n")

    if pilihan == "1":
        print(p1.tampilkan_identitas())
    elif pilihan == "2":
        print(p1.Alamat_lengkap())
    elif pilihan == "3":
        print("Usia:", p1.Usia(2025))
    elif pilihan == "4":
        print("Status Kawin:", p1.cek_status_perkawinan())
    elif pilihan == "5":
        print("Pekerjaan sesuai pendidikan:", p1.pekerjaan_sesuai_pendidikan())
    elif pilihan == "6":
        print(p1.info_agama())
    elif pilihan == "7":
        print("WNI?", p1.is_warga_negara())
    elif pilihan == "8":
        print(p1.ganti_alamat("Jl. Baru No.2", "03", "04"))
    elif pilihan == "9":
        print(p1.update_pekerjaan(input("update pekerjaan:")))
    elif pilihan == "10":
        print("\n=== Data Lengkap ===")
        print(p1)
        break

    else:
       print(", data tidal valid")

'''
print(p1.tampilkan_identitas())
print(p1.Alamat_lengkap())
print("Usia:", p1.Usia(2025))
print("Status Kawin:", p1.cek_status_perkawinan())
print("Pekerjaan sesuai pendidikan:", p1.pekerjaan_sesuai_pendidikan())
print(p1.update_pekerjaan("Dosen"))
print("\n=== Data Lengkap ===")
print(p1)
'''