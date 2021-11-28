import os


def dir_create(main_dir, *secondary_dirs):
    if not os.path.exists(main_dir):
        os.mkdir(main_dir)
    os.chdir(main_dir)

    for secondary_dir in secondary_dirs:
        if not os.path.exists(secondary_dir):
            os.mkdir(secondary_dir)


dir_create('my_project', 'settings', 'mainapp', 'adminapp', 'authapp')
