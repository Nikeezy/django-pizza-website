# Generated by Django 4.1.1 on 2023-02-07 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PizzaShop', '0006_pizzaorders'),
    ]

    operations = [
        migrations.AddField(
            model_name='pizzaorders',
            name='count',
            field=models.IntegerField(default=0, verbose_name='Количество'),
        ),
    ]
