"""
Terminal Music Player with Synchronized Lyrics
Plays MP3 and appends clean text lyrics downward
"""

import time
import os
import sys
import pygame

# ==================== KONFIGURASI LIRIK ====================
lyrics = [
    (0.0, "​Kini serahkan semua ujungnya pada takdir"),
    (7.56, "Jika beruntung, maka kisah ini tak akan berakhir"),
    (16.14, ""),
    (18.31, "Untuk sejenak"),
    (19.83, "Kumohon berhenti perdebatkan yang tak penting"),
    (25.23, "Kita berdamai, berjabat tangan"),
    (29.63, "Tertawakan yang tak bisa dibenahi"),
    (34.82, "Anggap saja besok ini semua hilang"),
    (39.2, "Cerita seperti apa yang mau kau kenang?"),
    (45.02, "Kita buat menyenangkan"),
    (49.36, "Di sisa waktu yang ada"),
    (53.76, "Jika ada yang salah"),
    (56.36, "Jika kau kecewa"),
    (58.48, "Tolong maafkan"),
    (62.89, "Kita buat menyenangkan"),
    (67.25, "Takkan tahu sampai kapan"),
    (71.63, "Selagi ku masih bisa"),
    (76.16, "Kita buat menyenangkan.. ha.. haa.."),
    (85.13, ""),
    (86.94, "Tiada yang tahu pasti"),
    (91.5, "Mungkin dalam hitungan hari"),
    (94.28, "Semua berhenti"),
    (96.26, "Dan bisa jadi"),
    (98.54, "Kita tak ada lagi"),
    (102.69, ""),
    (104.61, "Sebelum terlambat"),
    (106.27, "Kuucapkan banyak terima kasih"),
    (111.92, "Karena mengenalmu"),
    (114.36, "Buatku jadi"),
    (116.41, "Aku yang seperti ini"),
    (121.62, "Anggap saja besok ini semua hilang"),
    (125.76, "Semoga yang kau ingat hanya yang baiknya"),
    (131.7, "Kita buat menyenangkan"),
    (136.04, "Di sisa waktu yang ada"),
    (140.47, "Jika ada yang salah"),
    (142.85, "Jika kau kecewa"),
    (145.08, "Tolong maafkan"),
    (149.41, "Kita buat menyenangkan"),
    (153.94, "Takkan tahu sampai kapan"),
    (158.18, "Selagi ku masih bisa"),
    (162.89, "Kita buat menyenangkan"),
    (168.12, "Ha ha ha"),
    (170.43, ""),
    (191.57, ""),
    (193.76, "Kita buat menyenangkan"),
    (198.32, "Di sisa waktu yang ada"),
    (202.68, "Jika ada yang salah"),
    (205.11, "Jika kau kecewa"),
    (207.29, "Tolong maafkan"),
    (211.59, "Kita buat menyenangkan"),
    (216.11, "Takkan tahu sampai kapan"),
    (220.45, "Selagi ku masih bisa"),
    (224.8, "Kita buat menyenangkan"),
    (229.38, "Selagi ku masih bisa"),
    (233.71, "Kita buat menyenangkan.. aa-aan..."),
    (242.78, ""),
]

MP3_FILE = "bernadya-kita_buat_menyenangkan.mp3"

# ==================== MAIN PROGRAM ====================
def main():
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
    
    # Bersihkan layar di awal
    os.system('cls' if os.name == 'nt' else 'clear')
    print("==================================================")
    print("Kita Buat Menyenangkan - Bernadya")
    print("by: @saya_makmum")
    print("==================================================")
    
    input("\nTekan Enter untuk mulai memutar...\n")
    
    # Mulai musik
    pygame.mixer.music.play()
    
    current_index = -1
    is_playing = True
    
    while is_playing:
        if not pygame.mixer.music.get_busy():
            print("\n--------------------------------------------------")
            print("Pemutaran Selesai!")
            print("==================================================")
            is_playing = False
            break
            
        # Dapatkan waktu musik saat ini (dalam detik)
        current_time = pygame.mixer.music.get_pos() / 1000.0
        
        # Cek apakah sudah waktunya lirik berikutnya muncul
        target_index = -1
        for i, (timestamp, text) in enumerate(lyrics):
            if current_time >= timestamp:
                target_index = i
            else:
                break
                
        # Jika ada lirik baru, langsung cetak teksnya saja ke bawah
        if target_index != -1 and target_index != current_index:
            current_index = target_index
            print(lyrics[current_index][1])
            
        time.sleep(0.02)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nProgram dihentikan oleh user.")
        pygame.mixer.music.stop()