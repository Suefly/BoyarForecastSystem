"""BoyarForecastSystem URL Configuration

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
from baiyu import views as baiyu
from rouya import views as rouya
from django.urls import path,include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import login.views as login
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',baiyu.index),
    path('login/',login.login,name='login'),
    path(r'baiyu/',include('baiyu.urls')),
    path(r'rouya/',include('rouya.urls')),
    path(r'huangji/',include('huangji.urls')),
    path(r'danji/',include('danji.urls')),
] + staticfiles_urlpatterns()
