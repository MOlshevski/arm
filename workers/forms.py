from .models import Workers
from django.forms import ModelForm, TextInput


class WorkersForm(ModelForm):
    class Meta:
        model = Workers
        fields = ['surname', 'firstname', 'midname', 'bday', 'profession', 'division', 'adress']

        widgets = {
            'surname': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Фамилия'
            }),
            'firstname': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя'
            }),
            'midname': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Отчество'
            }),
            'bday': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата рождения'
            }),
            'profession': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Профессия'
            }),
            'division': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Структурное подразделение'
            }),
            'adress': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Адресс'
            }),

                }
