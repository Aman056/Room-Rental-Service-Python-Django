"""room_services URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from room.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    path('admin/', admin.site.urls),
    path('',index,name='index'),
    path('login',login,name='login'),
    path('signup',signup,name='signup'),
    path('about',about,name='about'),
    path('home',home,name='home'),
    path('admin_home',admin_home,name='admin_home'),
    path('user_home',user_home,name='user_home'),
    path('Logout',Logout,name='Logout'),
    path('add_room',add_room,name='add_room'),
    path('contact_us',contact_us,name='contact_us'),
    path('view_contact',view_contact,name='view_contact'),
    path('delete_contact/<int:id>',delete_contact,name='delete_contact'),
    path('feedback',feedback,name='feedback'),
    path('delete_feedback/<int:id>',delete_feedback,name='delete_feedback'),
    path('add_room',add_room,name='add_room'),
    path('view_room_user',view_room_user,name='view_room_user'),
    path('view_room_admin',view_room_admin,name='view_room_admin'),
    path('delete_room/<int:id>',delete_room,name='delete_room'),
    path('edit_room/<int:id>',edit_room,name='edit_room'),



    ]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
