from django.db import models

# Create your models here.
class FoodChoice(models.Model):
    ctf_type_name = models.CharField(max_length=100)
    ctf_x = models.CharField(max_length=100)
