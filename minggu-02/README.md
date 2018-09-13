# Hasil Praktik Big Data

## BAB 2 Menggunakan Intrepeter Python
Hasil yang diperoleh setelah mengerjakan panduan dokumentasi BAB 2, adalah sebagai berikut:
* Meminjam Interpreter  
  * Melewatkan Argumen
    Ketika diketahui oleh interpreter, nama skrip dan argumen tambahan sesudahnya diubah menjadi daftar string dan ditetapkan ke variabel argv dalam modul sys. Anda dapat mengakses daftar ini dengan menjalankan sistem impor. Panjang daftar setidaknya satu; ketika tidak ada skrip dan tidak ada argumen yang diberikan, sys.argv [0] adalah string kosong. Ketika nama skrip diberikan sebagai '-' (artinya input standar), sys.argv [0] diatur ke '-'. Ketika perintah -c digunakan, sys.argv [0] diatur ke '-c'. Ketika modul -m digunakan, sys.argv [0] diatur ke nama lengkap dari modul yang ada. Opsi yang ditemukan setelah perintah -c atau modul -m tidak dikonsumsi oleh pemrosesan opsi juru bahasa Python, tetapi tetap di sys.argv untuk perintah atau modul yang akan ditangani.
  
  * Mode Interaktif
    Ketika perintah dibaca dari tty, interpreter dikatakan dalam mode interaktif. Dalam mode ini meminta perintah berikutnya      dengan prompt utama, biasanya tiga tanda lebih besar dari (>>>); untuk garis lanjutan, akan diminta dengan prompt sekunder, secara default tiga titik (...). Interpreter mencetak pesan selamat datang yang menyatakan nomor versi dan pemberitahuan hak cipta sebelum mencetak prompt pertama:
 
* Interpreter dan Lingkungannya
  Secara default, file sumber Python diperlakukan sebagai dikodekan dalam UTF-8. Dalam pengkodean itu, karakter sebagian besar bahasa di dunia dapat digunakan secara bersamaan dalam string literal, pengidentifikasi dan komentar - meskipun pustaka standar hanya menggunakan karakter ASCII untuk pengenal, sebuah konvensi yang harus diikuti oleh kode portabel apa pun. Untuk menampilkan semua karakter ini dengan benar, editor Anda harus mengenali bahwa file tersebut UTF-8, dan itu harus menggunakan font yang mendukung semua karakter dalam file.

## BAB 3 Pengaturan Informal Terhadap Python
* Menggunakan Python sebagai kalkulator
  Pada Bab ini kita belajar menggunakan perintah python. Jalankan interpreter dan tunggu prompt utama, >>>. (Tidak perlu waktu lama.)
  
  * Nomor
    Pada sub bab ini dijelaskan bagaimana cara membuat kalkulator sederhana. Dengan menggunakan operator. operator division selalu menghasilkan floating point number. Classic division (/) menghasilkan nilai float. Floor division (//) membuang bagian pecahan. operator (%) mengembalikan sisa bagi div. Operator ( * * ) adalah akar. 
    
  * String
    Selain angka, Python juga dapat memanipulasi string, yang dapat diekspresikan dalam beberapa cara. Mereka dapat diapit dengan tanda kutip tunggal ('...') atau tanda kutip ganda ("...") dengan hasil yang sama [2]. \ dapat digunakan untuk menghindari tanda kutip: 
    String dapat digabung (direkatkan) dengan operator +, dan diulangi dengan * :
    String dapat diindeks (subscript), dengan karakter pertama memiliki indeks 0. Tidak ada jenis karakter yang terpisah; karakter hanyalah string ukuran satu:
    
  * List
    Python mengetahui sejumlah tipe data majemuk, yang digunakan untuk mengelompokkan nilai-nilai lainnya. Yang paling serbaguna adalah daftar, yang dapat ditulis sebagai daftar nilai yang dipisahkan koma (item) antara tanda kurung siku. Daftar mungkin berisi item dari berbagai jenis, tetapi biasanya semua item memiliki tipe yang sama.
    
* Langkah pertama menuju pemrograman
  


## BAB 4

