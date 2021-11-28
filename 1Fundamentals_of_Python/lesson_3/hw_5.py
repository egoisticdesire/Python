from random import choice


def get_jokes(n, arr_1, arr_2, arr_3):
    """
    Эта функция берет по 1 случайному элементу из каждого списка и сшивает их.
    :param n: кол-во шуток
    :param arr_1: список_1
    :param arr_2: список_2
    :param arr_3: список_3
    """
    jokes = []
    for i in range(n):
        random_idx_1 = choice(arr_1)
        random_idx_2 = choice(arr_2)
        random_idx_3 = choice(arr_3)
        jokes.append(f'{random_idx_1} {random_idx_2} {random_idx_3}')
    return jokes


nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

print(get_jokes(5, nouns, adverbs, adjectives))
