from django.urls import path
from todolist.views import get_todolist_json
from todolist.views import show_todolist
from todolist.views import register
from todolist.views import login_user
from todolist.views import logout_user
from todolist.views import add
from todolist.views import mark_finished_task
from todolist.views import delete_task

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('add/', add, name='add'),
    path('json', get_todolist_json, name='get_todolist_json'),
    path('mark-as-finished/<int:id>/', mark_finished_task, name='mark_finished_task'),
    path('delete/<int:id>/', delete_task, name='delete')
]