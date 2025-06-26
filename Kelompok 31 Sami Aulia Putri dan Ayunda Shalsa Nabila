import os
import time
from termcolor import colored

def clear_screen():
    os.system('cls')  

def tampilkan_logo():
    logo = """
███╗░░░███╗██╗░░░██╗░██████╗██╗██╗░░██╗  ██████╗░░█████╗░██████╗░██╗
████╗░████║██║░░░██║██╔════╝██║██║░██╔╝  ██╔══██╗██╔══██╗██╔══██╗██║
██╔████╔██║██║░░░██║╚█████╗░██║█████═╝░  ██║░░██║███████║██████╔╝██║
██║╚██╔╝██║██║░░░██║░╚═══██╗██║██╔═██╗░  ██║░░██║██╔══██║██╔══██╗██║
██║░╚═╝░██║╚██████╔╝██████╔╝██║██║░╚██╗  ██████╔╝██║░░██║██║░░██║██║
╚═╝░░░░░╚═╝░╚═════╝░╚═════╝░╚═╝╚═╝░░╚═╝  ╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝

░██████╗██╗░░░██╗░█████╗░░██████╗░█████╗░███╗░░██╗░█████╗░  ██╗░░██╗░█████╗░████████╗██╗
██╔════╝██║░░░██║██╔══██╗██╔════╝██╔══██╗████╗░██║██╔══██╗  ██║░░██║██╔══██╗╚══██╔══╝██║
╚█████╗░██║░░░██║███████║╚█████╗░███████║██╔██╗██║███████║  ███████║███████║░░░██║░░░██║
░╚═══██╗██║░░░██║██╔══██║░╚═══██╗██╔══██║██║╚████║██╔══██║  ██╔══██║██╔══██║░░░██║░░░██║
██████╔╝╚██████╔╝██║░░██║██████╔╝██║░░██║██║░╚███║██║░░██║  ██║░░██║██║░░██║░░░██║░░░██║
╚═════╝░░╚═════╝░╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝  ╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝
"""
    print(colored(logo, "magenta"))

def warna_mood(mood):
    if mood == "happy":
        return "yellow"
    elif mood == "sad":
        return "blue"
    elif mood == "stress":
        return "red"
    elif mood == "semangat":
        return "green"
    else:
        return "white"

def rekomendasi_lagu(mood):
    if mood == "happy":
        return "tiara andini – flip it up"
    elif mood == "sad":
        return "yura yunita – dunia tipu-tipu"
    elif mood == "stress":
        return "nadin amizah – bertaut"
    elif mood == "semangat":
        return "gac – satu tujuan"
    else:
        return "lagu tidak ditemukan"

def input_data_mood(moods, hari=7):
    data_mood = [{"mood": "", "lagu": ""} for _ in range(hari)]
    for hari_ke in range(hari):
        print(f"\nhari ke-{hari_ke+1}")
        mood = input("mood kamu hari ini [happy/sad/stress/semangat] (gunakan huruf kecil): ")
        lagu = rekomendasi_lagu(mood)
        data_mood[hari_ke]["mood"] = mood
        data_mood[hari_ke]["lagu"] = lagu
    return data_mood

def animasi_teks(teks):
    print()  # baris kosong sebelum animasi
    for huruf in teks:
        print(huruf, end="", flush=True)
        time.sleep(0.05)  # jeda 0.05 detik antar huruf
    print()  # baris baru setelah animasi selesai

def tampilkan_grafik_mood(data_mood):
    print("\ngrafik mood mingguan:")
    for hari_ke in range(len(data_mood)):
        warna = warna_mood(data_mood[hari_ke]["mood"])
        mood_warna = colored(data_mood[hari_ke]["mood"], warna)
        print(f"hari {hari_ke+1}: [mood: {mood_warna}]")

def tampilkan_lagu_mingguan(data_mood):
    print("\nnada rasa mingguan (rekomendasi lagu):")
    warna_hari = ["red", "green", "yellow", "blue", "magenta", "white", "red"]
    for hari_ke in range(len(data_mood)):
        teks = f"hari {hari_ke+1}: {data_mood[hari_ke]['lagu']}"
        print(colored(teks, warna_hari[hari_ke]))

