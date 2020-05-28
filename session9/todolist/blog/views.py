from django.shortcuts import render, redirect
from .models import Todo, Comment
from datetime import datetime
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    todos = Todo.objects.all().order_by('deadline')
    now = datetime.now()
    context = {
        'todos' : todos,
        }
    return render(request, 'home.html', context)

@login_required(login_url='/regiatration/login')
def new(request):
    if request.method == 'POST':
        new_todo = Todo.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
            deadline = request.POST['deadline'],
            author = request.user
        )
        return redirect('detail', new_todo.pk)
    return render(request, 'new.html')

def detail(request, todo_pk):
    todo = Todo.objects.get(pk = todo_pk)

    if request.method == "POST":
            Comment.objects.create(
                post = todo,
                content = request.POST['content'],
                author = request.user
            )
            return redirect('detail', todo_pk)

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

def delete_comment(request, todo_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect('detail', todo_pk)

def signup(request):
    if (request.method == "POST"):
        found_user = User.objects.filter(username=request.POST['username'])
        if (len(found_user) > 0):
            error = 'username이 이미 존재합니다'
            return render(request, 'registration/signup.html', { 'error' : error})

        new_user = User.objects.create(
            username = request.POST['username'],
            password = request.POST['password']
        )
        auth.login(request, new_user, backend='django.contrib.auth.backends.ModelBackend')
        return redirect('home')

    return render(request,'registration/signup.html')

def login(request):
    if (request.method == "POST"):
        found_user = auth.authenticate(
            username = request.POST['username'],
            password = request.POST['password'],
        )
        if (found_user is None):
            error = '아이디 혹은 비밀번호가 틀렸습니다'
            return render(request, 'registration/login.html', {'error' : error })

        auth.login(request, found_user, backend='django.contrib.auth.backends.ModelBackend')
        return redirect(request.GET.get('next', '/'))
    
    return render(request, 'registration/login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')