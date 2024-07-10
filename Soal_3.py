class AntrianRestoran:
    def _init_(self):
        self.pesanan = []

    def enqueue(self, pesanan):
        self.pesanan.append(pesanan)
        print(f"Pesanan {pesanan} berhasil ditambahkan ke antrian.")

    def dequeue(self):
        if not self.pesanan:
            print("Antrian kosong.")
            return None
        pesanan_terdepan = self.pesanan.pop(0)
        print(f"Pesanan {pesanan_terdepan} dilayani.")
        return pesanan_terdepan


if _name_ == "_main_":
    antrian = AntrianRestoran()

    while True:
        print("\nMenu:")
        print("1. Tambah pesanan")
        print("2. Layani pesanan")
        print("3. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            pesanan = input("Masukkan pesanan: ")
            antrian.enqueue(pesanan)
        elif pilihan == "2":
            antrian.dequeue()
        elif pilihan == "3":
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid.")