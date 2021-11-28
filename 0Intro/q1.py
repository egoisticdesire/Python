import os


def dir_create():
    for i in range(1, 10):
        new_folder = f'dir_{i}'
        os.mkdir(new_folder)


def dir_delete():
    for i in range(1, 10):
        new_folder = f'dir_{i}'
        os.rmdir(new_folder)


# directory = input('new or del or exit: ')
# while True:
#     if directory == 'new':
#         dir_create()
#         break
#     elif directory == 'del':
#         dir_delete()
#         break
#     elif directory == 'exit':
#         break
