# # # # 1
# import random
#
# user = None
# number = random.randint(1, 100)
#
# while user != '=':
#     count = random.randint(1, 3)
#     print('Комп думает, что это число', number)
#     user = input('Подсказка: ')
#     if user == '<':
#         number = number - count
#         if number < 1:
#             number = 1
#     elif user == '>':
#         number = number + count
#         if number > 100:
#             number = 100
# else:
#     print('Win')
#

# # # 2
import random

if __name__ == '__main__':
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