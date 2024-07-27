from django.urls import path
from menu import views


app_name = 'menu'

urlpatterns = [path('main-menu/', views.index,  name='menu'),

]