# Generated by Django 4.2.7 on 2023-12-06 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_alter_image_options_article_status_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='image_news',
        ),
        migrations.AlterField(
            model_name='article',
            name='status',
            field=models.BooleanField(default=True, verbose_name='Опубликовано'),
        ),
    ]