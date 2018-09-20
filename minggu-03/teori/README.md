# Hasil Praktik Big Data 

## BAB 5 (STRUKTUR DATA)
* Lebih Lanjut Tentang Daftar
  * count
    count digunakan untuk menampilkan jumlah elemen di dalam array. Seperti pada contoh, ada variabel berisi data buah-buahan, ketika saya mengetikan perintah fruits.count('apple') maka yang akan di tampilkan adalah angka 2. karena apple jumlah nya ada 2
    
  * index
    index digunakan untuk menampilkan elemen di dalam array. Seperti pada contoh, ada variabel berisi data buah-buahan, ketika saya mengetikan perintah fruits.index('banana') maka yang akan di tampilkan adalah angka 3. karena banana ada pada index ke 3
    
  * reverse
    reverse digunakan untuk membalikan unsur-unsur daftar.
  
  * sort
    sort digunakan untuk mengurutkan elemen. ketika saya mengetikan perintah fruits.sort() maka hasilnya adalah data di dalam array diurutkan sesuai abjad
    
  * pop
    pop digunakan untuk menghapus elemen yang paling terakhir.
 
* Menggunakan Daftar sebagai tumpukan 
  * append digunakan untuk menambahkan elemen ke bagian atas tumpukan. sebelumnya saya mendefinisikan variabel dengan nama stack yang berisi item 3, 4, 5. kemudian saya mengetikan stack.append (6) dan stack.append(7) maka item 6 dan 7 dimasukan ke dalam daftar elemen stack.
  
  * pop digunakan untuk mengambil item dari bagian atas tumpukan. pop merupakan kebalikan dari append.  ketika saya mengetikan stack.pop() maka item terakhir dari daftar akan terhapus.
  
* Menggunakan daftar sebagai antrian
  * untuk mengimplementasikan antrian, gunakan collections.deque yang dirancang agar memiliki penambahan cepat dan muncul dari kedua ujungnya. seperti yang sudah saya praktikan, membuat antrian yang berisi 3 item yaitu Eric, Jhon, dan Michael. kemudian menambahkan 2 item dengan nama Terry dan Graham dengan perintah append. kemudian implementasikan perintah popleft untuk menambahkan ke daftar. maka item pertama dan kedua akan hilang dan akan ditambahkan 2 item baru yaitu Terry dan Graham.
    
* Daftar Bersarang

* Pernyataan del
  * pernyataan del dapat digunakan untuk menghapus irisan dari daftar atau menghapus seluruh daftar. ketika saya menambahkan variabel a yang berisi beberapa item, a = [-1, 1, 66.25, 333, 333, 1234.5] ketika saya mengetikan perintah de a[0] maka item pertama di dalam daftar akan hilang. jika ingin menghapus seluruh item dengan mengetikan perintah del a.
  
* Tuples dan urutan
  tuples sering digunakan dalam situasi yang berbeda dan untuk tujuan yang berbeda. Tuples tidak dapt diubah, dan biasanya mengandung urutan elemen heterogen yang diakses melalui pembongkaran

* Set
  Satu set adalah koleksi berurutan tanpa elemen duplikat. Penggunaan dasar termasuk pengujian keanggortanan dan menghilangkan entri duplikat.  ketika saya mengetikan basket = 'apple', 'orange', 'apple', 'pear', 'orange', 'banana'} enter kemudian ketikan print(basket) maka data yang duplikat akan hilang.

* Teknik Looping
  enumerate() digunakan untuk mengulang melalui urutan, indek posisi dan nilai yang terkait dapat diambil pada saat yang sama. untuk mengulang lebih dari dua atau lebih urutan pada saat yang sama, entri dapat dipasangkan dengan zip(). Untuk mengulang urutan secara terbalik, pertama-tama tentukan urutan dalam arah maju dan kemudian panggil reversed() fungsi trsebut. gunakan sorted()fungsi yang mengembalikan daftar yang diurutkan baru saat meninggalkan sumber tidak berubah.


  
 
  
  

   
 
    
