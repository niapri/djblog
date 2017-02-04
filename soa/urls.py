from django.conf.urls import url, include
from . import views

urlpatterns = [
	url(r'^soahome/$', views.soahome, name='soahome'),
	url(r'^check_order/$', views.check_order, name='check_order'),
	url(r'^order_new/$', views.order_new, name='order_new'),
	url(r'^order_new/order_confirmation/$', views.order_confirmation, name='order_confirmation'), 
	url(r'^delivery_queue/$', views.delivery_queue, name='delivery_queue'),
	url(r'^order_archive/$', views.order_archive, name='order_archive'),
	url(r'^order/(?P<slug>\w+)/$', views.order_detail, name='order_detail'),
]