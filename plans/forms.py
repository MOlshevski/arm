from .models import Plans
from django.forms import ModelForm, TextInput, Textarea


class PlansForm(ModelForm):
    class Meta:
        model = Plans
        fields = ['title', 'body', 'time']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Мой план'
            }),
            'body': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Описание плана'
            }),
            'time': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дедлайн'
        })
                }
