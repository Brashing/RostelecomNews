from django.db import models

from django.contrib.auth.models import User

class Article(models.Model):
    categories = (('АН', 'Астрономия'),
                  ('К', 'Космонавтика'),
                  ('АФ', 'Астрофизика'))
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='Автор')
    title = models.CharField('Название', max_length=150,default='')
    anouncement = models.TextField('Аннотация', max_length=1250)
    text = models.TextField('Текст новости')
    date = models.DateTimeField('Дата публикации', auto_created=True)
    categories=models.CharField(choices=categories, max_length=20, verbose_name='Категории')

    #методы моделей
    def __str__(self):
        return f'Статья №{self.id} от {str(self.date)[:16]} "{self.title}"'

    def get_absolute_url(selfself):
        return f'/news/show/{self.id}'

    #метаданные модели
    class Meta:
        ordering = ['title','date']
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

