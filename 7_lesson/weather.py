#!/usr/bin/python3
""" Яндекс.Погода

Есть публичный урл со списком городов:
http://weather.yandex.ru/static/cities.xml

Для этих городов можно получить данные о погоде, подставив id города в шаблон:
http://export.yandex.ru/weather-ng/forecasts/<id города>.xml

Необходимо написать скрипт, который:
1. Создает файл базы данных SQLite с следующей структурой данных (если файла 
   базы данных не существует):

    Погода
        id                  INTEGER PRIMARY KEY
        Город               VARCHAR(255)
        Дата                DATE
        Температура днем    INTEGER
        Температура ночью   INTEGER

2. Скачивает и парсит XML со списком городов
3. Выводит список стран из файла и предлагает пользователю выбрать страну
4. Скачивает XML файлы погоды в городах выбранной страны
5. Парсит последовательно каждый из файлов и добавляет данные о погоде в базу
   данных. Если данные для данного города и данного дня есть в базе - обновить
   температуру в существующей записи.


Температура днем и температура ночью берется из 
forecast/day/day_part@day_short/temperature и 
forecast/day/day_part@night_short/temperature соответственно:

<forecast ...>
    <day date="...">
        <day_part typeid="5" type="day_short">
            <temperature>29</temperature> 
            ...
        </day_part>
        <day_part typeid="6" type="night_short">
            <temperature>18</temperature>
            ...
        </day_part>
    </day>
</forecast>

При повторном запуске скрипта:
- используется уже скачанный файл с городами
- используется созданная база данных, новые данные добавляются и обновляются

Важное примечание:

Доступ к данным в XML файлах происходит через простансво имен:
<forecast ... xmlns="http://weather.yandex.ru/forecast ...>

Чтобы работать с простанствами имен удобно пользоваться такими функциями:

# Получим пространство имен из первого тега:
def gen_ns(tag):
    if tag.startswith('{'):
        ns, tag = tag.split('}')
        return ns[1:]
    else:
        return ''

tree = ET.parse(f)
root = tree.getroot()

# Определим словарь с namespace
namespaces = {'ns': gen_ns(root.tag)}

# Ищем по дереву тегов
for day in root.iterfind('ns:day', namespaces=namespaces):
    ...

"""

import os
# import sys
import sqlite3
import urllib.request
from xml.etree import ElementTree as ET
# from collections import OrderedDict, namedtuple


# создание файла базы данных
def touch_db():

    db_filename = 'todo.db'

    if not os.path.exists(db_filename):

        with sqlite3.connect(db_filename) as conn:
            conn.execute("""
            create table погода (
            id        INTEGER PRIMARY KEY,
            City      VARCHAR(255),
            Date      DATE,
            TemperatureNight INTEGER,
            TemperatureDaytime INTEGER
            );
            """)


def parse_country_xml():
    path = '/home/timur/source/python/7_lesson'
    url = 'http://weather.yandex.ru/static/cities.xml'
    xml = 'city.xml'

    filename = os.path.join(path, xml)
    urllib.request.urlretrieve(url, filename)

    with open('city.xml', 'r', encoding='utf-8') as f:
        tree = ET.parse(f)

    country_list = []

    for node in tree.iter('country'):
        country_list.append(node.attrib['name'])

    return country_list


def parse_cities_xml(country):
    return


# tree = ET.parse(f)
# root = tree.getroot()
# print(parse_xml())


def main():

    touch_db()

    country_list = parse_country_xml()

    run = True

    while run:
        user_input = input('''---------------------------------\nВыберите страну из списка(q-выход):\n---------------------------------\n
        {}\n'''.format(', '.join(country_list)))
        if user_input == 'q':
            run = False
        elif user_input in country_list:
            print(user_input)
            run = False
        else:
            print('---------------------------------\nНекорректный ввод\n---------------------------------\n')


if __name__ == '__main__':
    main()
