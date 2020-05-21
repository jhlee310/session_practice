from django.shortcuts import render, redirect
from .models import Todo
from datetime import datetime

# Create your views here.
def home(request):
    todos = Todo.objects.all().order_by('deadline')
    now = datetime.now()
    context = {
        'todos' : todos,
        }
    return render(request, 'home.html', context)

def new(request):
    if request.method == 'POST':
        new_todo = Todo.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
            deadline = request.POST['deadline'],
        )
        return redirect('detail', new_todo.pk)
    return render(request, 'new.html')

def detail(request, todo_pk):
    todo = Todo.objects.get(pk = todo_pk)
    context = {'todo' : todo}
    return render(request, 'detail.html', context)

def edit(request, todo_pk):
    todo = Todo.objects.get(pk=todo_pk)

    if request.method == "POST":
        Todo.objects.filter(pk=todo_pk).update(
            title = request.POST['title'],
            content = request.POST['content'],
            deadline = request.POST['deadline'],
        )
        return redirect("detail", todo_pk)
    
    context = {'todo' : todo}
    return render(request, 'edit.html', context)

def delete(request, todo_pk):
    todo = Todo.objects.get(pk=todo_pk)
    todo.delete()
    
    return redirect('home')