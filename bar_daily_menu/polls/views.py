from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import loader
import sys
#importing from the a directory behind
sys.path.append("../bar_booking_management")
from bar_booking_management.Colors import Colors

from .models import Question
# Create your views here.


def index (request):
	lastest_question_list = Question.objects.order_by("-pub_date")[:5]
	#template = loader.get_template("polls/index.html")
	context = {"latest_question_list": lastest_question_list}
	# withouth the template we can use the render function to do quickly
	# this type of return should be used when using stub data i guess?
	#return HttpResponse(template.render(context, request))
	return render(request, "polls/index.html", context)

# longer version with http404 implementation
# def detail(request, question_id):

# 	try:
# 		question = Question.objects.get(pk=question_id)
# 	except Question.DoesNotExist:
# 		raise Http404("Question does not exist")

# 	return HttpResponse("You are looking at question %s" %question_id)

def detail(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	Colors.coloredMessage(Colors.CYAN, "Question retrieved ")
	print(question)
	return render(request, "polls/detail.html", {"question" : question})

def results(request, question_id):
	response = "You're looking at the results of question %s."
	return HttpResponse(response % question_id)

def vote(request, question_id):
		return HttpResponse("You are voting for the question %s." %question_id)
