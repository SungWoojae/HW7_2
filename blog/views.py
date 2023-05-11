from django.shortcuts import render,redirect,get_object_or_404
from django.utils import timezone
from .models import Blog


def home(request):
    blogs=Blog.objects.all()
    return render(request,"home.html",{"blogs":blogs})


    


def detail(request,id):
    # blog=Blog.object.get(id=id)
    blog=get_object_or_404(Blog,pk=id)
    return render(request,'detail.html',{'blog':blog})


def new(request):
    return render(request,'new.html')

def create(request):
    new_blog=Blog()
    new_blog.date=request.POST['date']
    new_blog.writer=request.POST['writer']
    new_blog.IP=request.POST['IP']
    new_blog.R=request.POST['R']
    new_blog.K=request.POST['K']
    new_blog.H=request.POST['H']
    new_blog.BB=request.POST['BB']
    new_blog.W=request.POST['W']
    new_blog.L=request.POST['L']
    new_blog.HLD=request.POST['HLD']
    new_blog.SV=request.POST['SV']
    new_blog.save()
    return redirect('detail',new_blog.id)