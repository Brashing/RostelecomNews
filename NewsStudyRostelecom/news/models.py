from ckeditor.fields import RichTextField
from django.db import models
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User
from .validators import russian_email
from django.db.models import Count
import datetime

class Tag(models.Model):
    title = models.CharField(max_length=80, verbose_name='Название')
    status = models.BooleanField(default=True, verbose_name='Статус')
    def __str__(self):
        return self.title
    class Meta:
        ordering = ['title','status']
        verbose_name = 'Тэг'
        verbose_name_plural ='Тэги'

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=1)

class Article(models.Model):
    categories = (('A', 'Астрономия'),
                  ('K', 'Космонавтика'),
                  ('AF', 'Астрофизика'),
                  ('G', 'Геология'))
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='Автор')
    title = models.CharField('Название новости', max_length=150, default='', null=False)
    anouncement = models.TextField('Аннотация', max_length=1250, null=False)
    source = models.URLField('Источник', null=True)
    sourcename = models.CharField('Название источника', max_length=150, null=False)
    text = RichTextField('Текст новости', null=False)
    date = models.DateTimeField('Дата публикации', auto_created=True)
    categories = models.CharField(choices=categories, max_length=20, verbose_name='Категории')
    tags = models.ManyToManyField(to=Tag, blank=True)
    status = models.BooleanField(default=False, verbose_name='Опубликовано')
    objects = models.Manager()
    published = PublishedManager()

    def __str__(self):
        return f'Статья №{self.id} от {str(self.date)[:16]} "{self.title}"'

    def get_absolute_url(self):
        return f'/news/{self.pk}'

    #метаданные модели
    def tag_list(self):
        s = ''
        for t in self.tags.all():
            s+=t.title+' '
        return s

    def image_tag(self):
        image = Image.objects.filter(article=self)
        if image:
            return mark_safe(f'<img src="{image[0].image.url}" height="50px" width="auto" />')
        else:
            return '(no image)'

    def get_views(self):
        return self.views.count()

    class Meta:
        ordering = ['title','date']
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

class Subscriber(models.Model):
    last_name = models.CharField(max_length=50, verbose_name='Фамилия', default='', null=False)
    first_name = models.CharField(max_length=50, verbose_name='Имя', default='', null=False)
    email = models.EmailField(max_length=254, verbose_name='Адрес электронной почты', null=False, validators=[russian_email])

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.email}"

    class Meta:
        ordering = ['last_name']
        verbose_name = 'Подписчик'
        verbose_name_plural = 'Подписчики'

class Image(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    title = models.CharField(max_length=150, blank=True)
    image = models.ImageField(upload_to='news_images/', blank=True, null=True)

    def __str__(self):
        return self.title

    def image_tag(self):
        if self.image is not None:
            return mark_safe(f'<img src="{self.image.url}" height="50px" width="auto"/>')
        else:
            return '(no image)'

    class Meta:
        ordering = ['title']
        verbose_name = 'Фото'
        verbose_name_plural = 'Фото'

class ViewCount(models.Model):
    article = models.ForeignKey(Article,on_delete=models.CASCADE,
                                related_name='views', verbose_name='Новость')
    ip_address = models.GenericIPAddressField(verbose_name='ip-адрес')
    view_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата просмотра')

    class Meta:
        verbose_name = 'Счетчик просмотров'
        verbose_name = 'Счетчик просмотров'
        verbose_name_plural = 'Счетчики просмотров'
        ordering=('-view_date',)
        indexes = [models.Index(fields=['-view_date'])]

    def __str__(self):
        return self.article.title