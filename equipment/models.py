from django.db import models

"""Model for equipment app. This application is not promising for further refinement, so the model will 
be simple and uninformative"""


class Equipments(models.Model):
    title = models.CharField('Оборудование', max_length=100)
    body = models.TextField('Описание оборудования')
    time = models.CharField('Дата текущей проверки', max_length=25)
    # I made it CharField, to use words like 'не проверялось' or 'не требуется проверка' in this column

    def __str__(self):
        return f'Оборудование:{self.title}'

    def get_absolute_url(self):
        return f'/equipment/'

    class Meta:
        verbose_name = 'Equipment'
        verbose_name_plural = 'Equipments'
