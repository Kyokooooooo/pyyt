import pywhatkit

try:
    song = input("Masukkan judul lagu: ")
    pywhatkit.playonyt(song)
    print("Berhasil diputar!")
except Exception as e:  # Tangkap detail error
    print("Ada yang error:", e)
