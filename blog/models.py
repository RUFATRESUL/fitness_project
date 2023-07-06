from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Author(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    bio=models.CharField(max_length=40)

    def __str__(self):
        return self.user.username
    
class Tag(models.Model):
    title=models.CharField(max_length=25)

    def __str__(self):
        return self.title

class Blog(models.Model):
    title=models.CharField()
    description=models.CharField()
    content=models.CharField()
    value=models.BooleanField(default=True)
    view_count=models.IntegerField()
    image=models.ImageField(null=True,blank=True)
    create_time=models.DateField(auto_now_add=True)
    author=models.ForeignKey(Author,on_delete=models.SET_NULL,blank=True,null=True)
    tag=models.ManyToManyField(Tag)

    def __str__(self):
        return self.title
    


    

class Contact(models.Model):
    name=models.CharField()
    phone=models.CharField()
    time=models.CharField()
    email=models.EmailField()
    massage=models.TextField()
    date=models.CharField()
    message=models.TextField()

    def __str__(self):
        return self.name