data_hasil_panen = {
    "lokasi1": {
        "nama": "Kebun A",
        "panen": {"padi": 1200, "jagung": 800, "kedelai": 500},
    },
    "lokasi2": {
        "nama": "Kebun B",
        "panen": {"padi": 1500, "jagung": 900, "kedelai": 450},
    },
    "lokasi3": {
        "nama": "Kebun C",
        "panen": {"padi": 1100, "jagung": 750, "kedelai": 600},
    },
    "lokasi4": {
        "nama": "Kebun D",
        "panen": {"padi": 1300, "jagung": 850, "kedelai": 550},
    },
    "lokasi5": {
        "nama": "Kebun E",
        "panen": {"padi": 1400, "jagung": 950, "kedelai": 480},
    },
}

def tampilkan_semua_hasil(data):
    print("\nIni No. 1")
    for lokasi in data.values():
        print(f"Nama Lokasi: {lokasi['nama']}")
        print(f"Hasil Panen:\n  Padi: {lokasi['panen']['padi']}\n  Jagung: {lokasi['panen']['jagung']}\n  Kedelai: {lokasi['panen']['kedelai']}\n")

def tampilkan_hasil_lokasi_tertentu(data):
    print("\nIni No. 2")
    lokasi2 = data.get("lokasi2")
    if lokasi2:
        print(f"Lokasi: {lokasi2['nama']}")
        print(f"Hasil Panen Jagung: {lokasi2['panen']['jagung']}")

def tampilkan_nama_lokasi(data):
    print("\nIni No. 3")
    lokasi3 = data.get("lokasi3")
    if lokasi3:
        print(f"Nama Lokasi dari lokasi3: {lokasi3['nama']}")

def hitung_total_hasil(data):
    print("\nIni No. 4")
    total_padi = sum(lokasi["panen"]["padi"] for lokasi in data.values())
    total_kedelai = sum(lokasi["panen"]["kedelai"] for lokasi in data.values())
    print(f"Total Panen:\n  Padi: {total_padi}\n  Kedelai: {total_kedelai}")

def tampilkan_per_lokasi(data):
    print("\nNo. 5")
    for lokasi in data.values():
        print(f"Nama Lokasi: {lokasi['nama']}")
        print(f"  Padi: {lokasi['panen']['padi']}\n  Kedelai: {lokasi['panen']['kedelai']}\n  Jagung: {lokasi['panen']['jagung']}\n")

def cek_kondisi_lokasi(data):
    print("\nNo. 6")
    for lokasi in data.values():
        status = "butuh perhatian khusus" if lokasi['panen']['padi'] > 1300 or lokasi['panen']['jagung'] > 800 else "kondisi baik"
        print(f"Lokasi {lokasi['nama']} {status}")

def jalankan():
    tampilkan_semua_hasil(data_hasil_panen)
    tampilkan_hasil_lokasi_tertentu(data_hasil_panen)
    tampilkan_nama_lokasi(data_hasil_panen)
    hitung_total_hasil(data_hasil_panen)
    tampilkan_per_lokasi(data_hasil_panen)
    cek_kondisi_lokasi(data_hasil_panen)

if __name__ == "__main__":
    jalankan()
