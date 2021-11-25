from django.db import models

# Create your models here.
class Driver(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    phone_number = models.BigIntegerField()
    city = models.CharField(max_length= 30)
    country = models.CharField(max_length=30)

