from django.db import models


class Equipments(models.Model):
    title = models.CharField('Оборудование', max_length=100)
    body = models.TextField('Описание оборудования')
    time = models.CharField('Дата текущей проверки', max_length=25)

    def __str__(self):
        return f'Оборудование:{self.title}'

    def get_absolute_url(self):
        return f'/equipment/'

    class Meta:
        verbose_name = 'Equipment'
        verbose_name_plural = 'Equipments'
