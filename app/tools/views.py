from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView

from models import *

# Create your views here.


def mycbtview(request):
	obs = Worksheet.objects.all()
	return HttpResponse("<b>"+unicode(obs))