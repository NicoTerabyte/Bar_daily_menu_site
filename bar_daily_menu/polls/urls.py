from django.urls import path

from . import views

#I specify the app name so i won't confuse the various link in the template
app_name = "polls"
urlpatterns = [
	path("", views.IndexView.as_view(), name="index"),
	path("<int:pk>/", views.DetailView.as_view(), name="detail"),
	path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
	path("<int:question_id>/vote/", views.vote, name="vote"),
	path("<int:pk>/add_comment", views.AddComment.as_view(), name="add_comment")
]

