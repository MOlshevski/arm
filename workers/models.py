from django.db import models


class Workers(models.Model):
    surname = models.CharField('Фамилия', max_length=30)
    firstname = models.CharField('Имя', max_length=30)
    midname = models.CharField('Отчество', max_length=30)
    bday = models.CharField('Дата рождения', max_length=30)
    profession = models.CharField('Профессия', max_length=50)
    division = models.CharField('Структурное подразделение', max_length=50)
    adress = models.CharField('Структурное подразделение', max_length=150)

    def __str__(self):
        return f'Фамилия работника:{self.surname}'

    def get_absolute_url(self):
        return f'/workers/'

    class Meta:
        verbose_name = 'Worker'
        verbose_name_plural = 'Workers'
