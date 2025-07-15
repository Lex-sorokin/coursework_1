from typing import Any
from unittest.mock import patch

from src.views import start_main


@patch("requests.get")
def test_start_main(requests_get: Any) -> None:
    """Тест для функции start_main."""
    requests_get.return_value.json.return_value = {"rates": {"RUB": 1}, "Global Quote": {"05. price": 1}}
    assert start_main("2021-12-01 09:00:00") == (
        '{"greeting": "Доброе утро", "cards": [{"last_digits": "1112", "total_spent": '
        '46207.08, "cashback": 462.07}, {"last_digits": "4556", "total_spent": '
        '4144689.17, "cashback": 41446.89}, {"last_digits": "5091", "total_spent": '
        '19816.84, "cashback": 198.17}, {"last_digits": "5441", "total_spent": '
        '470854.8, "cashback": 4708.55}, {"last_digits": "5507", "total_spent": '
        '84000.0, "cashback": 840.0}, {"last_digits": "6002", "total_spent": 69200.0, '
        '"cashback": 692.0}, {"last_digits": "7197", "total_spent": 2557824.54, '
        '"cashback": 25578.25}], "top_transactions": [{"date": "21.03.2019", '
        '"amount": -190044.51, "category": "Переводы", "description": "Перевод '
        'Кредитная карта. ТП 10.2 RUR"}, {"date": "23.10.2018", "amount": -177506.03, '
        '"category": "Переводы", "description": "Перевод Кредитная карта. ТП 10.2 '
        'RUR"}, {"date": "19.09.2018", "amount": -152500.0, "category": '
        '"Образование", "description": "СКОЛКОВО"}, {"date": "02.12.2018", "amount": '
        '-152500.0, "category": "Образование", "description": "СКОЛКОВО"}, {"date": '
        '"18.01.2019", "amount": -152500.0, "category": "Образование", "description": '
        '"СКОЛКОВО"}], "currency_rates": [{"currency": "USD", "rate": 1}, '
        '{"currency": "EUR", "rate": 1}], "stock_prices": [{"stock": "AAPL", "price": '
        '1.0}, {"stock": "AMZN", "price": 1.0}, {"stock": "GOOGL", "price": 1.0}, '
        '{"stock": "MSFT", "price": 1.0}, {"stock": "TSLA", "price": 1.0}]}'
    )
