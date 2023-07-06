from django.shortcuts import render
from .models import About
# Create your views here.

def home(request):
    return render(request,'home.html')

def about(request):
    abouts=About.objects.all()
    return render(request,'about.html',context={'abouts':abouts})

def service(request):
    return render(request,'service.html')

def about_view(request,id):
    about=About.objects.get(id=id)
    return render(request,'about-detail.html',context={'about':about})