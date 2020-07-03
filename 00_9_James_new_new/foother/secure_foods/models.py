from django.db import models

# Create your models here.
class AuthCountry(models.Model):
    ctf_name = models.CharField(max_length=100),
    ctf_x = models.CharField(max_length=100),
    ctf_y = models.CharField(max_length=100),
    ctf_addr = models.CharField(max_length=100),
    ctf_tel = models.CharField(max_length=12),
    ctf_code = models.IntegerField(),
    ctf_type = models.IntegerField(),
    ctf_type_name = models.CharField(max_length=50),