"""
Иногда в базовом классе удобно описать название метода и зарезать ошибку,
чтоб наследники этого класса гарантировано перекрыли эту ошибку своей логикой.
"""


class Venicle(object):
    """docstring for Venicle"""

    milage = 0

    def __init__(self, arg):
        self.arg = arg

    def add_millage(self, new_millage):
        raise NotImplementedError


class Car(Venicle):
    """docstring for Car"""
    seating_count = 0

    def add_millage(self, new_millage):
        self.millage += new_millage
