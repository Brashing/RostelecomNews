from ckeditor.widgets import CKEditorWidget
from .validators import russian_email
from django.core.validators import MinLengthValidator
from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django.core.validators import ValidationError
from django.forms import ModelForm, Textarea, CheckboxSelectMultiple, Select, DateInput, EmailInput, ImageField, \
    FileInput, TextInput, DateField
from .models import *

class UserUpdateForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'last_name', 'first_name', 'email']
        widgets = {
            'username': TextInput(attrs={'class': 'input', 'placeholder': 'Логин'}),
            'first_name': TextInput(attrs={'class': 'input', 'placeholder': 'Имя'}),
            'last_name': TextInput(attrs={'class': 'input', 'placeholder': 'Фамилия'}),
            'email': EmailInput(attrs={'class': 'input', 'placeholder': 'Адрес электронной почты'}),
        }

class AccountUpdateForm(ModelForm):
    class Meta:
        model = Account
        fields = ['nickname','birthdate','gender','account_image']
        widgets = {
            'nickname': Textarea(attrs={'cols': 80, 'rows': 1}),
            'birthdate': DateInput(attrs={'auto_create': True}),
            'gender': Select(),
            'account_image': FileInput(),
        }

    def clean_nickname(self):
        nickname = self.cleaned_data['nickname']
        if len(nickname) < 2:
            raise ValidationError('Имя не может быть меньше 2 знаков')
        return nickname

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ['name', 'email', 'message']