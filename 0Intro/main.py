import q2
from random import choice
from q1 import dir_create, dir_delete

your_choice = input('q1 or q2: ')
while True:
    if your_choice == 'q1':
        while True:
            directory = input('new or del or exit: ')
            if directory == 'new':
                # q1.dir_create()
                dir_create()
                break
            elif directory == 'del':
                # q1.dir_delete()
                dir_delete()
                break
            elif directory == 'exit':
                break
        break
    elif your_choice == 'q2':
        # q2.list_create()
        # print(q2.test_list)
        # print('Randomize:')
        # print(q2.choice(q2.test_list))
        # list_create()
        # print(test_list)
        # print('Randomize:')
        # print(choice(test_list))
        print(q2.get_random([1, 2, 3, 4, 5, 6, 7, 8, 9]))

        break
    else:
        print('Stupid!')
        break
