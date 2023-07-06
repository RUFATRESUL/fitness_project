from django.urls import path
from . import views
app_name='blog'
urlpatterns = [
    path('blog/',views.blog,name='blog'),
    path('contact/',views.contact,name='contact'),
    path('contact_view/',views.contact_view,name='contact_view'),
    path('blog/<int:id>/',views.blog_detail,name='blog-detail')
]
