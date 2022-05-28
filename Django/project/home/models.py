from django.db import models

# Create your models here.
class Register_on(models.Model):
    parentname = models.CharField(max_length=122)
    childname = models.CharField(max_length=122)
    guardianname = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()

class Feedback(models.Model):
    parentname = models.CharField(max_length=122)
    childname = models.CharField(max_length=122)
    guardianname = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()