# Auto_tests_for_portfolio

Автоматизированные тесты для портфолио, основанные на курсе Stepik: [https://stepik.org/course/575](https://stepik.org/course/575)

## 📘 Описание

Этот проект представляет собой набор автоматизированных тестов для веб-приложения, реализованный с использованием Python, Selenium и Pytest. Он охватывает основные аспекты тестирования веб-приложений, включая:

- Регистрацию и авторизацию пользователей
- Добавление товаров в корзину
- Проверку отображения сообщений об успешных действиях
- Проверку корректности отображаемых данных (цен, названий товаров)

Проект служит практическим примером для демонстрации навыков автоматизированного тестирования.

## ⚙️ Технологии

- Python 3.13+
- Selenium WebDriver
- Pytest
- Page Object Model (POM)
- Регулярные выражения (для извлечения данных из текста)

## 🚀 Установка

1. Клонируйте репозиторий:

```bash
git clone https://github.com/Bahalwik/Stepik_Selenium.git
cd Stepik_Selenium
```

2. Установите зависимости:
   
```bash
pip install -r requirements.txt
```

## ▶️ Запуск тестов

Все тесты сразу:

```bash
pytest -v --tb=line --language=en 
```


Все тесты с фикстурой need_review:

```bash
pytest -v --tb=line --language=en -m need_review
```

Отдельный тест (пример):
```bash
pytest -v --tb=short --language=ru -k "test_user_can_add_product_to_basket"
```
