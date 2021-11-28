import sys, os
# import game_random_number
from core import create_file, create_folder, get_list, delete, copy, save_info, change_directory
from game import game_revers
save_info('Start')
try:
    command = sys.argv[1]
except IndexError:
    print('Необходимо выбрать команду (help)')
else:
    if command == 'list':
        get_list()
    elif command == 'create_file':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Отсутствует название файла')
        else:
            create_file(name)
    elif command == 'create_folder':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Отсутствует название папки')
        else:
            create_folder(name)
    elif command == 'delete':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Нужно указать имя файла или папки для удаления')
        else:
            delete(name)
    elif command == 'ch':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Нужно указать имя файла или папки')
        else:
            change_directory(name)

    elif command == 'copy':
        try:
            try:
                name = sys.argv[2]
                new_name = sys.argv[3]
            except IndexError:
                print('Укажи имя файла/папки и новое имя файла/папки')
            else:
                copy(name, new_name)
        except FileNotFoundError:
            print(f'Файла {name} не существует!')
    elif command == 'help':
        print('help - вызов помощи\n'
              'list - вывод списка файлов и папок\n'
              'create_file - создание файла\n'
              'create_folder - создание папки\n'
              'delete - удаление файла или папки\n'
              'copy - копирование файла или папки\n'
              'ch - смена папки\n'
              'game - запуск игры\n')

    elif command == 'game':
        try:
            game_revers()
        except IndexError:
            print('Укажи команду')
save_info('Finish')
