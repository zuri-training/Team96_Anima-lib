from . import views
from django.urls import path
# from django.contrib.auth import as auth_views

app_name = 'accounts' 
urlpatterns = [        
    path('',views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.signin, name='signin'),
    path('logout', views.logout, name='logout'),
    # path('activate/<uidb64>/<token>', views.activate, name='activate'),
    # path('resetpassword', views.reset, name='resetpassword'),

    # Foget Password urls
    # path('forgotpassword/', views.forgot, name='forgot'),
    # path('forgotpassword/done/', views.done, name='done'),
    # path('reset/<uidb64>/<token>/', views.confirmview, name='confirm'),
    # path('reset/done/', views.resetcomplete, name='complete'),

    path('homepage/', views.homepage, name='home'),      
    path('contact', views.contact, name='contact'),
    path('documentation/', views.documentation, name='documentation'),
    path('library/<str:pk>/', views.library, name='library'),
    path('profile/<str:pk>/', views.profilepage, name='profile'),
    path('portfolio/<str:pk>/', views.portfolio, name='portfolio'),
    path('community/<str:pk>/', views.community, name='community'),
    path('edit/<str:pk>/', views.edit, name='edit'),
    path('team/<str:pk>/', views.team, name='team'),
    path('start/<str:pk>/', views.start, name='start'),
    path('important/<str:pk>/', views.important, name='important'),
    path('usingclasses/<str:pk>/', views.usingclasses, name='usingclasses'),

] 