# Generated by Django 4.1.7 on 2023-04-03 16:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_menu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='api',
            name='cat',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='api.category', verbose_name='Категории'),
        ),
        migrations.AlterField(
            model_name='api',
            name='photo',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='api',
            name='problem',
            field=models.CharField(blank=True, max_length=50, verbose_name='Проблема'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(blank=True, db_index=True, max_length=100, verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='name',
            field=models.CharField(blank=True, max_length=100, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='url',
            field=models.CharField(blank=True, max_length=255, unique=True, verbose_name='Ссылка'),
        ),
    ]
