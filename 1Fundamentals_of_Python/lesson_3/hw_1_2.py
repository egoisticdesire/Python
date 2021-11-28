def num_translate(key, arr):
    return arr.get(key)


def num_translate_adv(key, arr):
    if key[0].isupper():
        key = key.lower()
        return arr[key].title()
    else:
        return arr[key]


"""
Можно было затолкать словарь в тело функции и удалить аргумент 'arr',
обращаться к функции только по ключу.
Но тогда словарь станет локальным, а функция потеряет свою универсальность.
"""

translates = {'one': 'один',
              'two': 'два',
              'three': 'три',
              'four': 'четыре',
              'five': 'пять',
              'six': 'шесть',
              'seven': 'семь',
              'eight': 'восемь',
              'nine': 'девять',
              'ten': 'десять'}

print(num_translate('five', translates))
print(num_translate_adv('Five', translates))
