"""mysite URL Configuration

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
#from django.contrib import admin
#from django.urls import path
from django.conf.urls import url
#from django.views.generic import ListView
from .views import Index , changeStatus , deleteAsset, EditAsset
#from .views import httpsResponse

urlpatterns = [
    url(r'^edit_asset/$', EditAsset.as_view(), name='edit-asset'),
    url(r'^delete_asset/$', deleteAsset.as_view(), name='delete-asset'),
    url(r'^change_status/$', changeStatus.as_view(), name='change-status'),
    url(r'', Index.as_view(), name='index'),
]