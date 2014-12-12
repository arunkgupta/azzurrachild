from django.conf.urls import patterns, include, url
from django.conf import settings
from sito import views
from sito.views import *
from django.conf.urls.i18n import i18n_patterns


urlpatterns = patterns('sito.views',
	url(r'^$', HomeView, name="home"),
	url(r'^progetti/$', ProgettiView, name="progetti"),
	url(r'^news/$', NewsView, name="news"),
	url(r'^chisiamo/$', ChisiamoView, name="chisiamo"),
	url(r'^sostienici/$', SostieniciView, name="sostienici"),
	url(r'^link/$', LinkView, name="link"),
	url(r'^language/(?P<language>[a-z\-]+)/$', language),
	#url(r'^(?P<post_id>\d+)/$', DettaglioView, name="dettaglio"),
	
)