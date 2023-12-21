from django.db import models
from django.contrib.contenttypes.fields import GenericRelation, GenericForeignKey
from django.contrib.contenttypes.models import ContentType
# Create your models here.


class PizzaMenu(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название")
    cost = models.IntegerField(verbose_name="Стоимость")
    image = models.ImageField(verbose_name="Фото", upload_to='images', default=None)


class PizzaRecepts(models.Model):
    recept = models.CharField(max_length=1000, verbose_name="Рецепт")
    name = models.ForeignKey(PizzaMenu, on_delete=models.CASCADE, verbose_name="Название")


class Users(models.Model):
    login = models.CharField(verbose_name="Логин", max_length=50)
    password = models.CharField(verbose_name="Пароль", max_length=30)
    role = models.CharField(verbose_name='Роль', default='Member', max_length=30)


class PizzaOrders(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название")
    cost = models.IntegerField(verbose_name="Стоимость")
    count = models.IntegerField(verbose_name="Количество", default=0)
    login = models.CharField(verbose_name="Логин", max_length=50)
