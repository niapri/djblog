from django.conf.urls import url, include
from . import views

urlpatterns = [
	url(r'^$', views.post_list, name='post_list'),
	url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
	url(r'^post/new/$', views.post_new, name='post_new'),
	url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name="post_edit"),
	url(r'^projects/$', views.projects, name='projects'),
	url(r'^contact/$', views.contact, name='contact'),
	url(r'^contact/thankyou/$', views.thankyou, name='thankyou'),
	url(r'^pdftest/$', views.pdftest, name='pdftest'),
	url(r'', include('soa.urls')),
	url(r'', include('resales.urls')),
	url(r'', include('taskmanager.urls')),
]