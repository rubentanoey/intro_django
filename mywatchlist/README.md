# Assignment 3: Tests and Data Delivery

#### Nama    : Ruben Tanoey
#### NPM     : 2106752445
#### Kelas   : D
#### Deployed App Link    : 
- [HTML Page](https://rubentanoey-pbp2.herokuapp.com/mywatchlist/html)
- [XML Page](https://rubentanoey-pbp2.herokuapp.com/mywatchlist/xml)
- [JSON Page](https://rubentanoey-pbp2.herokuapp.com/mywatchlist/json)

___
</br>

## [1] Perbedaan antara HTML, XML, dan JSON
| No. | **HTML <br/> (Hypertext Markup Language)** | **XML <br/> (eXtensible Markup Language)** | **JSON <br/>(JavaScript Object Notation)** |
| :---: | :--- | :--- | :--- |
| 1. Definition | `HTML` merupakan bahasa markup yang membentuk struktur dari suatu page dalam web berdasarkan aturan dengan tag atau apitan tags tertentu. | `XML` merupakan bahasa markup yang menyimpan (*store*) dan membawa data, ditandai dengan sifatnya yang *self-descriptive* pasangan tags. | `JSON` merupakan notasi dengan *origin JS object notation syntax*, yang menyimpan dan membawa data, ditandai oleh pasangan nama-value.
| 2. Return object | Merespon HTTP Request dengan **struktur web page**. | Merespon HTTP Request dengan **data**. | Merespon HTTP Request dengan **data**.
| 3. Format \| Syntax | Terdiri atas *element tags*, atribut, dan konten, contoh: <br/> `<p>Example</p>` <br/> `<br/>` <br/> `<button type="next", class= btn btn-secondary>Next</button>` | Terdiri atas *root element* dan *element tags* yang *case-sensitive*, contoh: </br> `<question>` </br> `<name>Example</name>` </br> `<point>100</point>` </br> `</question>` | Terdiri atas pasangan *name-value*, dipisahkan koma, dan diapit kurung kurawal, contoh: </br> `{"Question":[` </br> `{"Name":"Example1", "Point":"100"},` </br> `{"Name":"Example2", "Point":90"},` </br> `]}`

</br>

## [2] Alasan diperlukan data delivery dalam pengimplementasian sebuah platform
Dalam pemrograman berbasis platform, `data delivery` memungkinkan perpindahan, penyimpanan, pengiriman, dan tata kelola data secara aman, terstruktur, dan mudah dari `server` ke `client`. Oleh karena itu, pemuatan data pada perbedaan platform diakomodasi dengan data delivery.

## Implementasikan *checklist* app watchlist.
1. Membuat app baru dengan nama **mywatchlist** </br>
    - Pada terminal, menjalankan perintah `python manage.py startapp mywatchlist`.
    - Menambahkan `MyWatchList` App pada `settings.py` di folder `project_django`.
    ```python
    INSTALLED_APPS = [
    ...
    'mywatchlist',
    ]
    ```
    - Menambahkan url `MyWatchList` pada `urls.py` di folder `project_django`.
    ```python
    urlpatterns = [
    ...
    path('mywatchlist/', include('mywatchlist.urls')),
    ]
    ```

2. Membuat model di file `models.py` di folder `mywatchlist`
    ```python
    from django.db import models
    from django.core.validators import MaxValueValidator, MinValueValidator

    class MyWatchList(models.Model):
        watched = models.BooleanField()
        title = models.CharField(max_length = 50)
        rating = models.FloatField(validators = [
            MaxValueValidator(5), 
            MinValueValidator(1)]
        )
        release_date = models.DateField()
        review = models.TextField()
    ```
    - watched: data 1/0 → belum/sudah ditonton
    - title: data char panjang max 50 → judul film
    - rating: float range 0-5 → rating film
    - release_date: format date → tanggal rilis film
    - review: text → review film

3. Menambahkan 10 data entry di file `initial_mywatchlist_data.json` di folder `mywatchlist > fixtures`
    ```python
    [
        {
            "model": "mywatchlist.mywatchlist",
            "pk": 1,
            "fields": {
                "watched": 1,
                "title": "Harry Potter I: Voldemort's Return",
                "rating": 4.4,
                "release_date": "2022-09-14",
                "review": "I love the fact that Voldemort comes back to life."
            }
        },
        ...
        {
            "model": "mywatchlist.mywatchlist",
            "pk": 10,
            "fields": {
                "watched": 1,
                "title": "Harry Potter X: Potter's Legacy",
                "rating": 3.3,
                "release_date": "2022-10-02",
                "review": "I hate the fact that the legacy is useless."
            }
        }
    ]
    ```

4. Mengimplementasikan sajian data
    - Pada `mywatchlist > template`, membuat `mywatchlist.html`.
        ```python
        {% extends 'base.html' %}
        {% block content %}

        <h1>My Watchlist</h1>

        <h5>Name:</h5>
        <p>{{ name }}</p>

        <h5>Student ID:</h5>
        <p>{{ student_id }}</p>

        <table>
            <tr>
                <th>Watched</th>
                <th>Title</th>
                <th>Rating</th>
                <th>Release Date</th>
                <th>Review</th>
            </tr>

            {% for watchlist in watchlists %}
            <tr>
                <td>{{watchlist.watched}}</td>
                <td>{{watchlist.title}}</td>
                <td>{{watchlist.rating}}</td>
                <td>{{watchlist.release_date}}</td>
                <td>{{watchlist.review}}</td>
            </tr>
            {% endfor %}

        </table>

        {% endblock content %}
        ```
    - Membuat fungsi pada `views.py` pada folder untuk tiga format
        - XML
        ```python
        ...
        def show_xml(request):
            data = MyWatchList.objects.all()
            return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
        ```
        - JSON
        ```python
        ...    
        def show_json(request):
            data = MyWatchList.objects.all()
            return HttpResponse(serializers.serialize("json", data), content_type="application/json")
        ```
        - HTML
        ```python
        ...
        def show_watchlist(request):
            watchlists = MyWatchList.objects.all()
            return render(
                request,
                "mywatchlist.html",
                {
                    "name": "Ruben Tanoey",
                    "student_id": "2106752445",
                    "watchlists": watchlists,
                },
            )
        ```

5.  Membuat routing agar tiap data ketiga format dapat diakses dengan URL melalui `urls.py`
    ```python
    from django.urls import path
    from mywatchlist.views import show_watchlist
    from mywatchlist.views import show_xml
    from mywatchlist.views import show_json

    app_name = 'mywatchlist'

    urlpatterns = [
        path('', show_watchlist, name='show_watchlist'),
        path('xml/', show_xml, name='show_xml'),
        path('json/', show_json, name='show_json'),
        path('html/', show_watchlist, name='show_html'),
    ]
    ```

6. Melakukan *deploy* ke `herokuapp` dengan cara:
    - Mengubah Procfile pada project_django menjadi
    ```python
    release: sh -c 'python manage.py migrate && ... && python manage.py loaddata initial_mywatchlist_data.json'
    ...
    ```
    - Membuka github.com dan menuju repositori, misalnya `https://github.com/rubentanoey/intro_django`
    - Menuju `settings > secrets > actions`
    - Klik `New repository secret`
    - untuk name `HEROKU_API_KEY`, secret API KEY dari profile herokuapp, add secret
    - untuk name `HEROKU_APP_NAME`, secret adalah nama aplikasi di herokuapp, add secret
    - Menuju `actions > workflow terakhir > Re-run all jobs`
    </br>
    Dalam kasus ini, hanya diperlukan langkah terakhir karena menggunakan repositori yang sama.

## [3] Akses ketiga link URL dengan Postman
1. http://localhost:8000/mywatchlist/html response
    ![html_postman](/README_src/html.PNG) 
2. http://localhost:8000/mywatchlist/xml response
    ![xml_postman](/README_src/xml.PNG) 
3. http://localhost:8000/mywatchlist/json response
    ![json_postman](/README_src/json.PNG) 