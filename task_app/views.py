from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from task_app.forms import User_register_form, Task_form
from task_app.models import Task
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def home(request):
    return render(request, 'home.html')

def dash(request):
    return render(request, "dash.html")

def user_dash(request):
    return render(request,'user_dash.html')

def user_register(request):
    user_register_form_object = User_register_form()
    if request.method == 'POST':
        user_register_form_object = User_register_form(request.POST)
        if user_register_form_object.is_valid():
            user_register_form_object.save()
            return redirect('/')
    return render(request,'user_register.html',{'user_register_form_object':user_register_form_object})


def login_view(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user_object = authenticate(request, username = username, password = password)
    if user_object is not None:
        login(request, user_object)
        return redirect('user_dash')
    return render(request,'login.html')

def logout_view(request):
    logout(request)
    return redirect('login_view')

@login_required(login_url = 'login_view')
def create_task(request):
    task_form_object = Task_form()
    if request.method == 'POST':
        task_form_object = Task_form(request.POST)
        if task_form_object.is_valid():
            task_object = task_form_object.save(commit = False)
            task_object.user = request.user
            task_object.save()
            return redirect('user_dash')
    return render(request,'create_task.html',{'task_form_object':task_form_object})

def view_my_tasks(request):
    task_objects = Task.objects.filter(user = request.user)
    paginator = Paginator(task_objects, 1)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, 'view_my_tasks.html',{'page_obj':page_obj})

def view_all_tasks(request):
    query = request.GET.get('query', '')
    task_objects = Task.objects.filter(title__icontains=query) | Task.objects.filter(description__icontains=query)
    paginator = Paginator(task_objects, 1)  # Show 25 contacts per page.
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, 'view_all_tasks.html',{'page_obj':page_obj})

@login_required(login_url = 'login_view')
def update_task(request, id):
    task_object = Task.objects.get(id = id)
    task_form_object = Task_form(instance = task_object)
    if request.method == 'POST':
        task_form_object = Task_form(request.POST,request.FILES,instance = task_object)
        if task_form_object.is_valid():
            task_form_object.save()
            return redirect('view_my_tasks')
    return render(request, 'update_task.html',{'task_form_object':task_form_object})

@login_required(login_url = 'login_view')
def delete_task(request,id):
    task_object = Task.objects.get(id=id)
    task_object.delete()
    return redirect('view_my_tasks')

def mark_task_complete(request, id):
    task_object = Task.objects.get(id = id)
    task_object.completed = True
    task_object.save()
    return redirect('view_my_tasks')

def mark_task_not_completed(request, id):
    task_object = Task.objects.get(id = id)
    task_object.completed = False
    task_object.save()
    return redirect('view_my_tasks')

