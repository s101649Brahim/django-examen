from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.http import Http404
from django.urls import reverse
from django.views import generic

import datetime



def index(request):
    nu = datetime.datetime.now()
    brexitTijd = datetime.datetime(2019, 3, 29, 11)
    
    verschil = brexitTijd - nu

    return HttpResponse(" %s." % verschil)
    
    
    
    

