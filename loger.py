import logging
import os.path

from config import ROOT_DIR


def module_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    path = str(os.path.join(ROOT_DIR, "logs", name.split(".")[1] + ".log"))
    file_handler = logging.FileHandler(path, "w", "utf-8")
    file_formatter = logging.Formatter(f"%(asctime)s %(filename)s %(levelname)s: модуль {name} %(message)s")
    file_handler.setFormatter(file_formatter)
    logger.addHandler(file_handler)
    logger.setLevel(logging.DEBUG)
    return logger
