
# Задание № 1
# data.json - файл с данными о некоторых математиках прошлого.
# 1. Необходимо написать функцию, которая считает эти данные из файла. Параметр функции - имя файла.
# 2. Написать функцию сортировки данных по ФАМИЛИИ в поле "name" (у тех у кого она есть).
# Например для Rene Descartes фамилия это Descartes, у Pierre de Fermat - Fermat и т.д.
# Если фамилии нет, то использовать имя, например Euclid.
# 3. Написать функцию сортировки по дате смерти из поля "years".
# Обратите внимание на сокращение BC. - это означает до н.э.
# 4. Написать функцию сортировки по количеству слов в поле "text"
# url_json = "https://github.com/VolodymyrZontov/Hillel_ITP_Python_16_09/blob/master/Homeworks/data.json"
import json
import re

json_file = "data.json"

############# 1
def open_file(filename_with_path):
    with open(filename_with_path, encoding='utf-8') as json_file:
        return json.load(json_file)

task_1 = open_file(json_file)
print("1. Открыли ===>", task_1)

############## 2

def key_name(dict_):
    return dict_["name"].split(" ")[-1]

task_2 = sorted(task_1, key=key_name)
print("2. по Имени ==>", task_2)

############### 3
# не могу полность разобратся с регуляркой(можно ли как то отсеить все, и получить только последние цифры?
#                                           (понятно что можно, но так и не понял еще как, может позже получится))
###############
def key_years(dict_):
    k_years = dict_['years']
    re_ = r'[0-9]{3,4}'
    re_k_years = re.findall(re_, k_years)
    if 'bc' in k_years.lower():
        return int(re_k_years[-1]) * -1
    return int(re_k_years[-1])

task_3 = sorted(task_1, key=key_years)
print("3. по Дате ===>", task_3)

################ 4

def key_len_text(dict_):
    return len(dict_["text"])
task_4 = sorted(task_1, key=key_len_text)
print("4. по Длине ==>", task_4)

