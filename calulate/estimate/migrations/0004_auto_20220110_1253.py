# Generated by Django 3.2.9 on 2022-01-10 08:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estimate', '0003_auto_20220110_1252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='price',
            field=models.IntegerField(help_text='Укажите справочную цену материала', validators=[django.core.validators.MinValueValidator(0, 'Минимальное значение: 0')], verbose_name='Справочная цена материала'),
        ),
        migrations.AlterField(
            model_name='work',
            name='price',
            field=models.IntegerField(help_text='Укажите справочную цену за работу', validators=[django.core.validators.MinValueValidator(0, 'Минимальное значение: 0')], verbose_name='Справочная цена работы'),
        ),
    ]
