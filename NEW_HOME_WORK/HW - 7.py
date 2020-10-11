# 1) Создать список из 20 случайных целых чисел в диапазоне от 1 до 100.
# Задание можно выполнить и через обычный цикл и через генератор списков.
import random
my_list1 = [random.randint(1, 100) for _ in range(10)]
print("Задание 1:", my_list1)
# 2) Создать словарь triangle в который записать точки A B C (ключи),
# и их координаты - кортежи (значения), созданные случайным образом с помощью модуля random.
triangle2 = {"A": random.randint(1,100),
            "B": random.randint(1,200),
            "C": random.randint(1,300)}
print("Задание 2:", triangle2)
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

#
# 4) Даны два словаря my_dict_1 и my_dict_2.
# а) Создать список из ключей, которые есть в обоих словарях.
# б) Создать список из ключей, которые есть в первом, но нет во втором словаре.
# в) Создать новый словарь из пар {ключ:значение}, для ключей, которые есть в первом, но нет во втором словаре.
# г) Объединить эти два словаря в новый словарь по правилу:
# если ключ есть только в одном из двух словарей - поместить пару ключ:значение,
# если ключ есть в двух словарях - поместить пару {ключ: [значение_из_первого_словаря, значение_из_второго_словаря]},

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
my_list4_a = print("Задание 4 А:", set(my_dict4_1.keys()).intersection((my_dict4_2.keys())))
my_list4_b = print("Задание 4 Б:", set(my_dict4_1.keys()).difference(my_dict4_2.keys()))
# tmp_dict = dict(key_10="qwe", key_0=1000)
# print(tmp_dict)
my_dict4_v = {}
for keys in set(my_dict4_1.keys()).difference(my_dict4_2.keys()):
    my_dict4_v[key] = [my_dict4_1[key], my_dict4_2[key]]

# print(my_dict4_1[key])
print(my_dict4_v)
    # for key2 in my_dict4_2.keys():
    # if set(key).difference(my_dict4_2.keys()):
    #     print(key)
# my_list4_v = my_dict4_1.item()
# my_list4_g =