# Generated by Django 4.1.7 on 2023-04-01 16:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_remove_menu_position_alter_menu_url'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Menu',
        ),
    ]