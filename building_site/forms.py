from .models import Sites
from django.forms import ModelForm, TextInput, DateInput, Select, Textarea


class SitesForm(ModelForm):
    class Meta:
        model = Sites
        fields = ['title', 'body', 'contract_type', 'contract_number', 'contract_date', 'manager_main', 'manager_line']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Строительный объект'
            }),
            'body': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Наименование объекта'
            }),
            'contract_type': Select(attrs={
                'class': 'form-control',
                'placeholder': 'Работы ведутся по:'
            }),
            'contract_number': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Номер договора'
            }),
            'contract_date': DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата составления договора'
            }),
            'manager_main': Select(attrs={
                'class': 'form-control',
                'placeholder': 'Общее руководство'
            }),
            'manager_line': Select(attrs={
                'class': 'form-control',
                'placeholder': 'Линейный руководитель'
            }),
                }
