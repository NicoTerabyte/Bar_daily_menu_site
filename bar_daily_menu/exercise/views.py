from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import loader

# Create your views here.

from .models import alphaModel

def alphaView(request):

	alphaObjList = alphaModel.objects
	print("[DEBUGGING] objects retrieved")
	return render(request=request, template_name="exercise/alpha.html", context={"alpha objects": alphaObjList})
