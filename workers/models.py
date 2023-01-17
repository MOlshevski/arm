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

    CHOICES_FREQUENCY = (
        ('1 раз в 2 года', '1 раз в 2 года'),
        ('1 раз в год', '1 раз в год'),
    )

    DANGEROUS_FACTORS_CHOICES = (
        ('Пыль растительного происхождения (А): древесина, пр.1, п.2.7;',
         'Пыль растительного происхождения (А): древесина, пр.1, п.2.7;'),
        ('Работы на механическом оборудовании, пр.3 п.12', 'Работы на механическом оборудовании, пр.3 п.12'),
        ('Работа на высоте, пр.3 п.1.', 'Работа на высоте, пр.3 п.1.'),
        ('Производственный шум, пр.1 п.4.4;', 'Производственный шум, пр.1 п.4.4;'),
        ('Тепловое излучение, пр. 1 п.4.9.', 'Тепловое излучение, пр. 1 п.4.9.'),
        ('Работы, связанные с оптическими приборами при длительности сосредоточенного наблюдения более 50 % времени рабочей смены пр.1 п.5.6',
         'Работы, связанные с оптическими приборами при длительности сосредоточенного наблюдения более 50 % времени рабочей смены пр.1 п.5.6'),
        ('Повышенная температура воздуха, пр. 1 п.4.8.', 'Повышенная температура воздуха, пр. 1 п.4.8.'),
        ('Углеводороды ароматические: бензол (К), толуол, ксилол, стирол и другие, пр.1, п.1.1.31.',
         'Углеводороды ароматические: бензол (К), толуол, ксилол, стирол и другие, пр.1, п.1.1.31.'),
        ('Альдегиды алифатические (предельные, непредельные и ароматические): формальдегид (К, А), ацетальдегид, акролеин, бензальдегид, фталевый (А), глутаровый альдегид (А), пр.1, п.1.1.2.',
         'Альдегиды алифатические (предельные, непредельные и ароматические): формальдегид (К, А), ацетальдегид, акролеин, бензальдегид, фталевый (А), глутаровый альдегид (А), пр.1, п.1.1.2.'),
    )

    surname = models.CharField('Фамилия', max_length=30)
    firstname = models.CharField('Имя', max_length=30)
    midname = models.CharField('Отчество', max_length=30)
    bday = models.CharField('Дата рождения', max_length=30, null=True, blank=True)
    profession = models.ForeignKey('Professions', on_delete=models.PROTECT, null=True)
    # I use ForeignKey here to link to the Professions model and make Select mode in forms.py
    division = models.CharField('Структурное подразделение', max_length=50, choices=DIVISION_CHOICES, default='Администрация')
    adress = models.CharField('Адрес', max_length=150, null=True, blank=True)
    manager = models.CharField('Руководитель стажировки', max_length=150, choices=CHOICES, default="Не было")
    training_start = models.DateField('Дата начала стажировки', null=True, blank=True)
    training_end = models.DateField('Дата окончания стажировки', null=True, blank=True)
    exam = models.DateField('Дата текущей проверки знаний', null=True, blank=True)
    medical = models.DateField('Дата текущего мед. осмотра', null=True, blank=True)
    dangerous_factors = models.CharField('Вредные и опасные факторы', max_length=200, choices=DANGEROUS_FACTORS_CHOICES,
                                         null=True, blank=True)
    condition_class = models.CharField('Класс условий труда', max_length=10, null=True, blank=True)
    frequency = models.CharField('Периодичность проведения медицинского осмотра',
                                 max_length=20, choices=CHOICES_FREQUENCY, null=True, blank=True)

    def __str__(self):
        return f'Фамилия работника:{self.surname}'

    def get_absolute_url(self):
        return f'/workers/'

    class Meta:
        verbose_name = 'Worker'
        verbose_name_plural = 'Workers'


"""Model Professions will be displayed only in the admin panel. Made for easy choice of profession in the form of 
worker creation"""


class Professions(models.Model):
    profession = models.CharField('Профессия', max_length=50)

    def __str__(self):
        return self.profession  # To display a profession not as an object, but by title

    class Meta:
        verbose_name = 'Profession'
        verbose_name_plural = 'Professions'

