# Приложение для анализа банковских операций.

## Данное приложение предназначено для анализа транзакций, которые находятся в Excel-файле.
## Приложение будет:
1. Генерировать JSON-данные для веб-страниц;
2. Формировать Excel-отчеты;
3. Осуществлять простой поиск по транзакциям;
4. Формировать отчёты по заданной категории за последние три месяца



## Установка


1. Клонируйте репозиторий:

git clone
git@github.com:Lex-sorokin/coursework_1.git

2. Перейдите в директорию проекта:

C:\Users\Lex\PycharmProjects\coursework_1


3. Установите необходимые зависимости:

poetry install

Линтеры и библиотеки согласно pyproject.toml

# Пример использования

1. **Пример: Отчет по категории**
```
Введите категорию: Супермаркеты
=== Отчет: Траты по категории 'Супермаркеты' ===
[
  {
    "date": "2024-12-01",
    "amount": -400.0,
    "description": "Перекресток"
  },
  {
    "date": "2024-12-02",
    "amount": -500.0,
    "description": "Metro"
  },
  ...
]
```

## Структура проекта:
.
├── src
│ ├── __init__.py
│ ├── utils.py
│ ├── decorators.py
│ ├── views.py
│ ├── reports.py
│ └── services.py
├── data
│ ├── operations.xlsx
├── tests
│ ├── __init__.py
│ ├── conftest.py
│ ├── test_utils.py
│ ├── test_views.py
│ ├── test_reports.py
│ └── test_services.py
├── user_settings.json
├── .env
├── .env.exemple
├── .idea/
├── .flake8
├── .gitignore
├── config.py
├── loger.py
├── pyproject.toml
├── poetry.lock
└── README.md


## Модуль views.py содержит функцию start_main, которая объединяет все модули проекта.

## Тесты

Покрытие тестами 100%
