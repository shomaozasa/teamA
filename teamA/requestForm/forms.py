from django import forms
from django.core.exceptions import ValidationError
from .models import Request, RequestFunction, User

class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ['name', 'system_name', 'mail']
        labels = {
            'name': '名前',
            'system_name': 'システム名',
            'mail': 'メールアドレス',
        }
        
class RequestFunctionForm(forms.ModelForm):
    class Meta:
        model = RequestFunction
        fields = ['function_name', 'description']
        labels = {
            'function_name': '機能名',
            'description': '機能の説明',
        }

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['user_id', 'password']
        labels = {
            'user_id': 'ユーザーID',
            'password': 'パスワード',
        }
        widgets = {
            'password': forms.PasswordInput(),
        }

