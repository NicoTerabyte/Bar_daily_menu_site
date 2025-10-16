from django.urls import path

from . import views

#I specify the app name so i won't confuse the various link in the template
app_name = "polls"
urlpatterns = [
	path("", views.index, name="index"),
	path("<int:question_id>/", views.detail, name="detail"),
	path("<int:question_id>/results/", views.results, name="detail"),
	path("<int:question_id>/vote/", views.vote, name="vote")
]

