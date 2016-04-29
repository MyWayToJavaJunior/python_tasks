#!/usr/bin/python3

# Реализовать класс Person, который отображает запись в книге контактов.
#  
# Класс имеет 4 атрибута:
# - surname - строка - фамилия контакта (обязательный)
# - first_name - строка - имя контакта (обязательный)
# - nickname - строка - псевдоним (опциональный)
# - birth_date - объект datetime.date (обязательный)
#  
# Каждый вызов класса должен создавать экземпляр (инстанс) класса с указанными
# атрибутами.
#  
# Также класс имеет 2 метода:
# - get_age() - считает возраст контакта в полных годах на дату вызова и
# возвращает строку вида: "27";
# - get_fullname() - возвращает строку, отражающую полное имя (фамилия + имя)
# контакта;
#
# Примечание:
# 1) смотрите документацию по модулю datetime;
# 2) при создании атрибута birth_date из строки типа "2014-12-31" необходимо:
# - определить какая информация нужна для создания объекта datetime.date,
# - получить эти данные из строки - разобрать ее (достать из нее отдельно,
# год, месяц, число),
# - на основании этой информации создать специальный объект datetime.date,
# - поместить этот спец.объект в атрибут экземпляра класса;

from datetime import date, datetime


class Person:

    def __init__(self, surname, first_name, birth_date, nickname=None):

        self.surname = surname
        self.first_name = first_name
        if nickname is not None:
            self.nickname = nickname
        try:
            date_format = "%Y-%m-%d"
            datetime_object = datetime.strptime(birth_date, date_format)
            self.birth_date = datetime_object.date()
        except ValueError:
            raise ValueError("You must provide birth date in correct format "
                             "(YYYY-MM-DD)!")

    def get_age(self):
        today = date.today()
        delta_in_days = today - self.birth_date
        return str(int(delta_in_days.days // 365.25))

    def get_fullname(self):
        return '{} {}'.format(self.surname, self.first_name)

john = Person('Safin', 'Timur', '1996-08-28', 'unnamed' )

print(john.get_fullname())
print(john.get_age())
