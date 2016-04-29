#!/usr/bin/python3
# перечисление

from re import findall


class Person:

    def __init__(self, id, age, gender):

        self.id = id
        self.age = age
        self.gender = gender

    def __repr__(self):
        return 'age:{}, gender:{}, id:{}'.format(self.age, self.gender, self.id)


def eql_age(filename):

    f = open(filename, 'r')

    data_file = findall(r'(\d)\s(\d+)\s(м)', f.read())
    person_list = [Person(int(i[0]), int(i[1]), i[2]) for i in data_file]

    res = max(person.age for person in person_list)

    for person in person_list:
    
        if person.age == res:

            print(person.id)
            break

    print(res)

eql_age('input.txt')
