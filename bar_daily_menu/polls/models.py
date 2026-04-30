import datetime

from django.db import models
from django.utils import timezone


# Create your models here.

class Question(models.Model):
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField("Date published")

	def __str__(self) -> str:
		return self.question_text

	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

#Relation one to many more choices can be related to one question
class Choice(models.Model):
	#! the foreign key signifies that links each Choice to the Question class
	#? related_name makes it able to avoid ambiguity. so you can refer to the name here
	#? instead of the modelName_set prefix
	question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="choices")
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)

	#this gets used in the html
	def __str__(self) -> str:
		return self.choice_text

class Comment(models.Model):
	comment_name = models.CharField(max_length=200)
	description = models.CharField(max_length=500)
	#una scelta può avere più commenti
	choice = models.ForeignKey(Choice, on_delete=models.CASCADE, related_name="comments")

	def __str__(self) -> str:
		return self.comment_name

# For my implementation
class First_course(models.Model):
	plate_name = models.CharField(max_length=200)
	ingriedients = []

class Menu(models.Model):
	first_course = None
	second_course = None
	bibite = None
