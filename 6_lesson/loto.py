#!/usr/bin/python3

"""Лото

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа,
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
случайная карточка.

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.

Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71
--------------------------
-- Карточка компьютера ---
 7 87     - 14    11
      16 49    55 88    77
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать
модуль random: http://docs.python.org/3/library/random.html

"""



import random
import sys

KEG_NUMBER = 90
EMPTY_NUMBER = ''
STRIKED = '-'


# генератор
def get_bag():

    keg_list = range(1, KEG_NUMBER + 1)
    random.shuffle(keg_list)
    while keg_list:
        yield keg_list.pop()


class Card:

    """Класс для карточки"""

    def __init__(self, name):
        self.arg = name
        self.rows = [[EMPTY_NUMBER] * 9,
                     [EMPTY_NUMBER] * 9,
                     [EMPTY_NUMBER] * 9]
        bag = get_bag()

        for row in self.rows:
            numbers = []
            for i in range(5):
                numbers.append(next(bag))
            numbers.sort()
            index_list = sorted(random.sample(range(0, 9), 5))
            for index in index_list:
                row[index] = numbers.pop(0)

    def __str__(self):
        res = []
        res.append('{:-^26}'.format(self.name))

        for row in self.rows:
            res.append(' '.join(['{:>2}'.format(x) for x in row]))

        res.append('-' * 26)

        return '\n'.join(res)

    def _numbers_inline(self):
        res = []
        for row in self.rows:
            for x in row:
                if x != EMPTY_NUMBER and x != STRIKED:
                    res.append(x)
        return res

    def strike(self, keg):

        for row in self.rows:
            for i, x in enumerate(row):
                if x == keg:
                    row[i] = STRIKED

    def __len__(self):

        # res = 0
        # for row in self.rows:
        #     for x in row:
        #         if x != EMPTY_NUMBER and x != STRIKED:
        #             res += 1
        return len(self._numbers_inline())

    def is_empty(self):
        return False if len(self) else True

    def __contains__(self, number):
        return number in self._numbers_inline()


# главня функия main
def main():

    player_card = Card('Игрок')
    computer_card = Card('Компьютер')

    bag = get_bag(KEG_NUMBER)

    for i, next_keg in enumerate(bag):
        print('Новый бочонок: {} (осталось {})'.format(next_keg, KEG_NUMBER - i - 1))
        print(player_card)
        print(computer_card)

        while True:

            user_input = input('Зачеркнуть цифру? (y/n)\n')
            if user_input not in ('y', 'n'):
                break
        if user_input == 'y':
            if next_keg not in player_card:
                print('числа {} нет на вашей карточе. Вы проиграли'.format(next_keg))
                return
            else:
                player_card.strike(next_keg)
        else:
            if next_keg in player_card:
                print('число {} на вашей карточе. Вы проиграли'.format(next_keg))
                return
        computer_card.strike(next_keg)

        if player_card.is_empty() or computer_card.is_empty():
            if not computer_card.is_empty():
                print('Вы выиграли!')
            elif not player_card.is_empty():
                print('Вы проиграли')
            else:
                print('Ничья')
            return


if __name__ == '__main__':
    main()
