Pencarian Linier dengan Python

Pencarian Linear adalah algoritma pencarian sederhana yang melintasi list yang diberikan dan memeriksa apakah suatu elemen ada dalam list atau tidak. Itu memeriksa setiap elemen dari list sampai menemukan elemen yang sedang dicari.

Algoritma ini mudah diterapkan dan dapat digunakan untuk mencari list kecil. Namun, ini menjadi kurang efisien seiring bertambahnya ukuran list, dan dibutuhkan lebih banyak waktu untuk menelusuri seluruh list.

Algoritma

Algoritma untuk pencarian linier adalah sebagai berikut:

Lintasi elemen list demi elemen
Jika elemen ditemukan, kembalikan indeks elemen
Jika elemen tidak ditemukan, kembalikan -1
Penerapan
Berikut adalah implementasi sederhana dari pencarian linier dengan Python:

    def LinearSearch(arr, x):
        for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

Dalam implementasi ini, arr adalah list yang akan dicari, dan x adalah elemen yang akan dicari. Fungsi mengembalikan indeks elemen jika ditemukan, dan -1 jika tidak ditemukan.

Kompleksitas Waktu

Kompleksitas waktu pencarian linier adalah O(n), di mana n adalah jumlah elemen dalam list. Ini berarti bahwa waktu yang dibutuhkan untuk menelusuri list tumbuh secara linier dengan ukuran list.

Kesimpulan

Pencarian linier adalah algoritme yang sederhana dan mudah diterapkan untuk mencari melalui list kecil. Namun, ini menjadi kurang efisien seiring bertambahnya ukuran list. Ada algoritma pencarian yang lebih efisien yang tersedia untuk list besar, seperti pencarian biner dan tabel hash.
