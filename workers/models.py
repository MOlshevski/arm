from django.db import models


class Workers(models.Model):

    DIVISION_CHOICES = (
        ('Администрация', 'Администрация'),
        ('ОРСМУ', 'ОРСМУ'),
        ('Производственная база', 'Производственная база'),
        ('Мирский производственный участок', 'Мирский производственный участок'),
        ('Участок металла и камня', 'Участок металла и камня'),
        ('Участок деревообработки', 'Участок деревообработки'),
    )

    CHOICES = (
        ('начальник ОРСМУ Буковский С.А.', 'начальник ОРСМУ Буковский С.А.'),
        ('заместитель начальника ОРСМУ Волохов Д.В.', 'заместитель начальника ОРСМУ Волохов Д.В.'),
        ('производитель работ ОРСМУ Носко Ю.М.', 'производитель работ ОРСМУ Носко Ю.М.'),
        ('начальник Мирского производственного участка Дрик П.А.', 'начальник Мирского производственного участка Дрик П.А.'),
        ('начальник участка металла и камня Смольский Д.Ю.', 'начальник участка металла и камня Смольский Д.Ю.'),
        ('начальник участка деревообработки Знак С.Н.', 'начальник участка деревообработки Знак С.Н.'),
        ('Не было', 'Не было'),
        ('Другой', 'Другой'),
    )

    surname = models.CharField('Фамилия', max_length=30)
    firstname = models.CharField('Имя', max_length=30)
    midname = models.CharField('Отчество', max_length=30)
    bday = models.CharField('Дата рождения', max_length=30, null=True, blank=True)
    profession = models.CharField('Профессия', max_length=50)
    division = models.CharField('Структурное подразделение', max_length=50, choices=DIVISION_CHOICES, default='Администрация')
    adress = models.CharField('Адрес', max_length=150, null=True, blank=True)
    manager = models.CharField('Руководитель стажировки', max_length=150, choices=CHOICES, default="Не было")
    training_start = models.DateField('Дата начала стажировки', null=True, blank=True)
    training_end = models.DateField('Дата окончания стажировки', null=True, blank=True)
    exam = models.DateField('Дата текущей проверки знаний', null=True, blank=True)
    medical = models.DateField('Дата текущего мед. осмотра', null=True, blank=True)

    def __str__(self):
        return f'Фамилия работника:{self.surname}'

    def get_absolute_url(self):
        return f'/workers/'

    class Meta:
        verbose_name = 'Worker'
        verbose_name_plural = 'Workers'
