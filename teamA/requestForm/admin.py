from django.contrib import admin
from .models import User, Request, RequestFunction
# Register your models here.

admin.site.register(User)
admin.site.register(Request)
admin.site.register(RequestFunction)