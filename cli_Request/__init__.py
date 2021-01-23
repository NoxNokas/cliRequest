from .config import Config
from .query import QueryCSV


def main():
    Config.read_opts()  # Парсим командрую строку
    lines = QueryCSV.find_lines_number(Config.PATH, Config.QUERY)
    print(lines)