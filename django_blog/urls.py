from django.contrib import admin
from django.urls import path
from blog import views  


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login_view, name='login'),
    path('', views.signup, name='signup'),
    path('home/', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('mypost/', views.myPost, name='mypost'),
    path('newpost/', views.newPost, name='newpost'),
    path('signout/', views.signOut, name='signout'),


  
]
