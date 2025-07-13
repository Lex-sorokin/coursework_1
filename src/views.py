import pprint

from src.utils import read_excel, extract_cards, hello_greeting, sort_by_sum, user_settings, get_currency_rates, \
    get_stock_prices


def start_main(date_time):
    df = read_excel('../data/operations.xlsx')
    settings_user = user_settings('../user_setting.json')
    print(settings_user)
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
        "stock_prices": stock_prices
    }
    return result

if __name__ == '__main__':

    pprint.pprint(start_main('2021-09-01 09:00:00'))
