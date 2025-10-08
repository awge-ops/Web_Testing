# qa-ui-tests-saucedemo


Простой набор UI e2e-тестов для https://www.saucedemo.com на базе Playwright + pytest.


## Что внутри


- POM-структура
- Тесты авторизации: успешный вход, неверный пароль, закрытый пользователь
- GitHub Actions workflow для CI


## Требования


- Python 3.8+
- pip
- playwright


## Быстрый старт локально


1. Создать и активировать виртуальное окружение


python -m venv venv


source venv/bin/activate # Linux / macOS


venv\Scripts\activate # Windows


2. Установить зависимости


pip install -r requirements.txt


3. Установить браузеры playwright


playwright install


4. Запустить тесты


pytest tests/test_login.py -q


## CI


В репозитории есть workflow `.github/workflows/tests.yml`, который устанавливает зависимости, загружает браузеры и запускает pytest.


## Дальше


- Добавить тесты для корзины и чекаута
- Интегрировать Allure отчёты и публикацию артефактов
