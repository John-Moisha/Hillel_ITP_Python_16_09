
# Задание 2.
#
# 1) Написать функцию, которая генерирует строку из 6 символов. Первые 4 символа это цифры или знак нижнего
# подчеркивания _. Последние два символа - буквы. Примеры: 10_2as или _120xx.
# 2) Создать в папке tmp_folder (создать, если не существует) файл json, имя которого сгенерировано с помощью
# функции из пункта 1.
# 3) внутри файла создать структуру:
# {"filename": filename,
# "Width": random int (до 400),
# "objects":[
# "object": {"class": symbol, "xmin": xmin (int), "xmax": xmax (int)},
# "object": {"class": symbol, "xmin": xmin (int), "xmax": xmax (int)},
# ]
# См фото по ссылке.

import json
import string
import random
import os

#1
def gen_names()-> str:
    return (''.join(random.choice(string.digits + '_') for _ in range(4))) +\
           (''.join(random.choice(string.ascii_lowercase) for _ in range(2)))

name_for_card = gen_names()

#3
def gen_list_dict(name_:str, rand_:int):
    out_list = []
    part_w = (rand_ // 4)
    if name_[0] != '_':
        out_list.append({"object": {'class': name_[0], "x_min": 0, "x_max": part_w * 1}})
    if name_[1] != '_':
        out_list.append({"object": {'class': name_[1], "x_min": part_w * 1, "x_max": part_w * 2}})
    if name_[2] != '_':
        out_list.append({"object": {'class': name_[2], "x_min": part_w * 2, "x_max": part_w * 3}})
    if name_[3] != '_':
        out_list.append({"object": {'class': name_[3], "x_min": part_w * 3, "x_max": rand_}})
    return out_list


def gen_data_for_file(name_f = name_for_card):
    rand_width = random.randint(1, 400)
    objects_ = gen_list_dict(name_f, rand_width)
    return {"filename": name_f, "width": rand_width, "objects": objects_}

print(gen_data_for_file())

#2
def creat_folder(name_f = name_for_card):
    if not os.path.isdir('tmp_folder'):
        os.mkdir('tmp_folder')
    path = './tmp_folder/' + name_f + '.json'
    with open(path, 'w') as file:
        json.dump(gen_data_for_file(), file, indent=3)

creat_folder()