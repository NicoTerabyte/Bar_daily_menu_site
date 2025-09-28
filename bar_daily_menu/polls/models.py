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
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)

	def __str__(self) -> str:
		return self.choice_text

class Though(models.Model):
	though_name = models.CharField(max_length=200)
	description = models.CharField(max_length=500)

	def __str__(self) -> str:
		return self.though_name

# For my implementation
class First_course(models.Model):
	plate_name = models.CharField(max_length=200)
	ingriedients = []

class Menu(models.Model):
	first_course = None
	second_course = None
	bibite = None
