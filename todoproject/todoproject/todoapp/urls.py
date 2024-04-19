# urls.py
from django.urls import path
from .views import index, todoappView, addTodoView, deleteTodoView, updateTodoView

app_name = 'todoapp'

urlpatterns = [
    path('', index, name='index'),
    path('todo/', todoappView, name='todo'),
    path('addTodoItem/', addTodoView, name='addTodoItem'),  # Corrected import here
    path('deleteTodoItem/<int:id>/', deleteTodoView, name='deleteTodoItem'),
    path('updateTodoItem/<int:id>/', updateTodoView, name='updateTodoItem'),
]

