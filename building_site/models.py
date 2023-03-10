from django.db import models


class Sites(models.Model):

    CONTRACT_TYPE_CHOICES = (
        ('по договору строительного подряда', 'по договору строительного подряда'),
        ('по договору строительного генподряда', 'по договору строительного генподряда'),
        ('по договору строительного подряда', 'по договору строительного подряда'),
        ('по договору', 'по договору'),
    )

    MAIN_MANAGER_CHOICES = (
        ('Начальник ОРСМУ Буковский С.А.',
         'Начальник ОРСМУ Буковский С.А.'),
        ('Заместитель начальника ОРСМУ Волохов Д.В.',
         'Заместитель начальника ОРСМУ Волохов Д.В.'),

        ('Начальник Мирского производственного участка Дрик П.А.',
         'Начальник Мирского производственного участка Дрик П.А.'),
    )

    LINE_MANAGER_CHOICES = (
        ('Производитель работ ОРСМУ Носко Ю.М.',
         'Производитель работ ОРСМУ Носко Ю.М.'),
        ('Мастер строительных и монтажных работ ОРСМУ Терешков И.Е.',
         'Мастер строительных и монтажных работ ОРСМУ Терешков И.Е.'),
        ('Мастер строительных и монтажных работ ОРСМУ Бондарчук П.В.',
         'Мастер строительных и монтажных работ ОРСМУ Бондарчук П.В.'),
        ('Мастер строительных и монтажных работ ОРСМУ Потапчик С.Н.',
         'Мастер строительных и монтажных работ ОРСМУ Потапчик С.Н.'),
        ('Производитель работ Мирского производственного участка Вайцехович В.Н.',
         'Производитель работ Мирского производственного участка Вайцехович В.Н.'),
    )

    title = models.CharField('Строительный объект', max_length=100)
    body = models.TextField('Наименование объекта')
    contract_type = models.CharField('Работы ведутся по:', max_length=100, choices=CONTRACT_TYPE_CHOICES)
    # To use it easy in template site_destination.html by Jinja2 ({{ sites.contract_type }})
    contract_number = models.CharField('Номер договора', max_length=50)
    contract_date = models.DateField('Дата составления договора')
    manager_main = models.CharField('Общее руководство', max_length=100, choices=MAIN_MANAGER_CHOICES)
    manager_line = models.CharField('Линейный руководитель', max_length=250, choices=LINE_MANAGER_CHOICES)

    def __str__(self):
        return f'Объект:{self.title}'

    def get_absolute_url(self):
        return f'/sites/'

    class Meta:
        verbose_name = 'Site'
        verbose_name_plural = 'Sites'