def hitung_statistik_mood(data_mood, mood_unik):
    jumlah_mood = [0] * len(mood_unik)
    for hari in data_mood:
        # Loop melalui indeks mood_unik secara manual
        for i in range(len(mood_unik)):
            m = mood_unik[i] # Dapatkan mood dari indeks
            if hari["mood"] == m:
                jumlah_mood[i] += 1
    return jumlah_mood


def tampilkan_rekap_mood(mood_unik, jumlah_mood):
    print("\nrekap emosi mingguan:")
    for i in range(len(mood_unik)):
        warna = warna_mood(mood_unik[i])
        mood_warna = colored(mood_unik[i], warna)
        print(f"{mood_warna:10}: {jumlah_mood[i]} hari")

def mood_terbanyak(mood_unik, jumlah_mood):
    maks = jumlah_mood[0]
    terbanyak = mood_unik[0]
    for i in range(1, len(jumlah_mood)):
        if jumlah_mood[i] > maks:
            maks = jumlah_mood[i]
            terbanyak = mood_unik[i]
    return terbanyak

def tampilkan_catatan(jumlah_sedih):
    if jumlah_sedih >= 3:
        print("\nkamu cukup sering merasa sedih minggu ini. semoga minggu depan lebih cerah.")
    elif jumlah_sedih == 0:
        print("\nhebat! tidak ada hari sedih minggu ini!")
    else:
        print(f"\nterdapat {jumlah_sedih} hari sedih minggu ini. tetap semangat ya!")

def simpan_ke_file(nama, data_mood, mood_unik, jumlah_mood, terbanyak, jumlah_sedih):
    with open("nada_rasa.txt", "w") as file:
        file.write("nada rasa mingguan – " + nama + "\n")
        for hari_ke in range(len(data_mood)):
            file.write("hari " + str(hari_ke+1) + ": mood = " + data_mood[hari_ke]["mood"] + ", lagu = " + data_mood[hari_ke]["lagu"] + "\n")
        file.write("\nrekap statistik:\n")
        for i in range(len(mood_unik)):
            file.write(f"- {mood_unik[i]}: {jumlah_mood[i]}\n")
        file.write("\nmood terbanyak: " + terbanyak + "\n")
        file.write("\njumlah hari sedih: " + str(jumlah_sedih) + "\n")
        if jumlah_sedih >= 3:
            file.write("catatan: kamu cukup sering merasa sedih minggu ini. semoga minggu depan lebih cerah.\n")
        elif jumlah_sedih == 0:
            file.write("catatan: hebat! tidak ada hari sedih minggu ini!\n")
        else:
            file.write("catatan: tetap semangat menghadapi minggu-minggu yang berat.\n")
    print("\ndata telah disimpan ke 'nada_rasa.txt'")

def main():
    clear_screen()
    tampilkan_logo()
    nama = input("masukkan nama kamu: ")
    moods = ["happy", "sad", "stress", "semangat"]
    mood_unik = moods.copy()
    data_mood = input_data_mood(moods)
    # Panggil animasi_teks tanpa delay parameter
    animasi_teks("mencari lagu terbaik minggu ini . . . . .")
    tampilkan_grafik_mood(data_mood)
    tampilkan_lagu_mingguan(data_mood)
    jumlah_mood = hitung_statistik_mood(data_mood, mood_unik)
    tampilkan_rekap_mood(mood_unik, jumlah_mood)
    terbanyak = mood_terbanyak(mood_unik, jumlah_mood)
    print(f"\nsuasana hati yang paling sering muncul minggu ini: {colored(terbanyak, warna_mood(terbanyak))}")
    jumlah_sedih = jumlah_mood[1]  # index ke-1 adalah 'sad'
    tampilkan_catatan(jumlah_sedih)
    print("\nterima kasih,", nama)
    print("jaga suasana hati dan terus melangkah dengan nada yang kamu pilih sendiri.")
    simpan_ke_file(nama, data_mood, mood_unik, jumlah_mood, terbanyak, jumlah_sedih)

main()
