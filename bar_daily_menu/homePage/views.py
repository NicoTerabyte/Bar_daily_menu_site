from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import loader

# Create your views here.

def homeView(request):
	return render(request, template_name="homePage/home.html")
