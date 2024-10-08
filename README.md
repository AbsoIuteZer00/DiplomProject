# DiplomProject

Инструкция актуальна для Windiws-систем.
Используемые технологии: python~=3.9 Django~=5.1.1 FastAPI~=0.115.0 Flask~=3.0.3

Скопируйте репозиторий с помощью команды: git clone https://github.com/AbsoIuteZer00/DiplomProject.git 
Перейдите в директорию проекта Django с помощью команды: cd Website
Перейдите в директорию проекта Flask с помощью команды: cd Flask
Перейдите в директорию проекта FastAPI с помощью команды: cd FastAPI

Создать и активировать виртуальное окружение:
pip install -r requirements.txt

Перейти в Website директорию
Для запуска выполнить следующие команды: Команда для создания миграций приложения для базы данных: python manage.py makemigrations  python manage.py migrate

Создание суперпользователя python manage.py createsuperuser

Будут выведены следующие выходные данные: Введите требуемое имя пользователя, электронную почту и пароль.

Например: Username (leave blank to use 'admin'): admin Email address: admin@admin.com Password: ******** Password (again): ******** Superuser created successfully.

Команды для запуска приложения Django: python manage.py runserver
Django-приложение будет доступно по адресу: http://127.0.0.1:8000/

Команда для запуска приложения FastAPI: uvicorn
FastAPI-приложение будет доступо по адресу: http://127.0.0.1:8000/

Приложение Flask запускается через main.py
Flask-приложение будет доступно по адресу: http://127.0.0.1:8000/
