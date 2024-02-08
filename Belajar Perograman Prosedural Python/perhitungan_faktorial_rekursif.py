"""
TODO:
 1. Buatlah perintah untuk meminta masukan pengguna yang bertipe data integer dan simpan pada variabel n.
 2. Buatlah fungsi rekursif bernama hitung_faktorial yang memiliki parameter n untuk mendapatkan hasil akhir perhitungan faktorial.
    2.1. Gunakan jenis linear, direct, dan tail recursion untuk membuat fungsi rekursif.
    2.2. Terapkan konsep decrement atau pengurangan satu demi satu setiap memanggil fungsi rekursif.
    2.3. Jika nilai n bernilai 0, hentikan proses rekursif dengan mengembalikan nilai 1.
    2.4. Selain itu, kembalikan nilai n dikali dengan fungsi rekursif dengan nilai decrement n.
    2.5. Simpan hasil fungsi pada variabel hasil_hitung_faktorial.
 3. Cetak pada akhir program dengan format "{n}! = {hasil_hitung_faktorial}".
"""

# Tulis kode Anda di bawah ini
# Solved 
#========================================================================================================================

# 1. Meminta masukan pengguna
n: int = int(input("Masukkan nilai untuk dihitung faktorial: "))
# 2. Fungsi rekursif
def hitung_faktorial(n: int) -> int:
    # 2.3. Hentikan proses rekursif jika n = 0 atau 1
    if n == 0 or n == 1:
        return 1
    # 2.4. Kembalikan nilai n dikali dengan rekursi
    else:
        return n * hitung_faktorial(n - 1)
# 2.5. Memanggil fungsi rekursif dan menyimpan hasilnya
hasil_hitung_faktorial: int = hitung_faktorial(n)
# 3. Menampilkan hasil
print(f"{n}! = {hasil_hitung_faktorial}.")





