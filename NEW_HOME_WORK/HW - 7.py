import random
# 1) Создать список из 20 случайных целых чисел в диапазоне от 1 до 100.
# Задание можно выполнить и через обычный цикл и через генератор списков.

my_list1 = [random.randint(1, 100) for _ in range(20)]
print("Задание 1:", my_list1)


# 2) Создать словарь triangle в который записать точки A B C (ключи),
# и их координаты - кортежи (значения), созданные случайным образом с помощью модуля random.
def randomXY():
    return random.sample(range(-50, 50), 2)

triangle2 = {key: randomXY() for key in ('A', 'B', 'C')}
print("Задание 2v1:", triangle2)
# v2
triangle2v2 = {"A": randomXY(),
             "B": randomXY(),
             "C": randomXY()}
print("Задание 2v2:", triangle2v2)


# 3) Создать функцию my_print, которая принимает строку и печатает ее
# с тремя символами * вначале и в конце строки.
# Пример:
# my_str = 'I'm the string'
# Печатает ***I'm the string***

def my_print3():
    my_str3 = "I'm the string"
    print("Задание 3v1:", '***' + my_str3 +'***')
my_print3()

###V2
my_str3 = "I'm the string"
def my_print3():
    print("Задание 3v2:", '***' + my_str3 +'***')
my_print3()
###V3
my_str_3 = "I'm the string"
oops = my_str_3
def my_print3(my_str_3):
    print("Задание 3v3:", '***' + my_str_3 +'***')
my_print3(oops)


# 4) Даны два словаря my_dict_1 и my_dict_2.
my_dict4_1 = {"key_1":"a",
              "key_2":"b",
              "key_3":"c",
              "key_4":"d",
              "key_5":"e"}
my_dict4_2 = {"key_1":"a",
              "key_2":"b",
              "key_7":"e",
              "key_6":"c",
              "key_5":"d"}

# а) Создать список из ключей, которые есть в обоих словарях.
print("Задание 4 А:", set(my_dict4_1.keys()).intersection(my_dict4_2.keys()))

# б) Создать список из ключей, которые есть в первом, но нет во втором словаре.
print("Задание 4 Б:", set(my_dict4_1.keys()).difference(my_dict4_2.keys()))

# в) Создать новый словарь из пар {ключ:значение}, для ключей, которые есть в первом, но нет во втором словаре.
print("Задание 4 Вv1:", {f"{key}": my_dict4_1[key] for key in my_dict4_1 if key not in my_dict4_2})
# Можно так V2
def my_dict4_V2(dict_1, dict2):
    return {key: value for (key, value) in dict_1.items() if key not in dict2}
print("Задание 4 Вv2:", my_dict4_V2(my_dict4_1,my_dict4_2))

# г) Объединить эти два словаря в новый словарь по правилу:
# если ключ есть только в одном из двух словарей - поместить пару ключ:значение,
# если ключ есть в двух словарях - поместить пару {ключ: [значение_из_первого_словаря, значение_из_второго_словаря]},
def my_dict4_Gv1(dict1, dict2):
    dictg = {}
    for key in (dict1 | dict2):
        if key in dict1.keys() & dict2.keys(): # или  if key in set(dict1.keys()).intersection(dict2.keys())
            dictg.update({key: [dict1.get(key), dict2.get(key)]})
        else:
            dictg.update({key: dict1.get(key) or dict2.get(key)})
    return dictg

def my_dict4_Gv2(dict1, dict2):
    #V2
    return {key: [dict1.get(key), dict2.get(key)] if key in dict1.keys() & dict2.keys() else
                        dict1.get(key) or dict2.get(key) for key in dict1.keys() | dict2.keys()}

print("Задание 4 Гv1:", my_dict4_Gv1(my_dict4_1, my_dict4_2))
print("Задание 4 Гv2:", my_dict4_Gv2(my_dict4_1, my_dict4_2))