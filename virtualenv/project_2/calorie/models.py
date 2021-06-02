from django.db import models
from model_utils import Choices

GENDER = Choices(
	("Male", "Male"),
	("Female", "Female"),
)

class Info(models.Model):
	name = models.CharField(max_length=64)
	age = models.CharField(max_length=3)
	gender = models.CharField(max_length=16, choices=GENDER, default="Male")
	weight = models.CharField(max_length=64)
	
	def __str__(self):
		return self.name + "'s Information"


class Calorie(models.Model):
	food_type = models.CharField(max_length=20)
	calories = models.CharField(max_length=20)
	food_type1 = models.CharField(max_length=20)
	calories1 = models.CharField(max_length=20)
	food_type2 = models.CharField(max_length=20)
	calories2 = models.CharField(max_length=20)
	food_type3 = models.CharField(max_length=20)
	calories3 = models.CharField(max_length=20)

	def __str__(self):
		return 'All Food'

