import os
from typing import Any, Callable

from config import ROOT_DIR


def write_log(message: str, filename: str) -> None:
    """
    Функция, которая записывает результат выполнения функции foo() в файл.
    """

    with open(os.path.join(ROOT_DIR, "data", filename), "a", encoding="utf-8") as f:
        f.write(str(message))


def log(filenane: str = "log.txt") -> Callable:
    """
    Декоратор для логирования функции с настройками.
    """

    def decorator(func: Callable) -> Callable:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            result = func(*args, **kwargs)
            write_log(result, filenane)
            return result

        return wrapper

    return decorator
