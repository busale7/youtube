"""YouTube2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from Tube import views
from django.conf import settings 
from django.conf.urls.static import static 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('video/', views.clip, name='list'),
    path('channels/', views.channels, name='channel_list'),
    path('vdetail/<int:video_id>/', views.videoDetail, name="vdetail"),
    path('cdetail/<int:channel_id>/', views.channelDetail, name="detail"),
    path('update/<int:channel_id>/', views.update_channel, name="update"),
    path('vupdate/<int:video_id>/', views.update_video, name="vupdate"),
    path('create/', views.create_channel, name='create_channel'),
    path('videocreate/', views.create_video, name='video_create'),
    path('vdelete/<int:video_id>/', views.delete_video, name="vdelete"),
    path('delete/<int:channel_id>/', views.delete_channel, name="delete"),

]
