from ckeditor.fields import RichTextField
from django.db import models
from ckeditor.widgets import CKEditorWidget
from .validators import russian_email
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User


class Account(models.Model):
    gender_choices = (('М', 'Мужской'),
                      ('Ж', 'Женский'),
                      ('N/A', 'Не определен'))
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                primary_key=True, verbose_name='Пользователь')
    nickname = models.CharField(max_length=100, verbose_name='Псевдоним')
    birthdate = models.DateField(null=True, blank=True, verbose_name='День рождения')
    gender = models.CharField(choices=gender_choices, max_length=20, verbose_name='Пол', null=True, blank=True)
    account_image = models.ImageField(default='default.jpg',
                                      upload_to='account_images', verbose_name='Фото аккаунта')

    def __str__(self):
        return f"{self.user.username}'s account"

    class Meta:
        ordering = ['user','gender']
        verbose_name = 'Аккаунт'
        verbose_name_plural = 'Аккаунты'

from news.models import Article
class FavoriteArticle(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True, verbose_name='Пользователь')
    article = models.ForeignKey(Article,on_delete=models.SET_NULL,null=True, verbose_name='Новость')
    create_at=models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')

    class Meta:
        ordering = ['create_at','article','user']
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранное'

class ContactForm(models.Model):
    status = models.BooleanField(default=False, verbose_name='Исправлено')
    name = models.CharField(verbose_name='Имя',max_length=100, validators = [MinLengthValidator(2)], null=False)
    email = models.EmailField(verbose_name='Адрес электронной почты',validators=[russian_email], null=False)
    message = RichTextField(verbose_name='Сообщение', null=False)

    class Meta:
        ordering = ['name']
        verbose_name = 'Форма обратной связи'
        verbose_name_plural = 'Форма обратной связи'