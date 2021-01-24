import configargparse


class Config:
    """
    Класс реализующий cli
    """
    PATH: str = ""
    COLUMN: str = ""
    QUERY: str = ""
    REGEX: str = ""

    @classmethod
    def read_opts(cls):
        p = configargparse.get_argument_parser()
        p.add_argument("--path", "-p", default=None, help="path to csv file")
        p.add_argument("--column", "-c", default=None, help="column from csv file")
        p.add_argument("--query", "-q", default=None, help="query for csv file")
        p.add_argument("--regex", "-r", default=None, help="regex for csv file")
        args = p.parse_args()

        if args.path is None:
            raise KeyError("Не указан путь до файла")
        cls.PATH = args.path

        if args.column is None:
            raise KeyError("Укажите столбец: --column")
        cls.COLUMN = args.column

        if args.query or args.regex:
            cls.QUERY = args.query
            cls.REGEX = args.regex
        elif args.query and args.regex:
            raise KeyError("Укажите что-то одно: --query <string> или --regex <regex>")
        else:
            raise KeyError("Укажите строку запроса: --query <string> или --regex <regex>")
