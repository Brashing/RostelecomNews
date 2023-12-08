# Generated by Django 4.2.7 on 2023-12-04 20:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_created=True, verbose_name='Дата публикации')),
                ('image_news', models.ImageField(default='default.jpg', upload_to='news_images', verbose_name='Фото новости')),
                ('title', models.CharField(default='', max_length=150, verbose_name='Название новости')),
                ('anouncement', models.TextField(max_length=1250, verbose_name='Аннотация')),
                ('source', models.URLField(verbose_name='Источник')),
                ('sourcename', models.CharField(max_length=150, verbose_name='Название источника')),
                ('text', models.TextField(verbose_name='Текст новости')),
                ('categories', models.CharField(choices=[('АН', 'Астрономия'), ('К', 'Космонавтика'), ('АФ', 'Астрофизика')], max_length=20, verbose_name='Категории')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
                'ordering': ['title', 'date'],
            },
        ),
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(default='', max_length=50, verbose_name='Фамилия')),
                ('first_name', models.CharField(default='', max_length=50, verbose_name='Имя')),
                ('email', models.EmailField(max_length=254, verbose_name='Адрес электронной почты')),
            ],
            options={
                'verbose_name': 'Подписчик',
                'verbose_name_plural': 'Подписчики',
                'ordering': ['last_name'],
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80, verbose_name='Название')),
                ('status', models.BooleanField(default=True, verbose_name='Статус')),
            ],
            options={
                'verbose_name': 'Тэг',
                'verbose_name_plural': 'Тэги',
                'ordering': ['title', 'status'],
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50)),
                ('image', models.ImageField(upload_to='news_images/')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.article')),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(blank=True, to='news.tag'),
        ),
    ]