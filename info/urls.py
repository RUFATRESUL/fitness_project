from django.urls import path
from . import views
app_name='info'
urlpatterns = [
   path('',views.home,name='home'),
   path('about/',views.about,name='about'),
   path('service/',views.service,name='service'),
   path('about/<int:id>/',views.about_view,name='about-detail')
]
