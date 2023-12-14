# Generated by Django 4.2.7 on 2023-12-13 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_account_nickname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='gender',
            field=models.CharField(choices=[('М', 'Мужской'), ('Ж', 'Женский'), ('N/A', 'Не определен')], max_length=20, null=True, verbose_name='Пол'),
        ),
    ]