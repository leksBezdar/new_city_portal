from django.db import models
from django.urls import reverse


class Api(models.Model):
    problem = models.CharField(max_length=50, verbose_name="Проблема", blank=True)
    description = models.TextField(blank=True, verbose_name="Описание")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото", blank=True)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время изменения")
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name="Категории", blank=True)

    def __str__(self):
        return self.problem


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Категория", blank=True)

    def __str__(self):
        return self.name

class Menu(models.Model):
    name = models.CharField('Название', max_length=100, blank=True)
    url = models.CharField('Ссылка', max_length=255, unique=True, blank=True)

    def __str__(self):
        return str(self.name)
