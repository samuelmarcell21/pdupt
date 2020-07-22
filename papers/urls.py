from django.conf.urls import url

from . import views

urlpatterns =[
	url(r'^$',views.cobak),
	url(r'^search/$',views.search),
]