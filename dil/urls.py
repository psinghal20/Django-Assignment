from django.conf.urls import url

from . import views

app_name = 'dil'
urlpatterns = [
	url(r'^$',views.index, name='index'),
	url(r'^register/$',views.register, name='register'),
	url(r'^logout/$',views.Logout, name='logout'),
	url(r'^(?P<username>[\w.@+-]+)/$',views.dashboard, name="dashboard"),
	url(r'^(?P<username>[\w.@+-]+)/(?P<profile>[\w.@+-]+)/red_inc/$',views.red_rose_inc, name="red_inc"),
	url(r'^(?P<username>[\w.@+-]+)/(?P<profile>[\w.@+-]+)/yellow_inc/$',views.yellow_rose_inc, name="yellow_inc"),
	url(r'^(?P<username>[\w.@+-]+)/(?P<profile>[\w.@+-]+)/$',views.visit_profile, name="visit_profile"),
]