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

# Create your views here.


'''
def HomeView(request):
	immagini_list = Immagini.objects.filter(categoria = '1').order_by('id')
	dottori_list = Immagini.objects.filter(categoria = '2').order_by('id')
	scelta_list = Immagini.objects.filter(categoria = '3').order_by('id')
	context = {'immagini_list': immagini_list,
				'dottori_list': dottori_list,
				'scelta_list': scelta_list
				}
   #return render_to_response('index.html', context_instance=RequestContext(request))
	return render(request, 'index.html', context)

'''