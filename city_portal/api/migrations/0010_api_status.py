# Generated by Django 4.1.7 on 2023-04-03 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_remove_api_description_alter_api_problem'),
    ]

    operations = [
        migrations.AddField(
            model_name='api',
            name='status',
            field=models.CharField(default='Новая', max_length=50, verbose_name='Статус заявки'),
        ),
    ]