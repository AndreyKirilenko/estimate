# Generated by Django 3.2.9 on 2022-01-30 19:28

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estimate', '0008_auto_20220130_2248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quantitymaterial',
            name='quantity',
            field=models.IntegerField(default=0, help_text='Укажите колличество материала', validators=[django.core.validators.MinValueValidator(0, 'Минимальное значение: 0')], verbose_name='Колличество материала'),
        ),
    ]