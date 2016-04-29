#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Вам дается последовательность целых чисел и вам нужно ее обработать
и вывести на экран сумму первой пятерки чисел из этой последовательности,
затем сумму второй пятерки, и т. д. Но последовательность не дается
вам сразу целиком. С течением времени к вам поступают её
последовательные части. Например, сначала первые три элемента,
потом следующие шесть, потом следующие два и т. д. Реализуйте класс Buffer,
который будет накапливать в себе элементы последовательности и выводить
сумму пятерок последовательных элементов по мере их накопления.
Одним из требований к классу является то, что он не должен хранить
в себе больше элементов, чем ему действительно необходимо,
т. е. он не должен хранить элементы, которые уже вошли в пятерку,
для которой была выведена сумма.
"""
# if len(self.current_list) >= 5:
#     o1 = sum(self.current_list[x] for x in range(5))
    # print(output_list, o1)
    # self.current_list = self.current_list[5:]
# else:

class Buffer:
    def __init__(self):
        self.current_list = []

    def add(self, *a):
        self.current_list = self.current_list + list(a)

        while len(self.current_list) >= 5:
            output_list = sum(self.current_list[x] for x in range(5))
            self.current_list = self.current_list[5:]
            print(output_list)

    def get_current_part(self):
        return self.current_list

buf = Buffer()
buf.add(1, 2, 3)
buf.get_current_part() # вернуть [1, 2, 3]
buf.add(4, 5, 6) # print(15) – вывод суммы первой пятерки элементов
buf.get_current_part() # вернуть [6]
buf.add(7, 8, 9, 10) # print(40) – вывод суммы второй пятерки элементов
buf.get_current_part() # вернуть []
buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1) # print(5), print(5) – вывод сумм третьей и четвертой пятерки
buf.get_current_part() # вернуть [1]
