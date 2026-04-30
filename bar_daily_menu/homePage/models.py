from django.db import models

#many to many relationship

class Sports(models.Model):
	sportName = models.CharField(max_length=50)
	practicioners = models.IntegerField(default=0)


# Create your models here.
class UserData(models.Model):
	name = models.CharField(max_length=50)
	age = models.IntegerField()
	favoriteSport = models.CharField(max_length=50)


class UserSports(models.Model):
	sport = models.ForeignKey(Sports, on_delete=models.CASCADE)
	user = models.ForeignKey(UserData, on_delete=models.CASCADE)
