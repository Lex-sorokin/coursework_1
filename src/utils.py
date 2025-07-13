import json
import os
from datetime import datetime
import numpy as np
import pandas as pd
import requests
from pandas import DataFrame
from dotenv import load_dotenv

load_dotenv()


def hello_greeting(date_time: str) -> str:
    """Функция, которая приветствует пользователя в зависимости от времени суток"""
    now = datetime.strptime(date_time, "%Y-%m-%d %H:%M:%S")
    result = ''
    if 0 < now.hour < 4 or 22 < now.hour < 24:
        result = 'Доброй ночи'
    elif 4 < now.hour < 10:
        result = 'Доброе утро'
    elif 10 < now.hour < 16:
        result = 'Добрый день'
    elif 16 < now.hour < 22:
        result = 'Добрый вечер'
    return result


def read_excel(file_path: str) -> DataFrame:
    """Функция, которая считывает финансовые операции из XLSX-файла."""
    df = pd.read_excel(file_path)
    return df.replace({np.nan: None})


def extract_cards(df: DataFrame) -> list[dict]:
    """Функция, которая обрабатывает данные из DataFrame и возвращает список словарей"""
    transaction_list = df.groupby('Номер карты').agg({'Сумма операции с округлением': 'sum'})
    list_cards = [{
        "last_digits": i[-4:],
        "total_spent": round(row['Сумма операции с округлением'], 2),
        "cashback": round(row['Сумма операции с округлением'] / 100, 2)
    } for i, row in transaction_list.iterrows()]
    return list_cards


def sort_by_sum(df) -> list[dict]:
    """Функция, которая возвращает Топ-5 транзакций по сумме платежа."""
    return_data = []
    ss = ['Дата платежа', 'Сумма платежа', 'Категория', 'Описание']
    result = df[ss][(df['Статус'] == 'OK')].sort_values("Сумма платежа", ascending=True).head()
    for i, row in result.iterrows():
        data = {
            "date": row['Дата платежа'],
            "amount": row['Сумма платежа'],
            "category": row['Категория'],
            "description": row['Описание']
        }
        return_data.append(data)
    return return_data


def user_settings(path: str) -> dict:
    """Функция, которая открывает .JSON файл с параметрами"""
    with open(path, encoding='utf8') as f:
        read_json = json.load(f)
    return read_json


def get_currency_rates(settings_user) -> list[dict]:
    """Функция, которая запрашивает актуальный курс валют по API."""
    data = []
    headers = {
        "apikey": os.getenv("API_KEY")
    }
    url = f"https://api.apilayer.com/exchangerates_data/2025-07-12"
    for currency in settings_user["user_currencies"]:
        payload = {
            "base": currency, "symbols": "RUB"
        }


        response = requests.get(url, headers=headers, params=payload)
        json_response = response.json()
        data.append({
            "currency": currency,
            "rate": json_response['rates']['RUB']
        })

    return data


def get_stock_prices(settings_user) -> list[dict]:
    pass
