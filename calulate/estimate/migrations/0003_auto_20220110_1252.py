# Generated by Django 3.2.9 on 2022-01-10 08:52

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estimate', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='material',
            name='price',
            field=models.IntegerField(default=0, help_text='Укажите справочную цену материала', validators=[django.core.validators.MinValueValidator(0, 'Минимальное значение: 0')], verbose_name='Справочная цена материала'),
        ),
        migrations.AddField(
            model_name='quantitywork',
            name='price',
            field=models.IntegerField(default=0, help_text='Укажите цену работы', validators=[django.core.validators.MinValueValidator(0, 'Минимальное значение: 0')], verbose_name='Цена за работу'),
        ),
        migrations.AlterField(
            model_name='work',
            name='price',
            field=models.IntegerField(default=0, help_text='Укажите справочную цену за работу', validators=[django.core.validators.MinValueValidator(0, 'Минимальное значение: 0')], verbose_name='Справочная цена работы'),
        ),
    ]
