from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from .models import TodoListItem 
from django.http import HttpResponseRedirect 
from django.urls import reverse

# Create your views here.
def index(request):
    return render(request, 'index.html')



def todoappView(request):
    all_todo_items = TodoListItem.objects.all()
    return render(request, 'todolist.html',  {'all_items':all_todo_items})


def addTodoView(request):
    new_item = TodoListItem()
    new_item.content = request.POST.get('content')
    new_item.save()
    return HttpResponseRedirect('/todo/') 


def deleteTodoView(request, id):
    y = TodoListItem.objects.get(id= id)
    y.delete()
    return HttpResponseRedirect('/todo/') 

def updateTodoView(request, id):
    todo_item = get_object_or_404(TodoListItem, id=id)

    if request.method == 'POST':
        todo_item.content = request.POST.get('content')
        todo_item.save()
        return HttpResponseRedirect(reverse('todoapp:todo')) 

    return render(request, 'update_todo.html', {'todo_item': todo_item})