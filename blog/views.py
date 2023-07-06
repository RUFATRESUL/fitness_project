from django.shortcuts import render,redirect
from .models import Blog,Contact,Author,Tag

# Create your views here.

def blog(request):
    author_username=request.GET.get('author')
    authors=Author.objects.all()
    blogs=Blog.objects.all()
    tags=Tag.objects.all()
    tag_title=request.GET.get('tag')
    if author_username:
       blogs=blogs.filter(author__user__username=author_username)
    if tag_title:
        blogs=blogs.filter(tags__title=tag_title)

    return render(request,'blog.html',context={'blogs':blogs,'tags':tags,'authors':authors})

def blog_detail(request,id):
    blog=Blog.objects.get(id=id)
    return render(request,'blog-detail.html',context={'blog':blog})

def contact(request):
    return render(request,'contact.html')

def contact_view(request):
    if request.method=='GET':
        return redirect('blog:contact')
    elif request.method=='POST':
        name=request.POST.get('name')
        phone=request.POST.get('phone')
        time=request.POST.get('time')
        email=request.POST.get('email')
        massage=request.POST.get('massage')
        date=request.POST.get('date')
        message=request.POST.get('message')
        contact=Contact(name=name,phone=phone,time=time,email=email,massage=massage,date=date,message=message)
        contact.save()
        return redirect('blog:contact')
    