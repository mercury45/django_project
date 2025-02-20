# Cake-Store
Проект для цифровой кафедры в Казанском федеральном университете.

Проект представляет собой сайт-магазин для заказа тортов на стеке:
- Django(Django REST Framework) (version 4.1.5)
- PostgreSQL
- REST API
- NoSQL (Redis)

## Запуск проекта для разработки

- `python -m venv env` - создание виртуального окружения
- `source env/bin/activate` - войти в виртуальное окружение на linux/macOS
- `env/Scripts/Activate.ps1` - войти в виртуальное окружение на Windows
- `pip install -r requirements.txt` - установка зависимостей
- `python manage.py runserver` - запустить сервер для разработки на http://127.0.0.1:8000