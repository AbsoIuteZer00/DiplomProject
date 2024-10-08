from django.shortcuts import render
from .models import *
from .forms import CompanyRegister

# Create your views here.


def main(request):
    """Get-запрос на главную страницу"""
    title = 'ООО "ПО "Высота"'
    heading = 'Главная страница'
    context = {
        'title': title,
        'heading': heading
    }
    return render(request, 'main.html', context)


def catalog(request):
    """Get-запрос на страницу каталога"""
    title = 'ООО "ПО "Высота"'
    heading = 'Каталог'
    context = {
        'title': title,
        'heading': heading
    }
    return render(request, 'catalog.html', context)


def contacts(request):
    """Get-запрос на страницу контактной информации"""
    title = 'ООО "ПО "Высота"'
    heading = 'Контакты'
    context = {
        'title': title,
        'heading': heading
    }
    return render(request, 'contacts.html', context)


def description(request):
    """Get-запрос на страницу информации об организации"""
    title = 'ООО "ПО "Высота"'
    heading = 'О нас'
    context = {
        'title': title,
        'heading': heading
    }
    return render(request, 'description.html', context)


def company_view(request):
    """Post-запрос на страницу опросного листа"""
    if request.method == 'POST':
        form = CompanyRegister(request.POST)
        if form.is_valid():
            company = form.cleaned_data['company']
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            address = form.cleaned_data['address']
            phone = form.cleaned_data['phone']
            description = form.cleaned_data['description']
            Company.objects.create(
                        company=company,
                        name=name,
                        email=email,
                        address=address,
                        phone=phone,
                        description=description
            )
        return render(request, 'success.html')
    return render(request, 'company_form.html')
