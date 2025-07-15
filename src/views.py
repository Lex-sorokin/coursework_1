import json
import os

from config import ROOT_DIR
from src.utils import (
    extract_cards,
    get_currency_rates,
    get_stock_prices,
    hello_greeting,
    read_excel,
    sort_by_sum,
    user_settings
)


def start_main(date_time: str) -> str:
    """Функция, которая """
    df = read_excel(os.path.join(ROOT_DIR, "data", "operations.xlsx"))
    settings_user = user_settings(os.path.join(ROOT_DIR, "user_setting.json"))
    cards = extract_cards(df)
    greeting = hello_greeting(date_time)
    top_transactions = sort_by_sum(df)
    currency_rates = get_currency_rates(settings_user)
    stock_prices = get_stock_prices(settings_user)
    result = {
        "greeting": greeting,
        "cards": cards,
        "top_transactions": top_transactions,
        "currency_rates": currency_rates,
        "stock_prices": stock_prices,
    }
    return json.dumps(result, ensure_ascii=False)
