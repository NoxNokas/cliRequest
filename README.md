# Репозиторий с заданием к экзамену

Автор: Альберт Халгатян

***

### Задание:


Использую package configargparser напишите cli инструмент для поиска данных внутри csv файлов
```shell script
$ <program> --path <путь до csv> [query]
```
Вывод: номер строки что нашел (может быть несколько)

***
### Реализованная программа
В проекте используется Poetry с его встроенным виртуальным окружением.

Чтобы активировать окружение, нужно зайти в папку с проектом и прописать в консоли:
```shell script
$ poetry shell
```

Работа с консолью:
```shell script
$ python main.py -p <путь до файла> -c <наименование колонки> -r <регулярное выражение>
```
или
```shell script
$ python main.py -p <путь до файла> -c <наименование колонки> -q <строка>
```

Пример regex:
```shell script
$ python main.py -p test.csv -c first -r [A][l][b][e][r][t]
```

Пример query:
```shell script
$ python main.py -p test.csv -c first -q Albert
```