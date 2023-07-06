from django.db import models

# Create your models here.
class About(models.Model):
    title=models.CharField()
    description=models.CharField()
    image=models.ImageField(null=True,blank=True)
    count_view=models.IntegerField()
    show=models.BooleanField(default=True,)
    create_time=models.DateField( auto_now_add=True)

    def __str__(self):
        return self.title

