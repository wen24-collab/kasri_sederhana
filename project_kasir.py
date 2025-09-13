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

#tampilan menu makanan
def tampilan_menu():
    global total 
    
    print("\n---MASUKAN PRODUK YANG INGIN DI BELI---")
    
    nama_produk = input("MASUKAN NAMA PRODUK: ")
    jumlah_produk = int(input("MASUKAN JUMLAH PRODUK: "))
    harga_produk = int(input("MASUKAN HARGA PRODUK: "))
    total_produk = jumlah_produk * harga_produk
    print(f"TOTAL HARGA {nama_produk} = Rp {total_produk}")
    return nama_produk, jumlah_produk, harga_produk, total_produk
    
    
tampilan_menu()