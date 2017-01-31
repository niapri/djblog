from django.conf.urls import url, include
from . import views

urlpatterns = [
	url(r'^order_new/$', views.order_new, name='order_new'),
]