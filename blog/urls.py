from django.urls import path
from blog import views
urlpatterns = [
    #path('admin/', admin.site.urls),
    path('login/', views.login_view, name='login'),
    path('', views.signup, name='signup'),
    path('home/', views.home),
    #path('', views.home, name='home'),
    path('mypost/', views.myPost),
    path('newpost/', views.newPost),
    path('signout/', views.signOut)


]
