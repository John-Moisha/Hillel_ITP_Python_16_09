from datetime import datetime
from dateutil.parser import parse
import re
path = "../Files/authors.txt"
# Дан файл authors.txt
# Все пункты сделать как отдельные функции(можно создавать дополнительные вспомагательные функции)
# 1) написать функцию, которая считывает данные из этого файла,
# возвращая список строк в которых есть полная дата и указание на чей-то день рождения или смерти.
# Например 8th February 1828 и слова birthday или death.

def open_file_write_to_list(path:str) -> list:
    file = open(path, "r")
    return [line.replace("\n","") for line in file]

open_fwtl = open_file_write_to_list(path)

def death_bday_with_date_in_list(listline:list) -> list:
    list_with_date = []
    for line in listline:
        if "death" in line or "birthday" in line:
            list_with_date.append(line)
    return list_with_date

death_bwdil = death_bday_with_date_in_list(open_fwtl)
print(type(death_bday_with_date_in_list(open_fwtl)), "1. ===>", death_bwdil)


def from_text_to_digital(date_in_text: str) -> str:
    return str(parse(date_in_text).strftime("%Y/%m/%d"))

def list_to_dicts(line_from_list: list) -> dict:

    # dict_name = {'name': str(line_from_list).split("-")[1].split("'")[0].strip()}
    # dict_date = {'date': from_text_to_digital((str(line_from_list).split("-")[0].strip())[2:])}
    # dict_name_date = {'name' : dict_name['name'], 'date': dict_date['date']}
    #######
    dict_back = {}
    for line in line_from_list:
        key = line.split("-")[1].split("'")[0].strip()
        value = from_text_to_digital((line.split("-")[0].strip()))
        dict_back.update({key: value})


    return dict_back
list_td = list_to_dicts(death_bwdil)
print(type(list_to_dicts(death_bwdil)), '2: ===>', list_to_dicts(death_bwdil))

# 3) Из словарей, полученных в пункте 2, создать список словарей.
# Например [{"name": "Charles Dickens", "date": "09/06/1870"}, ...,
# {"name": "J. D. Salinger", "date": "01/01/1919"}]
def from_dict_to_list_of_dicts(list_dicts: dict)-> list:

    return [{key : list_dicts.get(key)}for key in list_dicts.keys()]

print(type(from_dict_to_list_of_dicts(list_td)),'3. ===>', from_dict_to_list_of_dicts(list_td))


# def list_dicts(list_with_bd_day: list) -> list:

#     return [{"name": line.split("-")[1].split("'")[0].strip(),
#              "date": from_text_to_digital(line.split("-")[0].strip())}
#             for line in list_with_bd_day]
#
# list_d = list_dicts(death_bwdil)
# print(type(list_dicts(death_bwdil)),"2-3. =>", list_dicts(death_bwdil))


# 4) Из словарей, полученных в пункте 2, создать список словарей с днем рождения и смерти (если есть).
# Например [{"name": "Charles Dickens", "b_date": "07/02/1812", "d_date": "09/06/1870"}, ...,
# {"name": "J. D. Salinger", "b_date": "01/01/1919"}]

def name_date_b_or_d(list_with_date: list) -> list:

    day_b = [line for line in list_with_date if " birthday" in line]
    day_d = [line for line in list_with_date if " death" in line]
    dict_b = {line.split("-")[1].split("birthday")[0].strip(): from_text_to_digital(line.split("-")[0].strip())
            for line in day_b}
    dict_d = {line.split("-")[1].split("death")[0].strip(): from_text_to_digital(line.split("-")[0].strip())
            for line in day_d}
    dict_back = [{"Name": key, "B_day": dict_b.get(key), "D_day": dict_d.get(key)} for key in dict_b.keys() | dict_d.keys()]

    return dict_back

print(type(name_date_b_or_d(open_fwtl)), "4. ===>", name_date_b_or_d(death_bwdil))
