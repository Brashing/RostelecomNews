from ckeditor.widgets import CKEditorWidget
from .validators import russian_email
from django.core.validators import MinLengthValidator
from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django.core.validators import ValidationError
from django.forms import ModelForm, Textarea, CheckboxSelectMultiple, Select, DateInput, EmailInput, ImageField, \
    FileInput, TextInput
from .models import *

class UserUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name']
        widgets = {
            'username': TextInput(attrs={'class': 'input', 'placeholder': 'Логин'}),
            'email': EmailInput(attrs={'class': 'input','placeholder': 'Адрес электронной почты'}),
            'first_name': TextInput(attrs={'class': 'input', 'placeholder': 'Имя'}),
            'last_name': TextInput(attrs={'class': 'input', 'placeholder': 'Фамилия'}),
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

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, validators = [MinLengthValidator(2)])
    email = forms.CharField(validators=[russian_email])
    message = forms.CharField(widget=CKEditorWidget())
