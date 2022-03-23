import imp
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from blogapp.forms import Add_Blog_Form
from blogapp.models import Add_Blog
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request, 'blogapp/home.html')

@login_required
def add_blog(request):
    form = Add_Blog_Form()
    if request.method == "POST":
        form = Add_Blog_Form(request.POST,request.FILES)
        if form.is_valid():
            blog_obj = form.save(commit=False)
            blog_obj.User = request.user 
            form.save()
            return redirect('/bloglist/')
    return render(request,'blogapp/addblog.html',{'form':form})

@login_required
def blog_list(request):
    obj = Add_Blog.objects.all()
    return render(request,'blogapp/bloglist.html',{'obj':obj})

@login_required
def update_blog(request,id):
    obj = Add_Blog.objects.get(pk=id)
    form = Add_Blog_Form(instance=obj)
    if request.method == 'POST':
        form = Add_Blog_Form(request.POST,request.FILES,instance=obj)
        if form.is_valid():
            form.save()
            return redirect('/bloglist/')
    return render(request, 'blogapp/addblog.html',{'form':form})

@login_required
def blog_details(request, id):
    obj = Add_Blog.objects.get(pk = id)
    return render(request,'blogapp/detailblog.html',{'obj':obj})

@login_required
def delete_blog(request,id):
    obj = Add_Blog.objects.get(pk = id)
    obj.delete()
    return redirect('/bloglist/')

def create_account(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'blogapp/createaccount.html',{'form':form})

