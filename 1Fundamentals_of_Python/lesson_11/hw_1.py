from random import randint, sample

import pandas as pd


class LotoCard:
    def __init__(self, player_type):
        self.player_type = player_type
        self.card = [
            [],
            [],
            []
        ]
        self._MAX_NUMBER = 90
        self.MAX_NUMBER_IN_CARD = 15
        self._numbers_stroked = 0
        NEED_SPACES = 4
        NEED_NUMBERS = 5
        self._numbers = sample(range(1, self._MAX_NUMBER), self.MAX_NUMBER_IN_CARD)

        for line in self.card:
            for _ in range(NEED_SPACES):
                line.append('  ')
            for _ in range(NEED_NUMBERS):
                line.append(self._numbers.pop())

        def check_sort_item(item):
            if isinstance(item, int):
                return item
            else:
                return randint(1, self._MAX_NUMBER)

        for index, line in enumerate(self.card):
            self.card[index] = sorted(line, key=check_sort_item)

    def __str__(self):
        return f'{self.player_type:-^26}\n' \
               f'{pd.DataFrame(self.card).to_string(index=False, header=False)}\n' \
               f'{"-":-^26}\n'


class LotoGame:
    def __init__(self):
        self._player = LotoCard(input('Введите имя: '))
        self._computer = LotoCard('R2D2')
        self._bag = [x for x in range(1, 91)]

    def run(self, check=False):
        while True:
            if len(self._bag) < 1:
                print(f'Бочонки в мешке закончились. Результат:\n'
                      f'у игрока осталось {self._player.MAX_NUMBER_IN_CARD} числа/чисел,'
                      f'у компьютера осталось {self._computer.MAX_NUMBER_IN_CARD} числа/чисел\n')
                break
            barrel = self._bag.pop(randint(0, len(self._bag) - 1))
            print(f'\nНовый бочонок: {barrel} (осталось {len(self._bag)})')
            print(self._player)
            print(self._computer)
            reply = input('Зачеркнуть цифру? (y/n, q - выход)\n').lower()
            while len(reply) == 0 or reply not in 'ynq':
                print('\n\nОтвет не распознан!\n')
                print(f'Бочонок: {barrel} (осталось {len(self._bag)})')
                reply = input('Зачеркнуть цифру? (y/n, q - выход)\n').lower()

            if reply == 'q':
                print('Вы вышли из игры.')
                break
            elif reply == 'y':
                for x in range(3):
                    if barrel in self._player.card[x]:
                        check = True
                        self._player.card[x][self._player.card[x].index(barrel)] = 'x'
                        self._player.MAX_NUMBER_IN_CARD -= 1
                    if barrel in self._computer.card[x]:
                        self._computer.card[x][self._computer.card[x].index(barrel)] = 'x'
                        self._computer.MAX_NUMBER_IN_CARD -= 1
                if check:
                    if self._player.MAX_NUMBER_IN_CARD < 1:
                        print('Вы выиграли!')
                        break
                    elif self._computer.MAX_NUMBER_IN_CARD < 1:
                        print('Компьютер выиграл!')
                        break
                else:
                    print('Вы проиграли! Такого числа нет на Вашей карточке!')
                    break
            elif reply == 'n':
                for x in range(3):
                    if barrel in self._player.card[x]:
                        print('Вы проиграли! Такое число есть на Вашей карточке!')
                        check = True
                        break
                    if barrel in self._computer.card[x]:
                        self._computer.card[x][self._computer.card[x].index(barrel)] = 'x'
                        self._computer.MAX_NUMBER_IN_CARD -= 1
                if check:
                    break
                if self._player.MAX_NUMBER_IN_CARD < 1:
                    print('Вы выиграли!')
                    break
                elif self._computer.MAX_NUMBER_IN_CARD < 1:
                    print('Компьютер выиграл!')
                    break


if __name__ == '__main__':
    game = LotoGame()
    game.run()
