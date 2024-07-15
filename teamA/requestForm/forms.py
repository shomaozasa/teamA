from django import forms
from .models import Request

class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ['name', 'system_name', 'system_overview', 'mail']
        labels = {
            'name': '名前',
            'system_name': 'システム名',
            'system_overview': 'システム概要',
            'mail': 'メールアドレス',
        }
        widgets = {
            'system_overview': forms.Textarea(attrs={'rows': 6, 'cols': 40}),
        }

