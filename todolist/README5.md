# Assignment 4: Web Design Using HTML, CSS, and CSS Framework

#### Nama    : Ruben Tanoey
#### NPM     : 2106752445
#### Kelas   : D
#### Deployed App Link    : 
- [Todolist (Login Required)](https://rubentanoey-pbp2.herokuapp.com/todolist)
- [Login](https://rubentanoey-pbp2.herokuapp.com/todolist/login)
- [Register](https://rubentanoey-pbp2.herokuapp.com/todolist/register)
- [Create Task](https://rubentanoey-pbp2.herokuapp.com/create-task)
- [Logout (Back to Login Page)](https://rubentanoey-pbp2.herokuapp.com/todolist/logout)

___
</br>

## [1] Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?
| No. | **Internal CSS** | **External CSS** | **Inline CSS** |
| :---: | :--- | :--- | :--- |
| Deskripsi | Didefinisikan di dalam HTML | Didefinisikan di luar HTML (File baru) | Didefinisikan di tag dalam HTML |
| 1. Manfaat | Perubahan pada Internal CSS hanya berlaku pada satu halaman saja. <\br> - Tidak perlu melakukan upload beberapa file karena HTML dan CSS berada dalam satu file. </br> - Class dan ID bisa digunakan oleh internal stylesheet. | - Ukuran file HTML akan menjadi lebih kecil dan struktur dari kode HTML jadi lebih rapi. </br> - Loading website menjadi lebih cepat. </br> - File CSS dapat digunakan di beberapa halaman website sekaligus. | - Membantu pengujian perubahan pada satu elemen. </br> - Berguna untuk memperbaiki kode dengan cepat. </br> - Proses permintaan HTTP yang lebih kecil dan proses load website akan lebih cepat. |
| 2. Kekurangan | Membuat performa website lebih lemot. Sebab, CSS yang berbeda-beda akan mengakibatkan loading ulang setiap penggantian halaman website. | Halaman akan menjadi berantakan, ketika file CSS gagal dipanggil oleh file HTML. Hal ini terjadi disebabkan karena koneksi internet yang lambat.| Tidak efisien karena Inline style CSS hanya bisa diterapkan pada satu elemen HTML. |

## [2]  Jelaskan tag HTML5 yang kamu ketahui
    - `<a>` mendefinisikan bahwa dalam tag merupakan hyperlink.
    - `<body>` mendefinisikan bagian 'isi' dari suatu website
    - `<br>` mendefinisikan line kosong baru
    - `<button>` mendifinisikan tombol
    - `<h1>` mendefinisikan judul dengan priority 1 (ukuran besar)
    - etc.

## [3]  Jelaskan CSS Selector yang kamu ketahui
- **Element Selector** : Melakukan seleksi berdasarkan pada nama elemen dengan menuliskan tag elemennya
    Misal untuk elemen `<p>`, akan didefinisikan style-nya dengan:
    ```css
    p {
        color: blue;
    }
    ```
- **Id Selector**: Melakukan seleksi berdasarkan Id dengan karakter `#id`
    Misal untuk elemen `id = "navbarNew"`, akan didefinisikan style-nya dengan:
    ```css
    #navbarNew {
        color: blue;
    }
    ```
- **Class Selector**: Melakukan seleksi berdasarkan `Class` yang telah didefinisikan sebelumnya dengan `. class`
    Misal untuk elemen `Class = "center"`, akan didefinisikan style-nya dengan:
    ```css
    .center {
        color: blue;
    }
    ```
- **Group Selector**: Melakakukan seleksi dengan penggabungan beberapa elemen yang memiliki kesamaan style
    Misal untuk elemen h1, h2, p memiliki style yang sama, didefinisikan dengan:
    ```css
    h1, h2, p {
        color: blue;
    }

    ```