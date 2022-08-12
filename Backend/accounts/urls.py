from . import views
from django.urls import path

app_name = 'accounts' 
urlpatterns = [        
    path('',views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path('resetpassword/', views.reset, name='resetpassword'),
    path('forgotpassword/', views.forgot, name='forgetpassword'),      
    path('contact', views.contact, name='contact'),
    path('documentation/', views.documentation, name='documentation'),
] 