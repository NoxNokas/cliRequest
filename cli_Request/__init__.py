from .config import Config
from .query import QueryCSV
from .log import logger


def main():
    # Парсим командрую строку
    try:
        Config.read_opts()
    except KeyError as exceptMsg:
        logger.error(msg=exceptMsg)

    # Получаем список номеров строк
    try:
        lines = QueryCSV.find_lines_number(Config.PATH, Config.COLUMN, Config.QUERY)
        print(lines)
    except KeyError:
        logger.error("column does not exist")
    except Exception as exc:
        logger.error(exc)
