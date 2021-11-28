import random


def game_revers():
    min_num = 1
    max_num = 100
    user = None
    while user != '=':
        number = random.randint(min_num, max_num)
        print('Комп думает, что это число', number)
        user = input('Подсказка: ')
        if user == '>':
            min_num = number + 1
        elif user == '<':
            max_num = number - 1
    else:
        print('Win')

if __name__ == '__main__':
    game_revers()