# import yaml
# import os
#
#
# def dir_create(main_dir, *secondary_dirs):
#     if not os.path.exists(main_dir):
#         os.mkdir(main_dir)
#     os.chdir(main_dir)
#
#     for secondary_dir in secondary_dirs:
#         if not os.path.exists(secondary_dir):
#             os.mkdir(secondary_dir)
#
#
# with open('config.yaml') as file:
#     # The FullLoader parameter handles the conversion from YAML
#     # scalar values to Python the dictionary format
#     config_list = yaml.full_load(file)
#
#     dir_create(config_list)