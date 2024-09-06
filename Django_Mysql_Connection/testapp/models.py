from django.db import models

# Create your models here.
class emp(models.Model):
    ename = models.CharField(max_length=20)