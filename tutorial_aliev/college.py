#!/usr/bin/python3
# -*- coding: utf-8 -*-


class PersonCollege:
    """docstring for Person - fullname, age, nationality"""
    def __init__(self, fullname, age, gender, nationality, faculty, subjects, scientific_research):
        self.fullname = fullname
        self.age = age
        self.nationality = nationality
        self.faculty = faculty


class Professor(PersonCollege):
    """docstring for Professor"""
    def __init__(self, fullname, age, gender, nationality, faculty, subjects, scientific_research, work_experience):
        PersonCollege.__init__(self, fullname, age, gender, nationality, faculty, subjects, scientific_research)


class Students(PersonCollege):
    """docstring for Professor"""
    def __init__(self, fullname, age, gender, nationality, faculty, subjects, scientific_research, number_course, academic_perfomance):
        PersonCollege.__init__(self, fullname, age, gender, nationality, faculty, subjects, scientific_research)