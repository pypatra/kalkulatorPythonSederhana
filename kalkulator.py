import os


# Fungsi untuk menjumlahkan dua angka
def tambah(x, y):
    return x + y


# Fungsi untuk mengurangkan dua angka
def kurang(x, y):
    return x - y


# Fungsi untuk mengalikan dua angka
def kali(x, y):
    return x * y


# Fungsi untuk membagi dua angka
def bagi(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Pembagian oleh nol tidak diizinkan"


# Fungsi untuk meminta input angka dari pengguna
def input_angka():
    while True:
        try:
            angka = float(input("Masukkan angka: "))
            return angka
        except ValueError:
            print("Input tidak valid. Harap masukkan angka.")


# Fungsi untuk meminta operasi matematika dari pengguna
def input_operasi():
    operasi = input("Pilih operasi (+, -, *, /): ")
    if operasi in ["+", "-", "*", "/"]:
        return operasi
    else:
        print("Operasi tidak valid. Harap pilih operasi yang benar.")
        return input_operasi()


# Program utama
while True:
    os.system("cls")  # Membersihkan layar (Windows)
    print("=" * 20)
    print("Kalkulator".center(20))
    print("=" * 20)

    angka1 = input_angka()
    angka2 = input_angka()
    operasi = input_operasi()

    hasil = None  # Inisialisasi hasil dengan None

    # Memproses operasi matematika yang dipilih
    if operasi == "+":
        hasil = tambah(angka1, angka2)
    elif operasi == "-":
        hasil = kurang(angka1, angka2)
    elif operasi == "*":
        hasil = kali(angka1, angka2)
    elif operasi == "/":
        hasil = bagi(angka1, angka2)

    # Menampilkan hasil atau pesan kesalahan
    if hasil is not None:
        print("=" * 20)
        print("Hasil: {}".format(hasil))
        print("=" * 20)
    else:
        print("Operasi tidak valid.")

    ulangi = input("Apakah Anda ingin menghitung lagi? (ya/tidak): ")
    if ulangi.lower() != "ya":
        break
