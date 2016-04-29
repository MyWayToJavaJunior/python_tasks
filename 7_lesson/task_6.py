#!/usr/bin/python3

from datetime import date, datetime
import csv


class Person:

    def __init__(self, id, surname, name, birthdate, nickname=None):

        self.id = id
        self.surname = surname
        self.name = name
        if nickname is not None:
            self.nickname = nickname
        try:
            date_format = "%Y-%m-%d"
            date_object = datetime.strptime(birthdate, date_format)
            self.birthdate = date_object.date()
        except ValueError:
            raise ValueError("You must provide birth date in correct format "
                             "(YYYY-MM-DD)!")

    def get_age(self):
        today = date.today()
        delta_in_days = today - self.birthdate
        return str(int(delta_in_days.days // 365.25))

    def get_fullname(self):
        return "{0} {1}".format(self.surname, self.name)


def modifier(filename):

    with open(filename) as csvfile:
        dialect = csv.Sniffer().sniff(csvfile.read())
        csvfile.seek(0)
        reader = csv.reader(csvfile, dialect)
        for row in reader:
            print(row)

modifier('data.csv')










