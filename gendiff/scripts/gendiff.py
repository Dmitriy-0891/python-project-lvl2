#!:/usr/bin/env python3


import argparse
import json


def main():
    parser = argparse.ArgumentParser(description='Comparestwo configuration files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    print(args)


def generate_diff(file_path1, file_path2):
    dict_1 = json.load(open(f'{file_path1}'))
    dict_2 = json.load(open(f'{file_path2}'))
    main_dict = {}
    list_keys_1 = list(dict_1.keys())
    list_keys_2 = list(dict_2.keys())
    main_list_keys = list_keys_1 + list_keys_2
    main_set_keys = sorted(set(main_list_keys))
    for i in main_set_keys:
        i_1 = f"-{i}"
        i_2 = f"+{i}"
        if i in list_keys_1:
            if i in list_keys_2:
                if dict_1[i] == dict_2[i]:
                    main_dict[i] = dict_1[i]
                else:
                    main_dict[i_1] = dict_1[i]
                    main_dict[i_2] = dict_2[i]
            else:
                main_dict[i_1] = dict_1[i]
        else:
            main_dict[i_2] = dict_2[i]
    return json.dumps(main_dict)


if __name__ == '__main__':
    main()
