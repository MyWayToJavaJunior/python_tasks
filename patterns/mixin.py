"""
Множественное наследование - "Подмешивает" свой функционал не меняя
функционал базового класса Car отрабатывает свой init, далее видит super,
сначала идет в LicenseMixin, LicenseMixin отрабатывает
init, далее идет в базовый класс Venicle, тот тоже отрабатывает свои init
"""


class Venicle(object):
    """docstring for Venicle"""

    def __init__(self, brand):
        self.brand = brand


class LicenseMixin(object):
    """docstring for LicenseMixin"""
    def __init__(self, *args, **kwargs):
        super(LicenseMixin, self).__init__(*args, **kwargs)
        self.license = kwargs.get('license')


class Car(LicenseMixin, Venicle):
    """docstring for Car"""
    def __init__(self, brand, seat_cnt, *args, **kwargs):
        super(Car, self).__init__(brand, *args, **kwargs)
        self.seating_count = seat_cnt
