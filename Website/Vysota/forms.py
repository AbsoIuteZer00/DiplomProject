from django.forms import ModelForm, Textarea
from .models import Company


class CompanyRegister(ModelForm):
    """Класс определения названий в админ-панели"""
    class Meta:
        model = Company
        fields = '__all__'
        labels = {
            'company': 'Название организации',
            'name': 'Контактное лицо',
            'email': 'email',
            'address': 'Адрес',
            'phone': 'Номер телефона',
            'description': 'Комментарий',
        }
