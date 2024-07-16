from django import forms
from django.contrib import admin
from .models import Request, User
# Register your models here.


class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = '__all__'
        widgets = {
            'status': forms.RadioSelect
        }

class RequestAdmin(admin.ModelAdmin):
    form = RequestForm

admin.site.register(Request)
admin.site.register(User)