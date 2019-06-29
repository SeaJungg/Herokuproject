from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from django.utils import timezone
from django.core.paginator import Paginator

from django.contrib.auth.models import User
from django.contrib import auth

def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                request.POST['username'], password=request.POST['password1'])
            auth.login(request, user)
            return redirect('index')
    return render(request, 'signup.html')

def login(request):
    
    return render(request, 'login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('index')
    return render(request, 'signup.html')

def index(request) :
    if request.method == 'POST': 
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None: 
            auth.login(request, user)
            return redirect('index')
        else:
            return render(request, 'index.html', {'error': 'username or password is incorrect.'})
    else:
        blog = Blog.objects
        blog_list = Blog.objects.all()
        paginator = Paginator(blog_list, 3)
        page = request.GET.get('page')
        posts = paginator.get_page(page)
        return render(request, 'index.html', {'blog' : blog, 'posts':posts})
   
    return render(request, 'index.html', {'blog' : blog, 'posts':posts})

def detail(request, blog_id) :
    blog_detail = get_object_or_404(Blog, pk = blog_id)
    return render(request, 'detail.html', {'blog' : blog_detail })
#pk : primary key 객체들의 이름 구분하는 구분자 각각의 id를 알려주는 것

def new(request) : 
    return render(request, 'new.html')

def create(request) : 
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/'+str(blog.id))