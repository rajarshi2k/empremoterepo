from django.db import models
from django.urls import reverse

# Create your models here.
class Emp(models.Model):
    name=models.CharField(max_length=128)
    age=models.IntegerField()
    basic=models.FloatField()

    def get_absolute_url(self):
        return reverse('list')