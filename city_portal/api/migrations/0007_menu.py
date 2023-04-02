# Generated by Django 4.1.7 on 2023-04-01 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_delete_menu'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('url', models.CharField(max_length=255, unique=True, verbose_name='Ссылка')),
            ],
        ),
    ]