# SauceDemo Automation Project

Проект автоматизации тестирования UI для сайта [SauceDemo](https://www.saucedemo.com/).

## Стек технологий
* **Язык**: Python 3.14+
* **Фреймворк**: Pytest
* **Библиотека**: Selenium
* **Отчеты**: Allure Framework

## Инструкция по установке
1. Установите Java (необходима для работы Allure).
2. Установите зависимости проекта:
   ```bash
   python -m pip install -r requirements.txt
   ```

## Запуск тестов
Для запуска тестов и сбора данных для отчета выполните:
```bash
python -m pytest --alluredir=allure-results
```

## Генерация отчета
Для просмотра интерактивного отчета Allure в браузере:
```bash
allure serve allure-results
```

## Автор
**Айнур Кутов**
