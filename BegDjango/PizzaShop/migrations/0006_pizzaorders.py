# Generated by Django 4.1.1 on 2022-12-27 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PizzaShop', '0005_users_role'),
    ]

    operations = [
        migrations.CreateModel(
            name='PizzaOrders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('cost', models.IntegerField(verbose_name='Стоимость')),
                ('login', models.CharField(max_length=50, verbose_name='Логин')),
            ],
        ),
    ]
