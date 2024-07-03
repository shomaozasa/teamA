from django import forms
from .models import Request, RequestFunction, User

class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ['name', 'work_name', 'mail']
        labels = {
            'name': '名前',
            'work_name': '作品名',
            'mail': 'メールアドレス',
        }

class RequestFunctionForm(forms.ModelForm):
    class Meta:
        model = RequestFunction
        fields = ['request_id', 'function_name', 'description']
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