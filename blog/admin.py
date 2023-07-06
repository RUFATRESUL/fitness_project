from django.contrib import admin
from .models import Blog,Contact,Author,Tag
# Register your models here.
admin.site.register(Blog)
admin.site.register(Contact)
admin.site.register(Author)
admin.site.register(Tag)
