from .models import Workers
from django.forms import ModelForm, TextInput, DateInput, Select, FloatField, MultipleChoiceField


class WorkersForm(ModelForm):
    class Meta:
        model = Workers
        fields = ['surname', 'firstname', 'midname', 'bday', 'profession', 'division', 'adress', 'manager',
                  'training_start', 'training_end', 'exam', 'medical', 'dangerous_factors',
                  'condition_class', 'frequency']

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
            'profession': Select(attrs={
                'class': 'form-control',
                'placeholder': 'Профессия'
            }),
            'division': Select(attrs={
                'class': 'form-control',
                'placeholder': 'Структурное подразделение'
            }),
            'adress': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Адресс'
            }),
            'manager': Select(attrs={
                'class': 'form-control',
                'placeholder': 'Руководитель стажировки'
            }),
            'training_start': DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата начала стажировки'
            }),
            'training_end': DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата окончания стажировки'
            }),
            'exam': DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата текущей проверки знаний'
            }),
            'medical': DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата текущего мед. осмотра'
            }),
            'dangerous_factors': Select(attrs={
                'class': 'form-control',
                'placeholder': 'Опасные факторы'
                }),
            'condition_class': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Класс условий труда'
            }),
            'frequency': Select(attrs={
                'class': 'form-control',
                'placeholder': 'Периодичность проведения медицинского осмотра'
            }),
        }
