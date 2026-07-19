import time
import os
import sys
import pygame
import shutil

# ==================== WARNA TERMINAL ====================
class Warna:
    PUTIH_TEBAL = '\033[1;97m' # Putih terang dan tebal untuk lirik asli aktif
    PUTIH_BIASA = '\033[0;97m' # Putih biasa untuk terjemahan aktif
    ABU_ABU = '\033[90m'       # Abu-abu redup
    RESET = '\033[0m'

# ==================== KONFIGURASI LIRIK & TERJEMAHAN ====================
# Format: (timestamp, "Lirik Asli", "Terjemahan")
lyrics = [
    (44.85, "I know a place", "(Aku tahu sebuah tempat)"),
    (54.53, "It's somewhere I go when I need to remember your face", "(Itu adalah tempat di mana aku pergi ketika aku perlu mengingat wajahmu)"),
    (64.16, "We get married in our heads", "(Kita menikah di dalam pikiran kita)"),
    (74.77, "Something to do while we try to recall how we met", "(Ada sesuatu yang harus dilakukan sementara kita mencoba mengingat bagaimana kita bertemu)"),
    (81.21, "", ""),
    (84.21, "Do you think I have forgotten?", "(Apakah kamu pikir aku sudah lupa?)"),
    (89.22, "Do you think I have forgotten?", "(Apakah kamu pikir aku sudah lupa?)"),
    (94.12, "Do you think I have forgotten about you?", "(Apakah kamu pikir aku sudah lupa tentangmu?)"),
    (101.67, "", ""),
    (104.27, "You and I", "(Kamu dan Aku)"),
    (109.12, "Were alive", "(Kita masih hidup)"),
    (114.44, "With nothing to do I could lay and just look in your eyes", "(Dengan tidak ada yang harus dilakukan, aku bisa berbaring dan hanya menatap matamu)"),
    (124.81, "Wait and pretend", "(Tunggu dan berpura-pura)"),
    (134.84, "Hold on and hope that we'll find our way back in the end", "(Tetap berpegang dan berharap kita akan menemukan jalan kembali di akhir)"),
    (141.36, "", ""),
    (144.28, "Do you think I have forgotten?", "(Apakah kamu pikir aku sudah lupa?)"),
    (149.16, "Do you think I have forgotten?", "(Apakah kamu pikir aku sudah lupa?)"),
    (154.1, "Do you think I have forgotten about you?", "(Apakah kamu pikir aku sudah lupa tentangmu?)"),
    (164.25, "Do you think I have forgotten?", "(Apakah kamu pikir aku sudah lupa?)"),
    (169.23, "Do you think I have forgotten?", "(Apakah kamu pikir aku sudah lupa?)"),
    (174.12, "Do you think I have forgotten about you?", "(Apakah kamu pikir aku sudah lupa tentangmu?)"),
    (181.86, "", ""),
    (184.6, "There was something about you that now I can't remember", "(Ada sesuatu tentangmu yang sekarang tidak bisa kupingin)"),
    (189.51, "It's the same damn thing that made my heart surrender", "(Itu adalah hal yang sama yang membuat hatiku menyerah)"),
    (194.51, "And I'll miss you on a train", "(Dan aku akan merindukanmu di kereta api)"),
    (196.98, "I'll miss you in the morning", "(Aku akan merindukanmu di pagi hari)"),
    (199.5, "I never know what to think about", "(Aku tidak pernah tahu harus berpikir apa tentang)"),
    (203.83, "", ""),
    (203.63, "I think about you", "(Aku memikirkanmu)"),
    (209.23, "About you", "(Tentangmu)"),
    (214.24, "Do you think I have forgotten about you?", "(Apakah kamu pikir aku sudah lupa tentangmu?)"),
    (224.17, "About you", "(Tentangmu)"),
    (229.3, "About you", "(Tentangmu)"),
    (234.22, "Do you think I have forgotten about you?", "(Apakah kamu pikir aku sudah lupa tentangmu?)"),
    (242.78, "", ""),
]

