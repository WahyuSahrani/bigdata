# Rangkuman, Chapter 1 - Pandas Foundation
1. Dissecting the anatomy of a DataFrame
   * Tiga komponen - indeks, kolom, dan data (juga dikenal sebagai nilai) yang harus Anda ketahui untuk memaksimalkan potensi        penuh DataFrame.
   * Menggunakan fungsi read_csv pada movie dataset, dan menampilkan 5 baris pertama  denan head method:
   * Bagaimana itu bekerja? Pertama, pandas membaca data dari disk ke dalam memori dan kedalam DataFrame menggunakan excellent      dan fungsi read_csv. Output untuk kedua kolom dan index adalah font tebal, yang membuat mereka mudah di identifikasikan.        Sebuah DataFrame memiliki dua kapak vertical (index) dan horizontal (kolom). DataFrame data (nilai) selalu di regular font      dan sebuah pembatas komponen dari kolom atau index. Pandas menggunakan NaN (not a number).
   * Library standar python mengandung csv_module, yang bisa digunakan untuk parse dan membaca data.
 
2. Mengakses main komponen DataFrame
    * Masing-masing dari 3 komponen DataFrame index, kolom, dan data boleh diakses secara langsung dari sebuah DataFrame.
    * Masing-masing komponen ini adalah objek python ittu sendiri dengan uniq atribut dan method.
    * Bagaimana cara melakukannya:
      * Gunakan atribute DataFrame (index, kolom dan nilai)  untuk menentukan index, kolom, dan data.
      * Tampilkan masing-masing nilai komponen
      * Output tipe dari setiap komponen DataFrame.
    * Bagaimana itu bekerja, anda boleh mengakses tiga komponen utama dari DataFrame dengan index, kolom, dan nilai atributes.
    * Nama kelas yang memenuhi syarat dari objek untuk kolom variabel adalah pandas.core.indexes.base.Index. Ini dimulai dengan       nama paket, yang diikuti oleh jalur modul dan diakhiri dengan nama mengetik. Cara umum untuk merujuk objek adalah               memasukkan nama paket diikuti dengan nama jenis objek. Dalam contoh ini, kami akan mengacu kolom sebagai objek Indeks           panda.
     
3. Memahami tipe data
   * Tabel berikut berisi semua tipe data pandas, dengan ekuivalen string, dan beberapa catatan pada setiap jenis:    
   
   
