# Assignment 6: Javascript and AJAX

#### Nama    : Ruben Tanoey
#### NPM     : 2106752445
#### Kelas   : D
#### Deployed App Link    : 
- [Todolist (Login Required)](https://rubentanoey-pbp2.herokuapp.com/todolist)
- [Login](https://rubentanoey-pbp2.herokuapp.com/todolist/login)
- [Register](https://rubentanoey-pbp2.herokuapp.com/todolist/register)
- [Create Task](https://rubentanoey-pbp2.herokuapp.com/add)
- [Logout (Back to Login Page)](https://rubentanoey-pbp2.herokuapp.com/todolist/logout)
- [Logout (Back to Login Page)](https://rubentanoey-pbp2.herokuapp.com/todolist/json)

___
</br>

## [1] Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.
| **Sync Programming** | **Async Programming** |
| :---: | :--- |
| Dalam `synchronous programming`, tasks dijalankan sekali pada suatu waktu dan hanya ketika satu sebelumnya selesai, selanjutnya unblocked. Perlu **menunggu** untuk penyelesaian satu task, ke task lainnya. | Dalam `asynchronous programming`, tasks dapat dilakukan secara berkelanjutan **tanpa harus menunggu** task sebelumnya selesai. Dengan cara ini, multiple request dapat di-handle dalam suatu waktu. |

## [2] Jelaskan *Event-Driven Programming Paradigm*, sebutkan salah satu contoh penerapannya pada tugas ini.
-   *Event driven programming* merupakan pendekatan yang membuat program berjalan karena suatu *event*. Event tersebut dapat di-*trigger* atau dipicu aksi yang dilakukan user, baik itu mengeklik `button`, `linked-text`, etc.
-   Contoh penerapannya:
    ```javascript
    const openModal = e => {
        e.preventDefault(); // prevent refresh
        console.log('test')
        $("#createTaskModal").removeClass("hidden");
    };
    ...
    $("#openingModal").click(openModal);
    ...
    <button id="openingModal">Add Task</button>
    ```
    Jika button ber-id `openingModal` di-klik (event), maka yang akan muncul adalah modal Add Task.

## [3] Jelaskan penerapan asynchronous programming pada AJAX.
-   AJAX secara terus-menerus menginisasi request `JavaScript` dan `XML` yang mudah dilakukan `parsing`. Website load-time menjadi tereduksi sehingga performa dari web pun meningkat. Dengan AJAX yang *running over* HTTP Protocol, AJAX memperoleh akses ke semua request, termasuk HEAD yang bisa memperoleh data secara *seamless* secara real-time terbarui.

## [4] Implementasi *checklist*.
1. AJAX GET
-   Buatlah view baru yang mengembalikan seluruh data task dalam bentuk JSON.
    ```python
    def get_todolist_json(request):
    task = Task.objects.filter(user=request.user)
    return HttpResponse(
        serializers.serialize('json', task),
        content_type = 'application/json' 
        )
    ```
-   Buatlah *path* `/todolist/json` yang mengarah ke view yang baru kamu buat.
    ```python
    path('json', get_todolist_json, name='get_todolist_json'),
    ```
-   Lakukan pengambilan task menggunakan AJAX GET.
    ```javascript
    const conquerTask = () => {
        $.get("{% url 'todolist:get_todolist_json' %}", data => {

            $.each(data, (i, value) => {
                $("#allTodolist").append(card(value));
            });
        });
    };
    ```

2. AJAX POST
-   Buatlah sebuah tombol `Add Task` yang membuka sebuah modal dengan form untuk menambahkan task.
    ```javascript
    <button class="text-lg text-white items-center justify-center bg-[#04285A] py-1 px-5 rounded-md hover:shadow-lg hover:shadow-[#F4FCFF]" id="openingModal">Add Task</button>    
    ```
-   Buatlah `view` baru untuk menambahkan task baru ke dalam *database*.
    ```python
    def add(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        task = Task.objects.create(
            user=request.user,
            title=title,
            description=description,
            date=datetime.datetime.today(),
        )
        return JsonResponse(
            {
                "pk": task.id,
                "fields": {
                    "title": task.title,
                    "description": task.description,
                    "is_finished": task.is_finished,
                    "date": task.date,
                },
            },
            status=200,
        )
    ```
-   Hubungkan form yang telah kamu buat di dalam modal
    Copy form yang telah dibuat ke dalam `todolist.html` dan menjadikan button AddTask terhubung dengan fungsi
    `const openModal ...`, `$("#newForm").submit(e => { ...`, dan `$("#openingModal").click(openModal);`.
-   Tutup modal setelah penambahan task telah berhasil dilakukan.
    Melengkapi `todolist.html` dengan menambahkan `const closeModal ...` dan `$("#closingmodal").click(closeModal);`
-   Lakukan *refresh* pada halaman utama secara asinkronus untuk menampilkan list terbaru tanpa reload seluruh page.
