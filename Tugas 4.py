# Inisialisasi Matriks A dan B
DEFINISIKAN Orde_A sebagai [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
DEFINISIKAN Orde_B sebagai [[8, 14, -6], [12, 7, 4], [-11, 3, 21]]

# Memeriksa orde matriks
JIKA panjang(Orde_A) != 3 ATAU panjang(Orde_B) != 3 ATAU panjang(Orde_A[0]) != 3 ATAU panjang(Orde_B[0]) != 3 THEN
    TAMPILKAN "Matriks tidak dapat dikalikan, pastikan kedua matriks berordo 3x3."
    KELUAR

# Inisialisasi matriks hasil
DEFINISIKAN hasil sebagai matriks 3x3 dengan nilai awal 0

# Mengalikan matriks A dan B
UNTUK i DARI 0 HINGGA 2 Lakukan
    UNTUK j DARI 0 HINGGA 2 Lakukan
        hasil[i][j] = 0
        UNTUK k DARI 0 HINGGA 2 Lakukan
            hasil[i][j] += Orde_A[i][k] * Orde_B[k][j]

# Menampilkan hasil perkalian
TAMPILKAN "Hasil perkalian matriks A dan B adalah:"
UNTUK setiap baris dalam hasil Lakukan
    TAMPILKAN baris

TAMPILKAN "Selesai"
