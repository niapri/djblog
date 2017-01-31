from django.conf.urls import url, include
from . import views

urlpatterns = [
	url(r'^order_new/$', views.order_new, name='order_new'),
	url(r'^order_new/order_confirmation/$', views.order_confirmation, name='order_confirmation'), 
]