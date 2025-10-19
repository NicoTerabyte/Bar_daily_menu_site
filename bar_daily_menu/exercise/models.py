from django.db import models


# Create your models here.

class alphaModel(models.Model):

	name = models.CharField (max_length=50)
	priority_lvl = models.IntegerField()
	active = models.BooleanField()

	def __str__(self) -> str:
		return self.name
