from django.db import models

# Create your models here.
# class 

# class GroupSplit(models.Model):

class Transaction(models.Model):
    Transaction = models.CharField(null=True, blank=True,max_length=20)
    Amount = models.IntegerField(null=True, blank=True)
    created = models.DateTimeField(null= True,auto_now_add=True)


