import configargparse


class Config:
    """
    Класс реализующий cli
    """
    PATH: str = ""
    COLUMN: str = ""
    QUERY: str = ""

    @classmethod
    def read_opts(cls):
        p = configargparse.get_argument_parser()
        p.add_argument("--path", "-p", default=None, help="path to csv file")
        p.add_argument("--column", "-c", default=None, help="column from csv file")
        p.add_argument("--query", "-q", default=None, help="query for csv file")
        args = p.parse_args()

        if args.path is None:
            raise KeyError("Не указан путь до файла")
        cls.PATH = args.path

        if args.column is None:
            raise KeyError("Укажите столбец: --column")
        cls.COLUMN = args.column

        if args.query is None:
            raise KeyError("Укажите запрос: --query <query>")
        cls.QUERY = args.query
