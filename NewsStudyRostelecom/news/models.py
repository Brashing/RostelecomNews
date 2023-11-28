from django.db import models

from django.contrib.auth.models import User

class Tag(models.Model):
    title = models.CharField(max_length=80)
    status = models.BooleanField(default=True)
    def __str__(self):
        return self.title
    class Meta:
        ordering = ['title','status']
        verbose_name= 'Тэг'
        verbose_name_plural='Тэги'

class Article(models.Model):
    categories = (('АН', 'Астрономия'),
                  ('К', 'Космонавтика'),
                  ('АФ', 'Астрофизика'))
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='Автор')
    title = models.CharField('Название', max_length=150,default='', null=False)
    anouncement = models.TextField('Аннотация', max_length=1250, null=False)
    source = models.CharField('Источник', max_length=150, null=False)
    sourcename = models.CharField('Название источника', max_length=150, null=False)
    text = models.TextField('Текст новости', null=False)
    date = models.DateTimeField('Дата публикации', auto_created=True, null=False)
    categories=models.CharField(choices=categories, max_length=20, verbose_name='Категории', null=False)
    tags = models.ManyToManyField(to=Tag, blank=True)
    # objects = models.Manager()
    # published = PublishedToday()
    #методы моделей
    def __str__(self):
        return f'Статья №{self.id} от {str(self.date)[:16]} "{self.title}"'

    def get_absolute_url(self):
        return f'/news/{self.pk}'

    #метаданные модели
    class Meta:
        ordering = ['title','date']
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
