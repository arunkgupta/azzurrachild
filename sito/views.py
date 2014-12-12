from django.shortcuts import render
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext
from django.views.generic import ListView, DetailView
from sito.models import *
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template.loader import render_to_string
from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponseRedirect


def HomeView(request):
	language = "it"
	session_language = "it"
	if 'lang' in request.COOKIES:
		language = request.COOKIES['lang']
	if 'lang' in request.session:
		session_language = request.session['lang']
	
	slider_list = Slider.objects.all()
	news_list = News.objects.all()[:6]
	blog_list = Post.objects.all()[:4]
	page_list = Page.objects.all()[:6]
	context = {'slider_list': slider_list,
				'language':language,
				'news_list': news_list,
				'blog_list': blog_list,
				'page_list': page_list
				}
	return render(request, 'index.html', context)

def ProgettiView(request):
	language = "it"
	session_language = "it"
	if 'lang' in request.COOKIES:
		language = request.COOKIES['lang']
	if 'lang' in request.session:
		session_language = request.session['lang']

	page_list = Page.objects.all()
	context = {
				'page_list': page_list,
				'language':language
				}
	return render(request, 'progetti.html', context)

def NewsView(request):
	language = "it"
	session_language = "it"
	if 'lang' in request.COOKIES:
		language = request.COOKIES['lang']
	if 'lang' in request.session:
		session_language = request.session['lang']

	news_list = News.objects.all()
	context = {
				'news_list': news_list,
				'language':language
				}
	return render(request, 'news.html', context)

def LinkView(request):
	language = "it"
	session_language = "it"
	if 'lang' in request.COOKIES:
		language = request.COOKIES['lang']
	if 'lang' in request.session:
		session_language = request.session['lang']

	link_list = Link.objects.all()
	context = {
				'link_list': link_list,
				'language':language
				}
	return render(request, 'link.html', context)

def ChisiamoView(request):
	return render_to_response('chisiamo.html', context_instance=RequestContext(request))

def SostieniciView(request):
	return render_to_response('sostienici.html', context_instance=RequestContext(request))


def language(request, language='it'):
    response = HttpResponse("setting language to %s" % language)
    response.set_cookie('lang', language)
    request.session['lang'] = language
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

