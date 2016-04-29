#!/usr/bin/python3

""" Ремонт в квартире 

Есть квартира (2 комнаты и кухня). В квартире планируется ремонт: нужно 
поклеить обои, покрасить потолки и положить пол.

Необходимо рассчитать стоимость материалов для ремонта.

Из описания следуют следующие классы:
= Строительные материалы
  = Обои
  = Потолочная краска
  = Ламинат
= Комната
= Квартира

Подробнее, с методами (+) и атрибутами (-):
= Строительные материалы
  - площадь (кв. м)
  - цена за единицу (рулон, банку, упаковку)
  = Обои
    - ширина рулона
    - длина рулона
  = Потолочная краска
    - вес банки
    - расход краски
  = Ламинат
    - длина доски
    - ширина доски
    - кол-во досок в упаковке
= Комната
  - ширина
  - высота
  - длина
  - ширина окна
  - ширина двери
  + поклеить обои
  + покрасить потолок
  + положить пол
  + посчитать смету на комнату
  + при создании комнаты сразу передавать все атрибуты в конструктор __init__()
= Квартира
  - комнаты
  + добавить комнату
  + удалить комнату
  + посчитать смету на всю квартиру
  + при создании можно передать сразу все комнаты в конструктор

Необходимо создать стройматериалы, назначить им цены и размеры.
Создать комнаты, поклеить, покрасить и положить все на свои места.
Cоздать квартиру, присвоить ей комнаты и посчитать общую смету.

Подсказка: для округления вверх и вниз используйте:
import math
math.ceil(4.2)  # 5
math.floor(4.2) # 4

Примечание: Для простоты, будем считать, что обои над окном и над дверью 
не наклеиваются.
----------------

Дополнительно:
Сделать у объекта квартиры метод, выводящий результат в виде сметы:

[Комната: ширина: 3 м, длина: 5 м, высота: 2.4 м]
Обои        400x6=2400 руб.
Краска     1000x1=1000 руб.
Ламинат     800x8=6400 руб.
[Комната: ширина: 3 м, длина: 4 м, высота: 2.4 м]
Обои        400x5=2000 руб.
Краска     1000x1=1000 руб.
Ламинат     800x7=5600 руб.
[Кухня: ширина: 3 м, длина: 3 м, высота: 2.4 м]
Обои        400x4=1600 руб.
Краска     1000x1=1000 руб.
Ламинат     800x5=4000 руб.
---------------------------
Итого: 25000 руб.

"""
import math


class BuildMaterias:

    def __init__(self, area, unit_price):

        self.area = area
        self.unit_price = unit_price


class Wallpaper(BuildMaterias):

    def __init__(self, width, length, unit_price):
        super().__init__(width * length, unit_price)
        # self.width = width
        # self.length = length


class CeilingPaint(BuildMaterias):

    def __init__(self, weight, waste_paint, unit_price):
        super().__init__(weight/waste_paint, unit_price)
        # self.weight = weight
        # self.waste_paint = waste_paint


class Laminate(BuildMaterias):

    def __init__(self, width, length, count_boards, unit_price):
        super().__init__(width * length * count_boards, unit_price)
        # self.width = width
        # self.length = length
        # self.count_boards = count_boards


class Room:

    # names = ('width', 'length', 'height', 'width_window', 'width_door')

    def __init__(self, width, height, length, width_window, width_door):
        names = ('width', 'length', 'height', 'width_window', 'width_door')
        for name in names:
            setattr(self, name, locals()[name])
        # self.width_room = width_room
        # self.heigth_room = heigth_room
        # self.length_room = length_room
        # self.width_window = width_window
        # self.width_door = width_door

    def get_walls_area(self):
        return math.ceil(((self.width + self.length) * 2 - self.width_door - self.width_window) *
                         self.height)

    def get_celling_area(self):
        return math.ceil(self.width * self.length)

    def get_floor_area(self):
        return math.ceil(self.width * self.length)

    def set_walls_area(self, material):
        self.walls = material

    def set_celling_area(self, material):
        self.ceiling = material

    def set_floor_area(self, material):
        self.floor = material

    def get_material_price(self, surface):
        material = getattr(self, surface)
        surface_area_method = getattr(self, 'get_%s' % surface)
        count = math.ceil(surface_area_method() / material.area)
        return count * material.price

    def get_price(self):
        return (
            self.get_material_price('floor_area') +
            self.get_material_price('walls_area') +
            self.get_material_price('celling_area')
        )

    def __str__(self):
        return ('Room: width {} m, height {} m, length {} m'.format(
            self.width, self.height, self.length))


class Flat:

    def __init__(self, *rooms):

        self.rooms = list(rooms)

    def add_room(self, room):
        self.rooms.append(room)

    def del_room(self, room):
        self.rooms.remove(room)

    def get_price(self):
        return sum([room.get_price() for room in self.rooms])


def main():
    wallpaper = Wallpaper(20, 50, 200)
    paint = CeilingPaint(5, 100, 500)
    laminate = Laminate(1180, 155, 5, 500)

    room1 = Room(4, 6, 2.5, 1.5, 1.2)
    room1.set_walls_area(wallpaper)
    room1.set_celling_area(paint)
    room1.set_floor_area(laminate)

    room2 = Room(4, 6, 2.5, 1.5, 1.2)
    room2.set_walls_area(wallpaper)
    room2.set_celling_area(paint)
    room2.set_floor_area(laminate)


    flat = Flat(room1, room2)
    flat.add_room(room2)

    room1.get_material_price('floor_area')


if __name__ == '__main__':
    main()