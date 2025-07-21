import os.path

from pandas import DataFrame

from config import ROOT_DIR
from src.decorators import log
from src.reports import spending_by_category


def test_spending_by_category(transactions: DataFrame) -> None:
    """Тест для функции spending_by_category."""
    assert spending_by_category(transactions, "Такси", "2021-12-01 09:00:00") == (
        '[{"date": "2021-11-14", "sum_amount": 152.0, "category": "Такси", '
        '"description": "Яндекс Такси"}, {"date": "2021-09-20", "sum_amount": 252.0, '
        '"category": "Такси", "description": "Яндекс Такси"}]'
    )

    assert spending_by_category(transactions, "Такси") == "[]"

    @log("test.txt")
    def add_(a: int, b: int) -> int:
        return a + b

    add_(1, 2)
    f = open(os.path.join(ROOT_DIR, "data", "test.txt"))
    assert "3" in f.read()
    f.close()
