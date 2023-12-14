# Generated by Django 4.2.7 on 2023-12-05 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['title'], 'verbose_name': 'Фото', 'verbose_name_plural': 'Фото'},
        ),
        migrations.AddField(
            model_name='article',
            name='status',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='categories',
            field=models.CharField(choices=[('АН', 'Астрономия'), ('К', 'Космонавтика'), ('АФ', 'Астрофизика'), ('Г', 'Геология')], max_length=20, verbose_name='Категории'),
        ),
        migrations.AlterField(
            model_name='article',
            name='image_news',
            field=models.ImageField(default='default.jpg', upload_to='news_images/', verbose_name='Фото новости'),
        ),
    ]