# Generated by Django 4.1.1 on 2023-03-08 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PizzaShop', '0008_pizzamenu_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizzamenu',
            name='image',
            field=models.ImageField(default=None, upload_to='images', verbose_name='Фото'),
        ),
    ]
