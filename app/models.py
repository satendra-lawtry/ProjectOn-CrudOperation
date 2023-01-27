from statistics import mode
from django.db import models

class UserApp(models.Model):
    name=models.CharField(max_length=40,null=True)
    email=models.EmailField(null=True)
    password=models.CharField(max_length=30,null=True)
    contact=models.BigIntegerField(null=True)