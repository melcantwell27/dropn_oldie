"""
URL configuration for dropn project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('classes/', dance_class_list, name='dance_class_list'),
    path('classes/<int:pk>/', dance_class_detail, name='dance_class_detail'),
    path('students/', student_list, name='student_list'),
    path('students/<int:pk>/', student_detail, name='student_detail'),
    path('studios/', studio_list, name='studio_list'),
    path('studios/<int:pk>/', studio_detail, name='studio_detail'),
    path('teachers/', teacher_list, name='teacher_list'),
    path('teachers/<int:pk>/', teacher_detail, name='teacher_detail'),
]