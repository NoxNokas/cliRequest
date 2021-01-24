from .config import Config
from .query import QueryCSV
from .log import logger


def main():
    try:
        Config.read_opts()  # Парсим командрую строку
        lines = QueryCSV.find_lines_number(Config.PATH, Config.QUERY)
        print(lines)
    except KeyError as exceptMsg:
        logger.error(msg=exceptMsg)

