from django.db import models


class Plans(models.Model):
    title = models.CharField('Мой план', max_length=100)
    body = models.TextField('Описание плана')
    time = models.CharField('Дедлайн', max_length=25)

    def __str__(self):
        return f'План:{self.title}'

    def get_absolute_url(self):
        return f'/plans/'

    class Meta:
        verbose_name = 'Plan'
        verbose_name_plural = 'Plans'
