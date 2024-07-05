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

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name:
            raise ValidationError('名前は必須です。')
        return name
    
    def clean_system_name(self):
        work_name = self.cleaned_data.get('work_name')
        if not work_name:
            raise ValidationError('システム名は必須です。')
        return work_name

    def clean_mail(self):
        mail = self.cleaned_data.get('mail')
        if not mail:
            raise ValidationError('メールアドレスは必須です。')
        if '@' not in mail:
            raise ValidationError('有効なメールアドレスを入力してください。')
        return mail

class RequestFunctionForm(forms.ModelForm):
    class Meta:
        model = RequestFunction
        fields = ['function_name', 'description']
        labels = {
            'function_name': '機能名',
            'description': '機能の説明',
        }

    def clean_function_name(self):
        function_name = self.cleaned_data.get('function_name')
        if not function_name:
            raise ValidationError('機能名は必須です。')
        return function_name

    def clean_description(self):
        description = self.cleaned_data.get('description')
        if not description:
            raise ValidationError('機能の説明は必須です。')
        return description

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

    def clean_user_id(self):
        user_id = self.cleaned_data.get('user_id')
        if not user_id:
            raise ValidationError('ユーザーIDは必須です。')
        if User.objects.filter(user_id=user_id).exists():
            raise ValidationError('このユーザーIDは既に使用されています。')
        return user_id

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if not password:
            raise ValidationError('パスワードは必須です。')
        return password
