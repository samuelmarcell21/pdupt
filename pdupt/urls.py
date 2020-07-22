from django.conf.urls import url, include
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^authors/', include('authors.urls')),
    url(r'^papers/', include('papers.urls')),
    url(r'^find/', views.find),
    url(r'^search/', views.search),
    url(r'^$', views.index),
]