from django.db import models
from django.db.models.fields.related import ForeignKey
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator

class Tag(models.Model):
    name = models.CharField(
        max_length=100, verbose_name= 'Название',
        help_text='Укажите наименование тега'
        )
    slug = models.SlugField(
        max_length=100, unique=True,
        verbose_name='Уникальный слаг'
        )

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
        ordering = ['name']
    
    def __str__(self):
        return self.name


class Work(models.Model):
    name = models.CharField(
        max_length=100, verbose_name='Название',
        help_text='Укажите наименование работы'
        )
    measurement_unit = models.CharField(
        max_length=10, verbose_name='Еденица измерения'
        )
    price = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0, 'Минимальное значение: 0')],
        verbose_name='Цена работы', help_text='Укажите цену за работу'
        )

    class Meta:
        indexes = [
            models.Index(fields=['name']),
        ]
        verbose_name = 'Работы'
        verbose_name_plural = 'Работы'
        ordering = ['name']

    def __str__(self):
        return self.name


class Material(models.Model):
    name = models.CharField(
        max_length=100, verbose_name= 'Название', help_text='Укажите наименование материала'
        )
    measurement_unit = models.CharField(
        max_length=10, verbose_name='Еденица измерения'
        )
    price = models.IntegerField(
        default=0, validators=[MinValueValidator(0, 'Минимальное значение: 0')],
        verbose_name= 'Цена материала', help_text='Укажите цену за материал'
        )

    class Meta:
        indexes = [
            models.Index(fields=['name']),
        ]
        verbose_name = 'Материал'
        verbose_name_plural = 'Матeриал'
        ordering = ['name']

    def __str__(self):
        return self.name


class Calculate(models.Model):
    TUPE_CALC = (
        ('estimate', 'Смета'),
        ('template', 'Шаблон')
        )
    name = models.CharField(
        max_length=100, verbose_name= 'Наименование сметы', help_text='Укажите наименование'
        )
    slug = models.SlugField(
        max_length=100, unique=True, verbose_name= 'Уникальный слаг'
        )
    date_create = models.DateTimeField(
        auto_now_add=True, verbose_name='Дата создания'
        )
    date_update = models.DateTimeField(
        auto_now=True, verbose_name= 'Дата последнего редактирования'
        )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='calc_author', verbose_name='Автор расчета'
        )
    work = models.ManyToManyField(
        Work, 
        verbose_name='Виды работ',
        related_name='work_calc',
        through='QuantityWork',
        through_fields=('calculate', 'work'),
        )
    material = models.ManyToManyField(
        Material, verbose_name='Материал',
        related_name='material_calc',
        through='QuantityMaterial',
        through_fields=('calculate', 'material'),
        )
    text = models.TextField(
        max_length=300, help_text='Введите описание'
        )
    difficulty_factor = models.FloatField(
        verbose_name= 'Коэффициент сложности'
        )
    fuel_price = models.IntegerField(
        validators=[MinValueValidator(0, 'Минимальное значение: 0')],
        verbose_name= 'Транспортные расходы', help_text='Затраты на транспорт')
    upload = models.FileField(
        upload_to='uploads/%Y/%m/%d/', verbose_name= 'Дополнительные файлы'
        )
    tag = models.ManyToManyField(
        Tag, verbose_name='Теги', related_name='tag_calc'
        )
    tupe_calc = models.CharField(
        max_length=15, choices=TUPE_CALC, default='estimate', verbose_name= 'Тип расчета'
    )

    class Meta:
        verbose_name = 'Расчёт'
        verbose_name_plural = 'Расчёты'
        ordering = ['date_update']

    def __str__(self):
        return self.name


class QuantityMaterial(models.Model):
    material = models.ForeignKey(
        Material, on_delete=models.CASCADE, related_name='material_quantity'
    )
    calculate = models.ForeignKey(
        Calculate, on_delete=models.CASCADE, related_name='quantity'
    )
    quantity = models.IntegerField(
        validators=[MinValueValidator(1, 'Минимальное значение: 1')],
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['calculate', 'material'], name='unicue_material'
            ),
        ]

    def __str__(self):
        return f'{self.calculate}, {self.quantity}'


class QuantityWork(models.Model):
    work = models.ForeignKey(
        Work, on_delete=models.CASCADE, related_name='work_quantity'
    )
    calculate = models.ForeignKey(
        Calculate, on_delete=models.CASCADE, related_name='calc_quantity'
    )
    quantity = models.IntegerField(
        validators=[MinValueValidator(1, 'Минимальное значение: 1')],
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['calculate', 'work'], name='unicue_work'
            ),
        ]

    def __str__(self):
        return f'{self.calculate}, {self.quantity}'


class Favorite(models.Model):
    calculate = ForeignKey(Calculate, on_delete=models.CASCADE, related_name='calc_favorite')
    user = ForeignKey(User, on_delete=models.CASCADE, related_name='user_favorite')

    class Meta:
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранное'
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'calculate'], name='add_favorite'
            ),
        ]