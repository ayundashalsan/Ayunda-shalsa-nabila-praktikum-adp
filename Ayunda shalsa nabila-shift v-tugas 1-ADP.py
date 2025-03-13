print("============= SELAMAT DATANG DI RESTORAN TRENDY ^.^ ==============")
print("Menu                Paket Makanan                           Harga")
print(" 1.   Burger + French Fries + Cola                        Rp75.000")
print(" 2.   Pasta Carbonara + Garlic Bread + Lemonade           Rp85.000")
print(" 3.   Sushi Rolls + Teriyaki Chicken + Miso Soup          Rp95.000")
print(" 4.   Bulgogi Beef + Kimchi + Barley Tea                  Rp90.000")
print(" 5.   Chicken Shawarma + Hummus + Mint Tea                Rp80.000")
#menu dan harga
menu1, harga1 = "Burger + French Fries + Cola"              , 75000
menu2, harga2 = "Pasta Carbonara + Garlic Bread + Lemonade ", 85000
menu3, harga3 = "Sushi Rolls + Teriyaki Chicken + Miso Soup", 95000
menu4, harga4 = "Bulgogi Beef + Kimchi + Barley Tea  "      , 90000
menu5, harga5 = "Chicken Shawarma + Hummus + Mint Tea "     , 80000
print("======================== DATA PELANGGAN ==========================")
nama = input("Masukkan nama anda: ")
telepon = input("Masukkan No Telepon: ")
jenis_alamat_pengiriman = input("Masukkan jenis alamat pengiriman: ")

# Pesanan pertama
pilihan1 = int(input("Masukkan nomor menu pesanan pertama: "))
jumlah1 = int(input("Masukkan jumlah: "))

# Pesanan kedua
pilihan2 = int(input("Masukkan nomor menu pesanan kedua: "))
jumlah2 = int(input("Masukkan jumlah: "))

# Pesanan ketiga
pilihan3 = int(input("Masukkan nomor menu pesanan ketiga: "))
jumlah3 = int(input("Masukkan jumlah: "))

# Pesanan keempat
pilihan4 = int(input("Masukkan nomor menu pesanan keempat: "))
jumlah4 = int(input("Masukkan jumlah: "))

# Pesanan kelima
pilihan5 = int(input("Masukkan nomor menu pesanan kelima: "))
jumlah5 = int(input("Masukkan jumlah: "))

# menetapkan/mendeklerasikan
total_harga = 0
pesanan = ""
# Hitung pajak dan biaya pengiriman
pajak = total_harga * 0.1
total_bayar = total_harga + pajak
if total_harga < 150000:
    biaya_pengiriman = 25000
else:
    biaya_pengiriman = 0
total_akhir = float(total_bayar + biaya_pengiriman)      
# Cetak struk
print("========================== STRUK PEMESANAN ========================")
print("Nama pelanggan      :", nama)
print("Telepon             :", telepon)
print("Alamat              :", jenis_alamat_pengiriman)
print("Pesanan             :", pesanan)
if pilihan1 == 1:
    total_harga += jumlah1 * harga1
    print(menu1, "x", jumlah1, "=", jumlah1 * harga1)
elif pilihan1 == 2:
    total_harga += jumlah1 * harga2
    print(menu2, "x", jumlah1, "=", jumlah1 * harga2)
elif pilihan1 == 3:
    total_harga += jumlah1 * harga3
    print(menu3, "x", jumlah1, "=", jumlah1 * harga3)
elif pilihan1 == 4:
    total_harga += jumlah1 * harga4
    print(menu4, "x", jumlah1, "=", jumlah1 * harga4)
elif pilihan1 == 5:
    total_harga += jumlah1 * harga5
    print(menu5, "x", jumlah1, "=", jumlah1 * harga5)
    
if pilihan2 == 1:
        total_harga += jumlah2 * harga1
        print(menu1, "x", jumlah2, "=", jumlah2 * harga1)
elif pilihan2 == 2:
        total_harga += jumlah2 * harga2
        print(menu2, "x", jumlah2, "=", jumlah2 * harga2)
elif pilihan2 == 3:
        total_harga += jumlah2 * harga3
        print(menu3, "x", jumlah2, "=", jumlah2 * harga3)
elif pilihan2 == 4:
        total_harga += jumlah2 * harga4
        print(menu4, "x", jumlah2, "=", jumlah2 * harga4)
elif pilihan2 == 5:
        total_harga += jumlah2 * harga5
        print(menu5, "x", jumlah2, "=", jumlah2 * harga5)
        
if pilihan3 == 1:
        total_harga += jumlah3 * harga1
        print(menu1, "x", jumlah3, "=", jumlah3 * harga1)
elif pilihan3 == 2:
        total_harga += jumlah3 * harga2
        print(menu2, "x", jumlah3, "=", jumlah3 * harga2)
elif pilihan3 == 3:
        total_harga += jumlah3 * harga3
        print(menu3, "x", jumlah3, "=", jumlah3 * harga3)
elif pilihan3 == 4:
        total_harga += jumlah3 * harga4
        print(menu4, "x", jumlah3, "=", jumlah3 * harga4)
elif pilihan3 == 5:
        total_harga += jumlah3 * harga5
        print(menu5, "x", jumlah3, "=", jumlah3 * harga5)
        
if pilihan4 == 1:
        total_harga += jumlah4 * harga1
        print(menu1, "x", jumlah4, "=", jumlah4 * harga1)
elif pilihan4 == 2:
        total_harga += jumlah4 * harga2
        print(menu2, "x", jumlah4, "=", jumlah4 * harga2)
elif pilihan4 == 3:
        total_harga += jumlah4 * harga3
        print(menu3, "x", jumlah4, "=", jumlah4 * harga3)
elif pilihan4 == 4:
        total_harga += jumlah4 * harga4
        print(menu4, "x", jumlah4, "=", jumlah4 * harga4)
elif pilihan4 == 5:
        total_harga += jumlah4 * harga5
        print(menu5, "x", jumlah4, "=", jumlah4 * harga5)
        
if pilihan5 == 1:
        total_harga += jumlah5 * harga1
        print(menu1, "x", jumlah5, "=", jumlah5 * harga1)
elif pilihan5 == 2:
        total_harga += jumlah5 * harga2
        print(menu2, "x", jumlah5, "=", jumlah5 * harga2) 
elif pilihan5 == 3:
        total_harga += jumlah5 * harga3
        print(menu3, "x", jumlah5, "=", jumlah5 * harga3)
elif pilihan5 == 4:
        total_harga += jumlah5 * harga4
        print(menu4, "x", jumlah5, "=", jumlah5 * harga4)
elif pilihan5 == 5:
        total_harga += jumlah5 * harga5
        print(menu5, "x", jumlah5, "=", jumlah5 * harga5)
print("Total Harga         : Rp", total_harga)
print("Pajak (10%)         : Rp", pajak)
print("Biaya Pengiriman    : Rp", biaya_pengiriman)
print("===============================================================")
print("Total Bayar         : Rp", total_akhir)
print("===============================================================")
print("Terima kasih telah memesan di Restoran Trendy!")

