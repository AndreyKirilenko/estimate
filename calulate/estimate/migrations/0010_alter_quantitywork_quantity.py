# Generated by Django 3.2.9 on 2022-02-02 15:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estimate', '0009_alter_quantitymaterial_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quantitywork',
            name='quantity',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(1, 'Минимальное значение: 1')], verbose_name='Колличество'),
        ),
    ]
