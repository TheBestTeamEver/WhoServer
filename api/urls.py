"""android_serv URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^(?P<pk>[0-9]+)/level/$', views.get_level, name='level'),
    url(r'^all/$', views.get_all, name='all'),
    url(r'^names/$', views.get_names, name='all'),
    url(r'^get_top/$', views.get_top, name='get_top'),
    url(r'^get_random_urls/$', views.get_random_urls, name='get_random_urls'),
    url(r'^authentication/$', views.authentication, name='authentication'),
    url(r'^upload/$', views.upload_file, name='upload_file'),
    url(r'^put_score/$', views.put_score, name='put_score'),
]
