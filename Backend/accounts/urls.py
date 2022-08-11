from . import views
from django.urls import path

app_name = 'accounts' 
urlpatterns = [        
    path('',views.index, name='index'),
    path('register', views.register, name='register'),
    path('login', views.login_user, name='login'),
    path('register', views.register, name='register'),       
    path('contact', views.contact, name='contact'),
] 