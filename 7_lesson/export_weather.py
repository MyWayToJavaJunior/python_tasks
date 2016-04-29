#!/usr/bin/python3

""" Яндекс.Погода (экспорт)

Сделать скрипт, экспортирующий данные из базы данных погоды, 
созданной скриптом weather.py. Экспорт происходит в формате CSV или JSON.

Скрипт запускается из коммандной строки и получает на входе:
export_weather.py --csv filename [<город>]
export_weather.py --json filename [<город>]

Экспорт происходит в файл filename.
Опционально можно задать в коммандной строке город. В этом случае 
экспортируются только данные по указанному городу. Если города нет в базе -
выводится соответствующее сообщение.


"""

import csv
import json
import sys


def csv_data(filename):
    return


def json_data(filename):
    return


def main():

    args = sys.argv[1:]

    filename = args[1]

    if args[0] == '--csv':
        csv_data(filename)
    elif args[0] == '-json':
        json_data(filename)


if __name__ == '__main__':
    main()
