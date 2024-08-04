from django.urls import path
from cafe_site import views


app_name = 'cafe_site'

urlpatterns = [path('', views.index,  name='home'),
               path('contact/', views.contact, name='contact'),
               path('about/', views.about, name='about'),
]
