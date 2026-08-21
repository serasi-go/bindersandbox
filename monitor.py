import time
import psutil

def ubah_ke_gb(nilai_bytes):
    # Mengonversi data bytes menjadi satuan Gigabyte (GB)
    return round(nilai_bytes / (1024 ** 3), 2)

try:
    # Trik Anti-Flicker: Bersihkan layar sekali saja di awal
    print("\033[2J\033[H", end="")
    
    while True:
        # Trik Anti-Flicker: Kembalikan kursor ke pojok kiri atas tanpa menghapus layar
        print("\033[H", end="")
        
        # 1. Mengambil Data Prosesor (CPU)
        cpu_persen = psutil.cpu_percent(interval=1) # Mengukur beban sistem
        cpu_logis = psutil.cpu_count()
        cpu_fisik = psutil.cpu_count(logical=False)
        
        # 2. Mengambil Data Memori (RAM)
        ram_info = psutil.virtual_memory()
        ram_total = ubah_ke_gb(ram_info.total)
        ram_terpakai = ubah_ke_gb(ram_info.used)
        ram_tersedia = ubah_ke_gb(ram_info.available)
        ram_persen = ram_info.percent
        
        # 3. Menampilkan Antarmuka Dasbor (Menimpa teks lama dengan rapi)
        print("==================================================")
        print("       PEMANTAU SUMBER DAYA SISTEM (MYBINDER)     ")
        print("==================================================")
        print(f" Penggunaan CPU : [{cpu_persen}%]                     ") # Spasi tambahan untuk membersihkan sisa karakter lama
        print(f" Inti CPU (Core): {cpu_fisik} Fisik / {cpu_logis} Logis      ")
        print("--------------------------------------------------")
        print(f" Total RAM      : {ram_total} GB                      ")
        print(f" RAM Terpakai   : {ram_terpakai} GB ({ram_persen}%)    ")
        print(f" RAM Tersedia   : {ram_tersedia} GB                   ")
        print("==================================================")
        print(" Status         : Pemantauan aktif... (Mulus)     ")
        print("==================================================")
        
except KeyboardInterrupt:
    print("\n\nPemantauan dihentikan oleh pengguna.\n")
