# Assignment 2: Models View Template Django

Nama    : Ruben Tanoey
#### NPM     : 2106752445
Kelas   : D
#### Link    : [KatalogPage](https://rubentanoey-pbp2.herokuapp.com/katalog/)

___

## Bagan MVT Django
![diagram](/README_src/MVT_django.png)
**Komponen utama Django**  : URL, View, Model, Template.
#### URL
URL berisi semua URL yang akan **di-request user** melalui browser. Setiap URL berbeda akan membuka page yang berbeda dalam aplikasi web. Setelah menerima request, Django akan mencari respon yang paling tepat berdasarkan `urls.py` untuk request tersebut sehingga konsep MVT pada Django dijalankan.
#### View
View adalah **respon yang berkorespondensi dengan request** yang diberikan user. Misal Django mencari rubentanoey-pbp2.herokuapp.com/katalog/, maka Django akan mencari `views.py` yang tepat dari request yang ada. View melakukan *fetch* data dari `models.py` dan me-*render* `template`.
#### Model
Model merupakan tabel basis data. Sebab itu, `models.py` adalah sebuah class python yang merujuk pada suatu basis data. Model mencakup data-data yang diperlukan untuk kemudian di-fetch oleh `views.py`.
#### Template
Template merupakan komponen 'front-end' dari suatu aplikasi Django application. Folder `template` ini berisi output HTML dari aplikasi web dengan informasi yang dinamis. Untuk me-*generate* HTML secara dinamis, Django menggunakan DTL (Django Template Language) dengan static HTML. Penggunaan DTL Django menunjukkan data dari `models.py` secara dinamis.


## Virtual Environment
#### Mengapa virtual environment digunakan? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
**Virtual environment** adalah alat untuk menjaga semua dependency yang diperlukan untuk masing-masing project berbeda menjadi terpisah. Pemisahan ini dilakukan agar kebutuhan setiap project konsisten dengan membuat lingkungan virtual yang terisolasi. Selain itu, penggunaan virtual environment akan sangat berguna dalam project kolaboratif yang memerlukan dependency-dependency tertentu. <br />
Tanpa menggunakan virtual environment, Django akan **bisa tetap berjalan**. Akan tetapi, semua dependency berbeda untuk setiap projectnya perlu di-install kembali **secara global** mengakibatkan mobilitas developer melambat.

## Implementasi pada Project
#### [1] Membuat sebuah fungsi pada views.py yang dapat melakukan pengambilan data dari model dan dikembalikan ke dalam sebuah HTML.
1.  Membuat `CatalogItem` pada `models.py`.
```python
    ...
    class CatalogItem(models.Model):
        item_name = models.CharField(max_length=255)
        item_price = models.BigIntegerField()
        item_stock = models.IntegerField()
        description = models.TextField()
        rating = models.IntegerField()
        item_url = models.URLField()
```
2.  Membuat fungsi `show_catalog` pada `views.py`.
```python
    ...
    from katalog.models import CatalogItem

    def show_catalog(request):
        catalog = CatalogItem.objects.all()
        return render(
            request,
            "katalog.html",
            {
                "name": "Ruben Tanoey",
                "student_id": "2106752445",
                "catalogs": catalog,
            },
        )
```
#### [2] Membuat sebuah routing untuk memetakan fungsi yang telah kamu buat pada views.py.
1. Mengimplementasi routing pada `urls.py` di `project_django`.
```python
    urlpatterns = [
        ...
        path('katalog/', include('katalog.urls')),
    ]
```
#### [3] Memetakan data yang didapatkan ke dalam HTML dengan sintaks dari Django untuk pemetaan data template.
3. Membuat html file sebagai template di `katalog/template`
```python
    ...
    <table>
        ...
        {% for catalog in catalogs %}
        <tr>
            <td>{{catalog.item_name}}</td>
            <td>{{catalog.item_price}}</td>
            <td>{{catalog.item_stock}}</td>
            <td>{{catalog.rating}}</td>
            <td>{{catalog.description}}</td>
            <td>{{catalog.item_url}}</td>
        </tr>
        {% endfor %}

    </table>

    {% endblock content %}
```
#### [4] Melakukan deployment ke Heroku terhadap aplikasi yang sudah kamu buat.
1. Menambah direktori `'katalog'` pada `settings.py` di `project_django`.
```python
        INSTALLED_APPS = [
        ...
        'katalog',
    ]
```
2. Membuat `app_name` dan `urlpatterns` agar dapat memanggil fungsi `show_catalog`.
```python
    from katalog.views import show_catalog

    app_name = 'katalog'

    urlpatterns = [
        path('', show_catalog, name='show_catalog'),
    ]
```
3. Melakukan `python manage.py loaddata initial_catalog_data.json` untuk meload data.
4. Melakukan *deploy* ke `herokuapp` dengan cara:
    - Membuka github.com dan menuju repositori, misalnya `https://github.com/rubentanoey/mvt_django`
    - Menuju `settings > secrets > actions`
    - Klik `New repository secret`
    - untuk name `HEROKU_API_KEY`, secret API KEY dari profile herokuapp, add secret
    - untuk name `HEROKU_APP_NAME`, secret adalah nama aplikasi di herokuapp, add secret
    - Menuju `actions > workflow terakhir > Re-run all jobs`
5. Selesai, herokuapp bisa dibuka, misalnya di [KatalogPage](https://rubentanoey-pbp2.herokuapp.com/katalog/).