import os
import shutil
import datetime


def create_file(name, text=None):
    with open(name, 'w', encoding='utf-8') as f:
        if text:
            f.write(text)


def create_folder(name):
    try:
        os.mkdir(name)
    except FileExistsError:
        print('Папка уже существует')


def get_list(folders_only=False):
    result = os.listdir()
    if folders_only:
        result = [f for f in result if os.path.isdir(f)]
    print(result)


def delete(name):
    if os.path.isdir(name):
        os.rmdir(name)
    else:
        os.remove(name)


def copy(name, new_name):
    if os.path.isdir(name):
        try:
            shutil.copytree(name, new_name)
        except FileExistsError:
            print('Такая папка уже существует')
    else:
        shutil.copy(name, new_name)


def save_info(message):
    current_time = datetime.datetime.now()
    result = f'{current_time} - {message}'
    with open('log.txt', 'a', encoding='utf-8') as f:
        f.write(result + '\n')


def change_directory(name):
    os.chdir(name)
    print(os.getcwd())


if __name__ == '__main__':
    create_file('test.txt', 'some text')
    create_folder('test_f')
    get_list()
    # delete('test_f')
    # delete('test.txt')
    copy('test_f', 'test_f_2')
    copy('test.txt', 'test_2.txt')
    save_info('test')
    # change_directory_back()
