# Hasil Praktik Big Data
## BAB 10 Brief Tour of the Standard Library
* OS Interface -> OS modul menyediakan puluhan fungsi untuk berinteraksi dengan sistem. Pastikan untuk menggunakan gaya daripada . Ini akan mencegah membayangi fungsi bawaan yang beroperasi jauh berbeda.import osfrom os import os.open() open()
  
* File Wildcard -> Glob modul menyediakan fungsi untuk membuat daftar file dari pencarian direktori wildcard:

* Argumen baris perintah -> Skrip utilitas umum sering perlu memproses argumen baris perintah. Argumen-argumen ini disimpan dalam atribut argvsys modul sebagai daftar. Sebagai contoh hasil keluaran berikut dari berjalan pada baris perintah:python demo.py one two three

* Kesalahan output dan penghentian program -> sys Modul juga memiliki atribut untuk stdin , stdout , dan stderr . Yang terakhir ini berguna untuk memancarkan peringatan dan pesan kesalahan untuk membuatnya terlihat bahkan ketika stdout telah dialihkan:

* Pencocokan pola string -> reModul menyediakan alat ekspresi reguler untuk pengolahan string yang canggih. Untuk pencocokan dan manipulasi yang kompleks, ekspresi reguler menawarkan solusi yang ringkas dan dioptimalkan:

* Matematika -> modul math memberikan akses fungsi ke c library
  ** modul random digunakan untuk membuat pilihan acak 
  ** modul statistik digunakan untuk menghitung sifat dasar statistik (mean, median, varian dll)
 
* Akses Internet -> 


