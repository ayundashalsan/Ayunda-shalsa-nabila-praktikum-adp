print("============= SELAMAT DATANG DI RESTORAN TRENDY ^.^ ==============")
print("Menu                Paket Makanan                           Harga")
print(" 1.   Burger + French Fries + Cola                        Rp75.000")
print(" 2.   Pasta Carbonara + Garlic Bread + Lemonade           Rp85.000")
print(" 3.   Sushi Rolls + Teriyaki Chicken + Miso Soup          Rp95.000")
print(" 4.   Bulgogi Beef + Kimchi + Barley Tea                  Rp90.000")
print(" 5.   Chicken Shawarma + Hummus + Mint Tea                Rp80.000")

print("======================== DATA PELANGGAN ==========================")
nama = input("Masukkan nama anda: ")
telepon = input("Masukkan No Telepon: ")
Jenis_alamat_pengiriman = input("Masukkan jenis alamat pengiriman: ")
# Input pesanan
pilihan = int(input("Masukkan nomor menu yang ingin dipesan (1-5): "))
jumlah = int(input("Masukkan jumlah pesanan: " ))

# Menentukan menu
if pilihan == 1:
    menu_pesanan = "Burger + French Fries + Cola"
    harga = 75000
elif pilihan == 2:
    menu_pesanan = "Pasta Carbonara + Garlic Bread + Lemonade"
    harga = 85000
elif pilihan == 3:
    menu_pesanan = "Sushi Rolls + Teriyaki Chicken + Miso Soup"
    harga = 95000
elif pilihan == 4:
    menu_pesanan = "Bulgogi Beef + Kimchi + Barley Tea"
    harga = 90000
elif pilihan == 5:
    menu_pesanan = "Chicken Shawarma + Hummus + Mint Tea"
    harga = 80000
else:
    print("Pilihan menu tidak valid!")
    
# Menghitung total harga
total_harga = jumlah * harga
pajak = total_harga * 0.1
if total_harga < 150000:
    biaya_pengiriman = 25000
else:
    biaya_pengiriman = 0
total_akhir = float(total_harga + pajak + biaya_pengiriman)   
# Cetak struk
print("========================== STRUK PEMESANAN ========================")
print("Nama pelanggan      :", nama)
print("Telepon             :", telepon)
print("Alamat              :", Jenis_alamat_pengiriman)
print("Pesanan             :", menu_pesanan, )
print("jumlah              :", jumlah )
print("total_harga         : Rp", total_akhir)
print("Pajak (10%)         : Rp", pajak)
print("Biaya Pengiriman    : Rp", biaya_pengiriman)
print("===============================================================")
print("Total Bayar         : Rp", total_akhir)
print("===============================================================")
print("Terima kasih telah memesan di Restoran Trendy!")