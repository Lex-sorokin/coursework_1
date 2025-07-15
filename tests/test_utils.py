from typing import Any
from unittest.mock import mock_open, patch

import numpy as np
import pytest
from pandas import DataFrame

from src.utils import (
    extract_cards,
    get_currency_rates,
    get_stock_prices,
    hello_greeting,
    read_excel,
    sort_by_sum,
    user_settings
)


@pytest.mark.parametrize(
    "date, expect",
    [
        ("2021-12-01 23:00:00", "Доброй ночи"),
        ("2021-12-01 09:00:00", "Доброе утро"),
        ("2021-12-01 13:00:00", "Добрый день"),
        ("2021-12-01 18:00:00", "Добрый вечер"),
    ],
)
def test_hello_greeting(date: str, expect: str) -> None:
    """Тест для функции hello_greeting."""
    assert hello_greeting(date) == expect


@patch("pandas.read_excel")
def test_read_excel(mock_read_excel: Any) -> None:
    """Тест для функции read_excel."""
    mock_read_excel.return_value.replace.return_value = ""
    assert read_excel("") == ""


def test_extract_cards(fixture_cards: list[dict]) -> None:
    """Тест для функции extract_cards."""
    assert extract_cards(DataFrame(fixture_cards)) == [
        {"cashback": np.float64(41908.96), "last_digits": "7197", "total_spent": np.float64(4190896.25)}
    ]


def test_sort_by_sum(transactions: DataFrame) -> None:
    """Тест для функции sort_by_sum."""
    assert sort_by_sum(transactions) == [
        {"amount": -252.0, "category": "Такси", "date": "22.09.2021", "description": "Яндекс Такси"},
        {"amount": -152.0, "category": "Такси", "date": "15.11.2021", "description": "Яндекс Такси"},
        {"amount": -105.0, "category": "", "date": "16.11.2021", "description": "Яндекс Такси"},
    ]


def test_user_settings() -> None:
    """Тест для функции user_settings."""
    with patch("builtins.open", mock_open(read_data="{}")):
        assert user_settings("") == {}


def test_get_currency_rates(setting_user: dict) -> None:
    """Тест для функции get_currency_rates."""
    with patch("requests.get") as mock:
        mock.return_value.json.return_value = {"rates": {"RUB": 1}}
        assert get_currency_rates(setting_user) == [{"currency": "USD", "rate": 1}, {"currency": "EUR", "rate": 1}]


def test_get_stock_prices(setting_user: dict) -> None:
    """Тест для функции get_stock_prices."""
    with patch("requests.get") as mock:
        mock.json.return_value = {"Global Quote": {"05. price": 1}}
        assert get_stock_prices(setting_user) == [
            {"price": 1.0, "stock": "AAPL"},
            {"price": 1.0, "stock": "AMZN"},
            {"price": 1.0, "stock": "GOOGL"},
            {"price": 1.0, "stock": "MSFT"},
            {"price": 1.0, "stock": "TSLA"},
        ]
