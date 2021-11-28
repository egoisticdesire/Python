# Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный и
# отсортированный массивы. Сортировка должна быть реализована в виде функции.
# По возможности доработайте алгоритм (сделайте его умнее).

from random import randint


def bubble_sort(arr, reverse=False):
    for j in range(len(arr) - 1):
        for i in range(len(arr) - 1 - j):
            if not reverse:
                if arr[i] > arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
            else:
                if arr[i] < arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]

    return arr


my_list = [randint(-100, 99) for _ in range(20)]

print(f'Original list:\n\t{my_list}\n'
      f'Sorted list:\n\t{bubble_sort(my_list)}\n'
      f'Reversed sorted list:\n\t{bubble_sort(my_list, reverse=True)}')
