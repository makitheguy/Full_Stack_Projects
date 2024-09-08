from django.db import models

# Create your models here.
class Employee_info(models.Model):
    
    ename = models.CharField(max_length=30)
    esal = models.IntegerField()
    eaddr = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.ename