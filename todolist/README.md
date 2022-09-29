# Assignment 4: Implementasi Form dan Autentikasi dengan Django

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

## [1] Apa kegunaan `{% csrf_token %}` pada elemen `<form>`? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>?
- *Cross-Site Request Forgery* (CSRF) merupakan serangan keamanan yang menyebabkan web mengalami kejadian yang tidak diharapkan pada situs tepercaya bahkan ketika pengguna terautentifikasi. Serangan CRSF bekerja karena `request` browser secara otomatis mengambil semua `cookies` termasuk session.
- Pada `<form>`, elemen `{% csrf_token %}` diperlukan untuk memverifikasi apakah user yang terautentifikasi betul-betul user yang valid. Ketika ada request yang dilakukan client, komponen `{% csrf_token %}` pada elemen `<form>` harus memverifikasi validitas dari token yang di-request yang kemudian dibandingkan dengan token yang ditemukan pada `session user`. Apabila token tidak ditemukan dalam request atau value token yang diberikan tidak cocok, maka request dapat `dibatalkan` atau `aborted` secara langsung.
- Dengan demikian, apabila potongan tersebut tidak ditemukan, maka akan rentan terjadi serangan CSRF yang dijelaskan sebelumnya.

## [2] Apakah kita dapat membuat elemen `<form>` secara manual (tanpa menggunakan generator seperti `{{ form.as_table }}`)? Jelaskan secara gambaran besar bagaimana cara membuat `<form>` secara manual?
- Elemen `<form>` dapat dibuat secara manual tanpa `{{ form.as_table }}`.
- Dengan penggunaan elemen `<table>`, pembentukan form dapat terjadi dengan implementasi `<tr></tr>`, `<th></th>`, dan `<td></td>` untuk memuat setiap barisnya ke dalam barisan. Selain itu, elemen `<button></button>` dapat digunakan untuk melakukan submisi form.

## [3] Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.
- Ketika user melakukan submit, `POST` akan di-*request* ke server dan server akan melalukan pemanggilan dari fungsi di `views.py`.
- Method tersebut akan memperoleh data yang disubmit, misalnya dicek pada `if request.method == 'POST':` dan melakukan penyimpanan objek baru dengan `form = TodolistForm(request.POST)` dan `new_task.user = request.user`, `new_task.save()`. Setelah fungsi dilakukan, maka data yang diperoleh dapat muncul setiap iterasi di `todolist.html`.

## [4] Jelaskan implementasi checklist.
1. Membuat suatu aplikasi baru dengan `python manage.py startapp todolist`
2. Menambah path todolist
    ```python
    urlpatterns = [
    ...
    path('todolist/', include('todolist.urls')),
    ]
    ```
3. Membuat sebuah model Task
    ```python
    from django.contrib.auth.models import User

    class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True, blank = True)
    date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length = 255)
    description = models.TextField()
    is_finished = models.BooleanField(default = False)
    ```
