# Generated by Django 3.2.9 on 2022-01-09 11:52

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('estimate', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='favorite',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_favorite', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='calculate',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='calc_author', to=settings.AUTH_USER_MODEL, verbose_name='Автор расчета'),
        ),
        migrations.AddField(
            model_name='calculate',
            name='material',
            field=models.ManyToManyField(related_name='material_calc', through='estimate.QuantityMaterial', to='estimate.Material', verbose_name='Материал'),
        ),
        migrations.AddField(
            model_name='calculate',
            name='tag',
            field=models.ManyToManyField(related_name='tag_calc', to='estimate.Tag', verbose_name='Теги'),
        ),
        migrations.AddField(
            model_name='calculate',
            name='work',
            field=models.ManyToManyField(related_name='work_calc', through='estimate.QuantityWork', to='estimate.Work', verbose_name='Виды работ'),
        ),
        migrations.AddConstraint(
            model_name='quantitywork',
            constraint=models.UniqueConstraint(fields=('calculate', 'work'), name='unicue_work'),
        ),
        migrations.AddConstraint(
            model_name='quantitymaterial',
            constraint=models.UniqueConstraint(fields=('calculate', 'material'), name='unicue_material'),
        ),
        migrations.AddConstraint(
            model_name='favorite',
            constraint=models.UniqueConstraint(fields=('user', 'calculate'), name='add_favorite'),
        ),
    ]
