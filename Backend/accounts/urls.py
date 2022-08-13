from . import views
from django.urls import path

app_name = 'accounts' 
urlpatterns = [        
    path('',views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    # path('activate/<uidb64>/<token>', views.activate, name='activate'),
    # path('resetpassword', views.reset, name='resetpassword'),
    # path('forgotpassword', views.forgot, name='forgetpassword'),      
    path('contact', views.contact, name='contact'),
    path('documentation/', views.documentation, name='documentation'),
    path('library/<str:pk>/', views.library, name='library'),
    path('profile/<str:pk>/', views.profilepage, name='profile'),
    path('portfolio/<str:pk>/', views.portfolio, name='portfolio'),
    path('community/<str:pk>/', views.community, name='community'),
    path('edit/<str:pk>/', views.edit, name='edit'),
    path('team/<str:pk>/', views.team, name='team'),
    path('start/<str:pk>/', views.start, name='start'),
    path('homepage/<str:pk>/', views.homepage, name='homepage'),
    path('important/<str:pk>/', views.important, name='important'),
    path('usingclasses/<str:pk>/', views.usingclasses, name='usingclasses'),

] 