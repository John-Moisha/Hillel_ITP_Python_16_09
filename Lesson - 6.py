# my_list1 = [1, 20, 34, 12, -8]
# возыести в кывадрат элементы на четных местах(и остальные оставить без изминения)
########## V1 ###
# for index in range(len(my_list1)):
#     if index % 2 == 0:
#         print(my_list1[index] ** 2)
#     else:
#         print(my_list1[index])
#     # if not index % 2:
######### V2 ####
# for index, value in enumerate(my_list1):
#     if index % 2 == 0:
#         print(value ** 2)
#     else:
#         print(value)
######### V3 #####
# возвести элемент списка в степень его индекса
# for index, value in enumerate(my_list1):
#     print(value ** index)

#####################
# в new_list поместить числовые значения из my_list, учитывая что числа могут быть строкой
# my_list2 = [1, 2, 3, '4', '5', 6, 7, 'qwe', '88']
# new_lit2 = []
# ########### V1 ########
# # for value in my_list2:
# #     try:
# #         value = int(value)
# #         new_lit2.append(value)
# #     except ValueError:
# #         pass
# ########### V2 ########
# for value in my_list2:
#     if type(value) == str:
#         if value.isdigit():
#             value = int(value)
#             new_lit2.append(value)
#     else:
#         new_lit2.append(value)
#
# print (new_lit2)

######## Множество Set #########
# my_list3 = [1, 20, 34, 12, -8, 12, 1, 1, 23]
# my_set3 = set('my_list3_list_list')
# print(my_set3)

# #3) У вас есть переменная my_str, тип - str. Напечатать ЧИСЛО сколько РАЗНЫХ символов встречается в my_str.
# # Большая и маленькая буква считается как один символ. Пробелы, запятые и т.д. считаем тоже как символы.
# # Пример:  my_str="bla BLA car".
# # Вывод на экран:
# # 6
# # """
# my_str3 = "bla BLA carDDD"
# print(len(set(my_str3.lower())))

# my_set2_1 = {1, 2, 3}
# my_set2_2 = {2, 3, 4}

# my_set2_1.add(7)
# #1 и там и там №1 тетрадь возвращает
# inter = my_set2_1.intersection(my_set2_2)
# two_inter = inter
# print(inter, my_set2_1, inter is two_inter)
# #2 и там и там №1 тетрадь возвращает#
# my_set2_1.intersection_update(my_set2_2)
# print(my_set2_1)
# #3
# union = my_set2_1.union(my_set2_2)
# print(union)
# #4
# my_set2_1.update(my_set2_2)
# print(my_set2_1)
# #5
# dif = my_set2_1.difference(my_set2_2)
# print(dif)
# #6
# my_set2_1.difference_update(my_set2_2)
# print(my_set2_1)
# #7
# sym_dif = my_set2_1.symmetric_difference(my_set2_2)
# print(sym_dif)
# #8
# my_set2_1.symmetric_difference_update(my_set2_2)
# print(my_set2_1)

#### !!!!!!!!!!!!!
my_alphabet = ''
index_a = ord ('Z')
# print(ord('a'), chr(98))
print(index_a, chr(index_a -1))

for index in range(ord('a'), ord('z') + 1):
    my_alphabet += chr(index)
print(my_alphabet)
my_random = ','.join(set(my_alphabet))
print(my_random)
my_random = ','.join(set(my_random))
print(my_random)

#Гениратор списков

# my_list8 = [1, 2, -3, 4, -5]
# # my_sqr8 = [value ** 2 for value in my_list8] # new object
# my_sqr8 = [value ** 2 for value in my_list8 if value > 0] # new object
# print(my_sqr8)
# # [print(value ** 2) for value in my_list8]

# # Знакомство со словарями
# childrens = ["Nastya", "Vlada", "Matvey"]
#
# person_zontov = {"name": "Vava",
#           "age": 41,
#           "childrens": childrens,
#           "teacher": True,
#           12: "Key_12"}
#
# math_dict = {0: "Четное число",
#              1: "Не Четное число"}
#
# hillel_tichers = {"zontov": person_zontov,
#                   "Kamiskiy": {}}
#
# # print(math_dict[0])
# # print(math_dict[123%2])
#
# print(hillel_tichers["zontov"]["childrens"])
