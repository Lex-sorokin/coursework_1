import json

from loger import module_logger

logger = module_logger(__name__)


def just_search(word: str, transaction: list[dict]) -> str:
    """Функция, которая возвращает JSON-ответ со всеми транзакциями, содержащими запрос в описании или категории."""
    logger.info("Функция just_search запущена")
    filter_transaction = filter(lambda x: (word in str(x["Категория"]) or word in str(x["Описание"])), transaction)
    result = json.dumps(list(filter_transaction), ensure_ascii=False, indent=4)
    logger.info("Функция успешно завершила работы")
    return result
