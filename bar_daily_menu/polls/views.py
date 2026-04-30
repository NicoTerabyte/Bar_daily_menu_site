from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
import sys
from django.urls import reverse
from django.db.models import F
from django.views import generic, View
import logging
#importing from the a directory behind
sys.path.append("../bar_booking_management")
from bar_booking_management.Colors import Colors

from .models import Question, Choice, Comment
# Create your views here.

logging.basicConfig(
	level=logging.DEBUG,
	format="%(asctime)s - %(levelname)s - %(message)s",
	datefmt='%H:%M:%S'
)

view_logger = logging.getLogger("ViewLogger")
view_logger.setLevel(logging.DEBUG)

view_logger.debug("first log :)")

#! implementing the generic views
class IndexView(generic.ListView):
	'''
	Return the last five published questions.
	It is automatic in the generic.ListView class
	We are inhereting the get_queryset method and we are
	overriding it for our Question model
	'''
	template_name = "polls/index.html"
	context_object_name = "latest_question_list"


	def get_queryset(self):
		return Question.objects.order_by("-pub_date")[:5]


class DetailView(generic.DetailView):
	'''
		inhereting from the generic.Detailview sorry for the redudancy of the name
		they do have the model and template_name variable
	'''
	model = Question
	template_name = "polls/detail.html"


class ResultsView(generic.DetailView):
	"""Qui viene reinderizzato quando voti"""
	model = Question
	template_name = "polls/results.html"



class AddComment(View):
	"""
	Questa classe deve essere in grado di reinderizzare
	la choice di vote
	"""

	def __init__(self) -> None:
		view_logger.debug(Colors.coloredMessage(Colors.YELLOW, "add_comment triggered init"))
		super().__init__()


	def get(self, request):
		return HttpResponse()

	def post(self, request, choice_id):
		view_logger.debug(Colors.coloredMessage(Colors.GREEN, "add_comment POST request received"))
		view_logger.debug(Colors.coloredMessage(Colors.GREEN, "Received choice data from choice {}".format(choice_id)))

		received_choice = get_object_or_404(Choice, pk=choice_id)
		return render(request, "polls/add_comment.html")

def vote(request, question_id):
	question = get_object_or_404(Question, pk=question_id)

	try:
		selected_choice = question.choices.get(pk=request.POST["choice"])

	except (KeyError, Choice.DoesNotExist):
		return render(
			request, "polls/detail.html",
			{
				"question": question,
				"error_message": "You didn't select a choice.",
			},
		)

	else:
		selected_choice.votes = F("votes") + 1
		selected_choice.save()
		return HttpResponseRedirect(reverse("polls:add_comment", args=(question.id,)))





## Old code for theory
# Old view the hard way
# def index (request):
# 	lastest_question_list = Question.objects.order_by("-pub_date")[:5]
# 	#template = loader.get_template("polls/index.html")
# 	context = {"latest_question_list": lastest_question_list}
# 	# withouth the template we can use the render function to do quickly
# 	# this type of return should be used when using stub data i guess?
# 	#return HttpResponse(template.rpassender(context, request))
# 	return render(request, "polls/index.html", context)

# longer version with http404 implementation
# def detail(request, question_id):

# 	try:
# 		question = Question.objects.get(pk=question_id)
# 	except Question.DoesNotExist:
# 		raise Http404("Question does not exist")

# 	return HttpResponse("You are looking at question %s" %question_id)


# def detail(request, question_id):
# 	question = get_object_or_404(Question, pk=question_id)
# 	Colors.coloredMessage(Colors.CYAN, "Question retrieved ")
# 	return render(request, "polls/detail.html", {"question" : question})

# def results(request, question_id):
# 	question = get_object_or_404(Question, pk=question_id)
# 	return render(request, "polls/results.html", {"question" : question})
