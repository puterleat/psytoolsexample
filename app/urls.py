from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import ListView, DetailView
from tools.views import *

urlpatterns = patterns('',


    url(r'^problems/', ListView.as_view(model=Problem) , name="problems"),
    url(r'^problem/(?P<slug>[-\w]+)/', DetailView.as_view(model=Problem) , name="problem"),
    url(r'^worksheet/(?P<slug>[-\w]+)/', DetailView.as_view(model=Worksheet) , name="worksheet"),
	url(r'^', ListView.as_view(model=Problem) , name="home"),
    url(r'^admin/', include(admin.site.urls)),
)
