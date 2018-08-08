"""smupro URL Configuration

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
from django.urls import include, path
from multiplex.views import HallList, cinema_list, CinemaDetail
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('halls/', HallList.as_view(), name='hall-list'),
    path('cinemas/', cinema_list, name='cinema-list'),
    path('cinemas/<int:pk>/', CinemaDetail.as_view(), name='cinema-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)