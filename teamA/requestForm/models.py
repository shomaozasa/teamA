from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    user_id = models.CharField(max_length=10, null=False, blank=False)

class Request(models.Model):
    request_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False, blank=False)
    system_name = models.CharField(max_length=100, null=False, blank=False, default='default')
    system_overview = models.CharField(null=False, blank=False, default='default')
    mail = models.EmailField(max_length=100, null=False, blank=False)
    date = models.DateField(auto_now_add=True, null=False, blank=False)


