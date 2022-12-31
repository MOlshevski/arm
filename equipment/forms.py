from .models import Equipments
from django.forms import ModelForm, TextInput, Textarea


class EquipmentsForm(ModelForm):
    class Meta:
        model = Equipments
        fields = ['title', 'body', 'time']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Оборудование'
            }),
            'body': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Описание оборудования'
            }),
            'time': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата текущей проверки'
        })
                }
