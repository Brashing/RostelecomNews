from django.db import models

from django.contrib.auth.models import User


class Account(models.Model):
    gender_choices = (('М', 'Мужской'),
                      ('Ж', 'Женский'),
                      ('N/A', 'Не определен'))
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                primary_key=True, verbose_name='Пользователь')
    nickname = models.CharField(max_length=100, verbose_name='Псевдоним')
    birthdate = models.DateField(null=True, verbose_name='День рождения')
    gender = models.CharField(choices=gender_choices, max_length=20, verbose_name='Пол')
    account_image = models.ImageField(default='default.jpg',
                                      upload_to='account_images', verbose_name='Фото аккаунта')

    # pip install pillow в терминале, если нет библиотеки

    def __str__(self):
        return f"{self.user.username}'s account"

    class Meta:
        ordering = ['user','gender']
        verbose_name = 'Аккаунт'
        verbose_name_plural = 'Аккаунты'