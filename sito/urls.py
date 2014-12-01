from django.conf.urls import patterns, include, url
from django.conf import settings
from sito import views
from sito.views import *
#from django.contrib import admin
urlpatterns = patterns('sito.views',
	url(r'^$', HomeView, name="home"),
	url(r'^(?P<post_id>\d+)/$', DettaglioView, name="dettaglio"),
	
)