MP3_FILE = "about_you.mp3"

# ==================== FUNGSI BANTUAN ====================
def get_term_width():
    return shutil.get_terminal_size((80, 20)).columns

def cetak_tengah(teks, warna=Warna.RESET):
    lebar = get_term_width()
    teks_tengah = teks.center(lebar)
    print(f"{warna}{teks_tengah}{Warna.RESET}")

# === MAIN PROGRAM BY "saya_makmum" ===
def main():
    if os.name == 'nt':
        os.system('')

    if not os.path.exists(MP3_FILE):
        print(f"Error: File '{MP3_FILE}' tidak ditemukan!")
        input("\nTekan Enter untuk keluar...")
        sys.exit(1)
        
    pygame.mixer.init()
    
    try:
        pygame.mixer.music.load(MP3_FILE)
    except Exception as e:
        print(f"Error memuat file: {e}")
        input("\nTekan Enter untuk keluar...")
        sys.exit(1)
        
    lyrics.sort(key=lambda x: x[0])
    
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print("\n" * 5)
    cetak_tengah("about you", Warna.PUTIH_TEBAL)
    print("\n")
    cetak_tengah("press enter to playing", Warna.ABU_ABU)
    input()
    
    os.system('cls' if os.name == 'nt' else 'clear')
    
    pygame.mixer.music.play()
    
    current_index = -1
    is_playing = True
    
    while is_playing:
        if not pygame.mixer.music.get_busy():
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\n" * 5)
            cetak_tengah("----------------------------------------", Warna.ABU_ABU)
            cetak_tengah("Pemutaran Selesai!", Warna.PUTIH_TEBAL)
            cetak_tengah("========================================", Warna.ABU_ABU)
            print("\n" * 5)
            is_playing = False
            break
            
        current_time = pygame.mixer.music.get_pos() / 1000.0
        
        target_index = -1
        for i, (timestamp, text, translation) in enumerate(lyrics):
            if current_time >= timestamp:
                target_index = i
            else:
                break
                
        if target_index != -1 and target_index != current_index:
            current_index = target_index
            
            sys.stdout.write('\033[H')
            sys.stdout.flush()
            
            print("\n" * 3)
            
            cetak_tengah("", Warna.ABU_ABU)
            cetak_tengah("about you", Warna.PUTIH_TEBAL)
            cetak_tengah("", Warna.ABU_ABU)
            
            print("\n" * 2) 
            
            # 1. Lirik Sebelumnya (Abu-abu redup, tanpa terjemahan)
            if current_index > 0:
                cetak_tengah(lyrics[current_index-1][1], Warna.ABU_ABU)
            else:
                cetak_tengah("", Warna.ABU_ABU)
                
            # 2. Lirik Saat Ini (Asli & Terjemahan)
            print("\n")
            cetak_tengah(lyrics[current_index][1], Warna.PUTIH_TEBAL) # Asli: Putih Tebal
            
            terjemahan_aktif = lyrics[current_index][2]
            if terjemahan_aktif != "":
                cetak_tengah(terjemahan_aktif, Warna.PUTIH_BIASA) # Terjemahan: Putih Biasa
            else:
                cetak_tengah("", Warna.PUTIH_BIASA) # Spasi kosong agar tinggi tetap stabil
            print("\n")
            
            # 3. Lirik Selanjutnya (Abu-abu redup, tanpa terjemahan)
            if current_index < len(lyrics) - 1:
                cetak_tengah(lyrics[current_index+1][1], Warna.ABU_ABU)
            else:
                cetak_tengah("", Warna.ABU_ABU)
                
            # Timpa sisa layar bawah
            print("\n" * 4)
            for _ in range(5):
                cetak_tengah("")
            
        time.sleep(0.02)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n" * 5)
        cetak_tengah("Program dihentikan oleh user.", Warna.ABU_ABU)
        print("\n" * 5)
        pygame.mixer.music.stop()