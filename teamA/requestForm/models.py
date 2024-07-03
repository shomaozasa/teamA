from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    user_id = models.CharField(max_length=10, null=False, blank=False)

class Request(models.Model):
    request_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False, blank=False)
    work_name = models.CharField(max_length=100, null=False, blank=False)
    mail = models.EmailField(max_length=100, null=False, blank=False)
    date = models.DateField(auto_now_add=True, null=False, blank=False)

class RequestFunction(models.Model):
    function_id = models.AutoField(primary_key=True)
    request_id = models.ForeignKey(Request, on_delete=models.CASCADE)
    function_name = models.CharField(max_length=50, null=False, blank=False)
    description = models.TextField(max_length=400, null=False, blank=False)