4. Membuat class pada `forms.py` dan fungsi pada `views.py` serta tampilannya pada `*.html`.
    - `todolist.html`
        ```python
        {% extends 'base.html' %}
        {% block content %}
        <div class="todolist-container">
            
            <div class="header">
                <h2>{{user}}'s To Do</h2>
            </div>

            <div class="todolist">
                <table class="listtable">
                    <thead>
                        <tr>
                            <th>Finished</th>
                            <th>Task</th>
                            <th>Description</th>
                            <th>Created</th>
                            <th>Status</th>
                            <th>Delete</th>
                        </tr>
                    </thead>
                    {% for task in todolist %}
                    <tbody>
                        <tr>
                            <th>
                                <input class='todolist-check' 
                                    type="checkbox" 
                                    id='{{task.id}}' 
                                    value= '{{task.ud}'
                                    name="finishbtn"
                                    {% if task.is_finished %} checked {% endif %}
                                    onchange="location.href='{% url 'todolist:mark_finished_task' task.id %}'"  
                                />                  
                                <!-- <span class="checkmark"></span> -->
                            </th>
                            <th>{{task.title}}</th>
                            <th>{{task.description}}</th>
                            <th>{{task.date}}</th>
                            {% if task.is_finished == True %}
                                <td style="text-align: center; color: green">Finished</td>
                            {% else %}
                                <td style="text-align: center; color: gold">In Progress</td>
                            {% endif %}
                            <th>
                                <button class="btn" style="color: red;" ><a href="{% url 'todolist:delete' task.id %}">Delete</a></button>
                            </th>

                        </tr>
                    </tbody>
                    
                    {% endfor %}
                </table>
            </div>

            <p><a href="{% url 'todolist:add_task' %}">Add Task</a></p>
            <button><a href="{% url 'todolist:logout' %}">Logout</a></button>
        </div>

        {% endblock content %}
        ```
    - `views.py`
        ```python
        def register(request):
            form = UserCreationForm()

            if request.method == "POST":
                form = UserCreationForm(request.POST)
                if form.is_valid():
                    form.save()
                    messages.success(request, 'Akun telah berhasil dibuat!')
                    return redirect('todolist:login')
            
            context = {'form':form}
            return render(request, 'register.html', context)

        def login_user(request):
            if request.method == 'POST':
                username = request.POST.get('username')
                password = request.POST.get('password')
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user) # melakukan login terlebih dahulu
                    response = HttpResponseRedirect(reverse("todolist:show_todolist")) # membuat response
                    response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
                    return response
                else:
                    messages.info(request, 'Username atau Password salah!')
            context = {}
            return render(request, 'login.html', context)

        def logout_user(request):
            logout(request)
            response = HttpResponseRedirect(reverse('todolist:login'))
            response.delete_cookie('last_login')
            return response

        @login_required(login_url = '/todolist/login/')
        def show_todolist(request):
            todolist_objects = Task.objects.filter(user=request.user)
            context = {"todolist": todolist_objects, "username": request.user}
            return render(request, "todolist.html", context)

        @login_required(login_url = '/todolist/login/')
        def add_task(request):
            user_name = User.objects.get(username=request.user)    
            form = TodolistForm()
            new_task = None
            if request.method == 'POST':
                form = TodolistForm(request.POST)
                if form.is_valid():
                    new_task = form.save(commit=False)
                    new_task.user = request.user
                    new_task.save()
                return HttpResponseRedirect(reverse("todolist:show_todolist"))
            context = {'form': form}
            return render(request, 'add_task.html', context)

        @login_required(login_url = "/todolist/login/")
        def mark_finished_task(request, id):
            task = Task.objects.get(user = request.user, id=id)
            task.is_finished = not (task.is_finished)
            task.save(update_fields = ["is_finished"])
            return HttpResponseRedirect(reverse("todolist:show_todolist"))
            
        @login_required(login_url = "/todolist/login/")
        def delete_task(request, id):
            task = Task.objects.get(user=request.user, id = id)
            task.delete()
            return HttpResponseRedirect(reverse("todolist:show_todolist"))
        ```   
5. Pembuatan halaman form pada `forms.py` dan tampilan menambah task pada `add_task.html`
    - `forms.py`
        ```python
        class TodolistForm(forms.ModelForm):
        title= forms.CharField(widget= forms.TextInput(attrs={'size':'50'}))
        description= forms.CharField(widget=forms.Textarea(attrs={'size': '100'}))

        class Meta:
            model = Task
            fields = ('title', 'description')
        ```
    - `add_task.html`
        ```python
        {% extends 'base.html' %}
        {% block content %}

        <div class="new container">
            <div class="header">
                <h3>Task Form</h3>
            </div>
                <form method="POST" action="" id="newForm">
                    {% csrf_token %}
                    <table>
                        {{form.as_table}}
                        <tr>  
                            <td></td>
                            <td><input type="submit" name="submit" value="Create Task"/></td>
                        </tr>  
                        <tr>
                            <td></td>
                            <td><input type="button" value="Go back!" onclick="history.back()"></td>
                        </tr>
                    </table>
                </form>
        </div>
        {% endblock content %}
        ```
5. Membuat routing pada `urls.py` pada folder `todolist`.
```python
from django.urls import path
from todolist.views import show_todolist
from todolist.views import register
from todolist.views import login_user
from todolist.views import logout_user
from todolist.views import add_task
from todolist.views import mark_finished_task
from todolist.views import delete_task

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', add_task, name='add_task'),
    path('mark-as-finished/<int:id>/', mark_finished_task, name='mark_finished_task'),
    path('delete/<int:id>/', delete_task, name='delete')
]
```
6. Melakukan *deploy* ke `herokuapp` dengan cara:
    - Melakukan git add, commit, dan push.
    - Menuju `actions > workflow terakhir > Re-run all jobs`
    </br>

7. Membuat dua akun pengguna dan tiga dummy data menggunakan model Task pada akun masing-masing di situs web Heroku.
- ![Ruben's Task](/README_src/ruben_task.jpg) 
- ![Dadin's Task](/README_src/dadin_task.jpg) 
    