# Generated by Django 4.1.7 on 2023-04-01 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_menu'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='position',
        ),
        migrations.AlterField(
            model_name='menu',
            name='url',
            field=models.CharField(max_length=255, unique=True, verbose_name='Ссылка'),
        ),
    ]