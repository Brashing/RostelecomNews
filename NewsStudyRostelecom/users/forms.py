from django import forms
from django.core.validators import ValidationError
from django.forms import ModelForm, Textarea, CheckboxSelectMultiple, Select, DateInput, EmailInput, ImageField, FileInput
from .models import *

class AccountForm(ModelForm):
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
