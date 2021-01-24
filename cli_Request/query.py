import numpy as np
import pandas as pd
import re


class QueryCSV:

    @staticmethod
    def find_lines_number(path: str, column: str, query: str):
        """

        Функция для поиска вхождения указанной
        последовательности символов в каждой строке csv файла

        :param path: путь до csv файла
        :param column: имя столбца в котором осуществляется поиск
        :param query: запрос к csv файлу
        :return: возвращает  массив состоящий из индексов строк
        """

        chunksize = 10 ** 3
        df = pd.read_csv(path, chunksize=chunksize)

        for chunk in df:
            temp_str = chunk[query == chunk[column]].index.tolist()
            if len(temp_str):
                for i in temp_str:
                    yield i

    @staticmethod
    def rg_find_lines_number(path: str, column: str, query: str):
        """

        Функция для поиска вхождения указанного
        регулярного выражения в каждой строке csv файла

        :param path: путь до csv файла
        :param column: имя столбца в котором осуществляется поиск
        :param query: запрос к csv файлу
        :return: возвращает  массив состоящий из индексов строк
        """

        chunksize = 10 ** 3
        df = pd.read_csv(path, chunksize=chunksize)

        # regex = re.compile('[A][l][b][e][r][t]')       [A][l]+[\w]+[a]
        regex = re.compile(query)

        for chunk in df:
            d = [i for i in map(regex.findall, chunk[column]) if i]
            a = np.array(d, dtype=str).ravel().tolist()
            a = list(set(a))

            temp_str = chunk[chunk[column].isin(a)].index.tolist()
            if len(temp_str):
                for i in temp_str:
                    yield i
