# Program Kasir Sederhana

# Inisialisasi variabel global
nama_USER = ""
tanggal = ""
keranjang = []
total = 0

#validasi input user
def setup_awal():
    global nama_kasir, tanggal
    print("=" * 40)
    print("        SETUP KASIR")
    print("=" * 40)
    nama_kasir = input("Masukkan Nama USER: ")
    tanggal = input("Masukkan Tanggal (dd/mm/yyyy): ")
    if not tanggal:
        # Jika tidak diisi, gunakan tanggal hari ini
        from datetime import datetime
        tanggal = datetime.now().strftime("%d/%m/%Y")
        print("setup sudah selesai silahkan tekan ENTER untuk melanjutkan")
        
setup_awal()




#tampilan setup user
def tampilan_setup():
    print("=" * 40)
    print("        MENU KASIR")
    print("=" * 40)
    print(f"NAMA USER: {nama_kasir}")
    print(f"TANGGAL: {tanggal}")
tampilan_setup()


manu_makanan = {
    "Nasi Goreng"   :       "20.000",
     "Mie Ayam"     :       "20.000",
     "Sate Ayam"    :       "25.000",
     "Gado-Gado"    :       "15.000",
     "Bakso"        :       "18.000"
}
#tampilan menu makanan
def pilih_makanan():
    global nama_makanan, jumlah_makanan, harga_makanan, total
    
    print("\n==== SILAHKAN PILIH MAKANAN YANG INGIN ANDA PESAN ====")
    for nomer, makanan, in manu_makanan.items():
        print(f"{nomer}. {makanan}")
    print("\n----SILAHKAN PILIH MENU MAKANAN----")
    
    nama_makanan = input("MASUKAN NAMA MAKANAN: ")
    jumlah_makanan = int(input("MASUKAN JUMLAH PORSI: "))
    harga_makanan = float(input("MASUKAN HARGA PERPORSI: "))
    total += jumlah_makanan * harga_makanan
    print("PILIHAN KAMU SUDAH MASUK")
    
menu_minumnan = {
    "ES TEH" : "5.000",
    "ES JERUK" : "7.000",
    "KOPI" : "5.000",
    "TEH ANGET" : "5.000"
    
}


        
def pilih_minuman():
    global minuman, jumlah_minuman, harga, total
    
    print("\n======SILAHKAN PILIH MINUMAN YANG AKAN ANDA PESAN======")
    for minuman, harga in menu_minumnan.items():
        print(f"{minuman}. {harga}")
        
    print("\n--------SILAHKAN PILIH MINUMAN--------")
    
    minuman = input("masukann minuman yang anda pilih: ")
    jumlah_minuman = int(input("masukan jumlaha pesanan: "))
    harga = float(input("harga minuman: "))
    total += jumlah_minuman * harga
    print("PILIHAN KAMU SUDAH MASUK")
    

def rincian_MAKAN():
    print("\n----RINCIAN BELANJA----")
    
    print("\n=====RINCIAN MAKANAN=====")
    print(f"MAKANAN YANG ANDA PESAN: {nama_makanan}")
    print(f"JUMLAH PESANAN ANDA: {jumlah_makanan}")
    print(f"HARGA MAKAN PERPORSI: {harga_makanan:,.3f}")
    print(f"TOTAL HARGA MAKANAN: {total:,.3f}")
    
def rincian_minum(): 
    print("\n=====RINCIAN MINUMAN=====")
    print(f"minuman yang anda pesan: {minuman}")
    print(f"jumlah pesanan anda: {jumlah_minuman}")
    print(f"harga pergelas: {harga:,.3f}")
    print(f"TOTAL PESANAN ANDA: {total:,.3f}")
    

def main():
    style = "=" * 20 
    print(style)
    print("PILIH PROGRAM")
    print(style)
    
    print("1. PESAN MAKANAN")
    print("2. PESAN MINUMAN")
    print("3. KELUAR")
    
   
    
    
main()
pesanan = (str(input("silahkan masukan pesanan anda: ")))
if pesanan == "1":
    pilih_makanan()
    rincian_MAKAN()
elif pesanan == "2":
    pilih_minuman()
    rincian_minum()
else:
    exit()
