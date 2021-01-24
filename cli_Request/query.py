class QueryCSV:

    @classmethod
    def find_lines_number(cls, path, query) -> list:
        """

        Функция для поиска вхождения указанной
        последовательности символов в каждой строке csv файла

        :param path: путь до csv файла
        :param query: запрос к v файлу
        :return: возвращает  массив состоящий из номеров строк
        """

        lines = list()  # Номера прошедших валидацию строк
        index = 1
        with open(path) as csv_file:
            for line in csv_file:
                if query in line:
                    lines.append(index)
                index += 1
        return lines
