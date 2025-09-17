# Program Kasir Sederhana yang Diperbarui

# Inisialisasi variabel global
nama_kasir = ""
tanggal = ""
keranjang = []
total = 0

def setup_awal():
    global nama_kasir, tanggal
    print("=" * 40)
    print("        SETUP KASIR")
    print("=" * 40)
    nama_kasir = input("Masukkan Nama USER: ")
    tanggal = input("Masukkan Tanggal (dd/mm/yyyy): ")
    if not tanggal:
        from datetime import datetime
        tanggal = datetime.now().strftime("%d/%m/%Y")
    print("Setup sudah selesai. Silahkan tekan ENTER untuk melanjutkan")
    input()

def tampilan_setup():
    print("=" * 40)
    print("        MENU KASIR")
    print("=" * 40)
    print(f"NAMA USER: {nama_kasir}")
    print(f"TANGGAL: {tanggal}")

def tambah_produk():
    print("\n---TAMBAH PRODUK---")
    
    nama_produk = input("MASUKAN NAMA PRODUK: ")  
    try:
        jumlah_produk = int(input("MASUKAN JUMLAH PRODUK: "))
        harga_produk = float(input("MASUKAN HARGA PRODUK: "))
        subtotal = jumlah_produk * harga_produk
        
        # Tambahkan ke keranjang
        keranjang.append({
            'nama': nama_produk,
            'jumlah': jumlah_produk,
            'harga': harga_produk,
            'subtotal': subtotal
        })
        
        print(f"Produk {nama_produk} berhasil ditambahkan!")
    except ValueError:
        print("Error: Jumlah dan harga harus berupa angka!")

def lihat_keranjang():
    print("\n" + "=" * 60)
    print("                      KERANJANG BELANJA")
    print("=" * 60)
    print(f"{'No':<5} {'Nama Produk':<20} {'Jumlah':<10} {'Harga':<15} {'Subtotal':<15}")
    print("-" * 60)
    
    for i, item in enumerate(keranjang, 1):
        print(f"{i:<5} {item['nama']:<20} {item['jumlah']:<10} {item['harga']:<15.2f} {item['subtotal']:<15.2f}")
    
    print("=" * 60)

def hitung_total():
    global total
    total = sum(item['subtotal'] for item in keranjang)
    print(f"\nTOTAL BELANJA: Rp {total:,.2f}")
    return total

def proses_pembayaran():
    global total
    if total == 0:
        hitung_total()
    
    print("\n---PROSES PEMBAYARAN---")
    try:
        bayar = float(input("Masukkan jumlah pembayaran: Rp "))
        if bayar < total:
            print("Pembayaran kurang! Silakan masukkan jumlah yang cukup.")
            return False
        else:
            kembalian = bayar - total
            print(f"Kembalian: Rp {kembalian:,.2f}")
            return True
    except ValueError:
        print("Error: Jumlah pembayaran harus berupa angka!")
        return False

def cetak_struk():
    print("\n" + "=" * 60)
    print("                      STRUK PEMBELIAN")
    print("=" * 60)
    print(f"Kasir: {nama_kasir}")
    print(f"Tanggal: {tanggal}")
    print("=" * 60)
    
    for item in keranjang:
        print(f"{item['nama']} - {item['jumlah']} x Rp {item['harga']:,.2f} = Rp {item['subtotal']:,.2f}")
    
    print("=" * 60)
    print(f"TOTAL: Rp {total:,.2f}")
    print("=" * 60)
    print("Terima kasih telah berbelanja!")
    print("=" * 60)

def main():
    setup_awal()
    
    while True:
        tampilan_setup()
        print("\nPilihan Menu:")
        print("1. Tambah Produk")
        print("2. Lihat Keranjang")
        print("3. Hitung Total")
        print("4. Bayar")
        print("5. Cetak Struk")
        print("6. Keluar")
        
        pilihan = input("Masukkan pilihan (1-6): ")
        
        if pilihan == "1":
            tambah_produk()
        elif pilihan == "2":
            lihat_keranjang()
        elif pilihan == "3":
            hitung_total()
        elif pilihan == "4":
            if proses_pembayaran():
                print("Pembayaran berhasil!")
            else:
                print("Pembayaran gagal!")
        elif pilihan == "5":
            cetak_struk()
        elif pilihan == "6":
            print("Terima kasih telah menggunakan program kasir!")
            break
        else:
            print("Pilihan tidak valid! Silakan pilih 1-6.")
        
        input("\nTekan ENTER untuk melanjutkan...")

if __name__ == "__main__":
    main()