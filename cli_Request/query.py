import pandas as pd


class QueryCSV:

    @classmethod
    def find_lines_number(cls, path: str, column: str, query: str) -> list:
        """

        Функция для поиска вхождения указанной
        последовательности символов в каждой строке csv файла

        :param path: путь до csv файла
        :param column: имя столбца в котором осуществляется поиск
        :param query: запрос к v файлу
        :return: возвращает  массив состоящий из номеров строк
        """

        chunksize = 10 ** 3
        lines = list()  # Номера прошедших валидацию строк
        df = pd.read_csv(path, chunksize=chunksize)

        for chunk in df:
            temp_str = chunk[query == chunk[column]].index
            if temp_str.size:
                for i in temp_str:
                    lines.append(i)

        return list(lines)
