from random import choice

test_list = []


# def list_create():
#     for i in range(1, 10):
#         number = input('Введи данные: ')
#         test_list.append(number)


# list_create()
# print(test_list)
# print('Randomize:')
# print(choice(test_list))

def get_random(input_list):
    if input_list:
        result = choice(input_list)
        return result


if __name__ == '__main__':
    print(get_random([1, 2, 3, 4, 5, 6, 7, 8, 9]))
