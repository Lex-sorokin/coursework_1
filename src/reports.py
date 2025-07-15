import json
from datetime import datetime
from typing import Optional

import pandas as pd
from dateutil.relativedelta import relativedelta
from pandas import DataFrame

from loger import module_logger
from src.decorators import log

logger = module_logger(__name__)


@log()
def spending_by_category(transactions: DataFrame, category: str, date_time: Optional[str] = None) -> str:
    """Функция возвращает траты по заданной категории за последние три месяца от переданной даты."""
    logger.info("Функция spending_by_category запущена")
    if isinstance(date_time, str):
        f_date_time = datetime.strptime(date_time, "%Y-%m-%d %H:%M:%S")
    else:
        f_date_time = datetime.now()

    new_date = f_date_time - relativedelta(months=3)
    df = transactions
    df["Дата операции"] = pd.to_datetime(df["Дата операции"], errors="coerce", dayfirst=True)
    col_date_operation = "Дата операции"
    tr_sort_data: DataFrame = df[
        (df[col_date_operation] >= new_date) & (df[col_date_operation] <= f_date_time) & (df["Категория"] == category)
    ]
    result = [
        {
            "date": row["Дата операции"].strftime("%Y-%m-%d"),
            "sum_amount": row["Сумма операции с округлением"],
            "category": row["Категория"],
            "description": row.get("Описание", "-"),
        }
        for _, row in tr_sort_data.iterrows()
    ]

    logger.info("Функция успешно завершила работы")
    return json.dumps(result, ensure_ascii=False)
