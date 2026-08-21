import time
import psutil

def ubah_ke_gb(nilai_bytes):
    # Mengonversi data bytes menjadi satuan Gigabyte (GB)
    return round(nilai_bytes / (1024 ** 3), 2)

try:
    # Anti-Flicker: Bersihkan layar sekali saja di awal
    print("\033[2J\033[H", end="")
    
    while True:
        # Anti-Flicker: Kembalikan kursor ke pojok kiri atas tanpa menghapus layar
        print("\033[H", end="")
        
        # 1. Mengambil Data Prosesor (CPU)
        cpu_persen = psutil.cpu_percent(interval=1)
        cpu_logis = psutil.cpu_count()
        cpu_fisik = psutil.cpu_count(logical=False)
        
        # 2. Mengambil Data Memori (RAM)
        ram_info = psutil.virtual_memory()
        ram_total = ubah_ke_gb(ram_info.total)
        ram_terpakai = ubah_ke_gb(ram_info.used)
        ram_tersedia = ubah_ke_gb(ram_info.available)
        ram_persen = ram_info.percent
        
        # 3. Mengambil Data Hardisk (Disk Storage)
        # Menghitung partisi utama root ('/') tempat sistem MyBinder berjalan
        disk_info = psutil.disk_usage('/')
        disk_total = ubah_ke_gb(disk_info.total)
        disk_terpakai = ubah_ke_gb(disk_info.used)
        disk_bebas = ubah_ke_gb(disk_info.free)
        disk_persen = disk_info.percent
        
        # 4. Menampilkan Antarmuka Dasbor Lengkap
        print("==================================================")
        print("       PEMANTAU SUMBER DAYA SISTEM (MYBINDER)     ")
        print("==================================================")
        print(f" Penggunaan CPU : [{cpu_persen}%]                     ")
        print(f" Inti CPU (Core): {cpu_fisik} Fisik / {cpu_logis} Logis      ")
        print("--------------------------------------------------")
        print(f" Total RAM      : {ram_total} GB                      ")
        print(f" RAM Terpakai   : {ram_terpakai} GB ({ram_persen}%)    ")
        print(f" RAM Tersedia   : {ram_tersedia} GB                   ")
        print("--------------------------------------------------")
        print(f" Total Hardisk  : {disk_total} GB                     ")
        print(f" Disk Terpakai  : {disk_terpakai} GB ({disk_persen}%) ")
        print(f" Disk Tersisa   : {disk_bebas} GB                     ")
        print("==================================================")
        print(" Status         : Pemantauan aktif... (Mulus)     ")
        print("==================================================")
        
except KeyboardInterrupt:
    print("\n\nPemantauan dihentikan oleh pengguna.\n")
