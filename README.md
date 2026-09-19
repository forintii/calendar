# Календарь заметок

Веб-приложение на Django для создания и структурирования заметок по датам.

##  Стек
- Python 3.x
- Django 5.1.4
- SQLite
- HTML, CSS
- Git


##  Функционал
- Регистрация и аутентификация пользователей
- Создание заметок с привязкой к датам и добавление цвета заметкам по своему усмотрению
- Просмотр и редактирование заметок в календаре
- Удаление заметок


##  Как запустить
1. Клонировать репозиторий:
   git clone https://github.com/ваш-логин/название-репозитория.git
   cd название-репозитория

2. Создать и активировать виртуальное окружение:
   python3 -m venv venv
   source venv/bin/activate

3. Установить зависимости:
   pip install -r requirements.txt

4. Создать файл `.env` в папке с `manage.py` и указать в нём:
   SECRET_KEY=ваш_секретный_ключ
   DEBUG=True

   Сгенерировать ключ можно командой:
   python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"

5. Применить миграции:
   python3 manage.py migrate

6. Запустить сервер разработки:
   python3 manage.py runserver

7. Открыть в браузере:
   http://127.0.0.1:8000/
