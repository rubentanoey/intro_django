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

## [3] Jelaskan CSS Selector yang kamu ketahui
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

## [4] Jelaskan langkah implementasi
1. Menghubungkan html dengan Tailwind CSS dengan menjalankan src berikut pada `base.html`.
    ```html
        {% load static %}
        <!DOCTYPE html>
        <html lang="en">
        <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Ruben Tanoey PBP</title>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" />
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/tw-elements/dist/css/index.min.css" />
        <script src="https://cdn.tailwindcss.com"></script>
        {% block meta %} 
        {% endblock meta %}
        </head>
        <body>
        {% block content %} 
        {% endblock content %}
        <script src="https://cdn.jsdelivr.net/npm/tw-elements/dist/js/index.min.js"></script>
        </body>
        </html>
    ```
2. Mengubah style dari setiap file.html
- Pada `login.html`, `register.html` dan `add-task.html`
    - Menggunakan container `<div>` yang membuat page sebesar media untuk memberi dasar warna web dengan modifier `bg-[#]`.
    - Agar dapat responsif, menggunakan modifier `flex`.
    - Menggunakan container `<div>` yang membuat kotak yang memungkinkan untuk diisi elemen lain seperti `<button>`, `<div>`, `<input>`, etc.
    - Melakukan media query yang dapat didefinsikan dari dokumentasi tailwind, yaitu dengan `sm:`, `md:`, dan `lg`.
    - Melakukan styling lainnya seperti `text-color`, `text-size`.
- Pada `todolist.html`
    - Melakukan seperti pada `.html` lainnya.
    - Pada elemen card, digunakan modifier `hover:` agar dapat dilakukan hover pada setiap cards.
    - Agar cards dalam container dapat responsif turun ke bawah, maka dibutuhkan modifier `flex flex-warp`
    - Melakukan styling lainnya
- Melakukan deployment di HerokuApp.
