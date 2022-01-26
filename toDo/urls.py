from django.contrib import admin
from django.urls import path

from toDoApp.views import toDoS, add_toDo, delete_toDo, done_toDo

urlpatterns = [
    path('', toDoS, name='toDoS'),
    path('add-toDo/', add_toDo, name='add_toDo'),
    path('delete-toDo/<int:pk>/', delete_toDo, name='add_toDo'),
    path('done-toDo/<int:pk>/', done_toDo, name='add_toDo'),
    path('admin/', admin.site.urls),
]
