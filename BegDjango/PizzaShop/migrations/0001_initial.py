# Generated by Django 4.1.1 on 2022-11-26 18:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PizzaMenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('cost', models.IntegerField(max_length=1000000, verbose_name='Стоимость')),
            ],
        ),
        migrations.CreateModel(
            name='PizzaRecepts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recept', models.CharField(max_length=1000, verbose_name='Рецепт')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PizzaShop.pizzamenu', verbose_name='Название')),
            ],
        ),
    ]