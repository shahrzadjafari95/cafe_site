from django.urls import path, include
from cafe_site import views


app_name = 'cafe_site'

urlpatterns = [path('', views.index,  name='home'),
               path('contact/', views.contact, name='contact'),

]
