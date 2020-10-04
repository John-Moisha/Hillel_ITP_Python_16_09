# 1. Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list по следующему правилу:
# Если строка стоит на нечетном месте в my_list, то ее заменить на
# перевернутую строку. "qwe" на "ewq".
# Если на четном - оставить без изменения.
# Задание сделать с использованием enumerate.
#
# my_list1 = ['qwe', 'rty', 'uio', 'asd', 'fgh', 'jkl']
# for index, value in enumerate(my_list1):
#     if index % 2 != 0:
#         my_list1[index] = value[::-1]
#     else:
#         pass
# print(my_list1)

# 2. Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list у которых первый символ - буква "a".
# my_list2 = ['qwe', 'arty', 'uio', 'asd', 'fgh', 'akl']
# my_result_list2 =[]
# for value in my_list2:
#     for s in value:
#         if s[0] == 'a':
#             my_result_list2.append(value)
# print(my_result_list2)


# 
# 3. Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list в которых есть символ - буква "a" на любом месте.
# my_list3 = ['qwe', 'arty', 'uiao', 'asd', 'fgh', 'akl']
# my_result_list3 =[]
# for value in my_list3:
#     for s in value:
#         if s == 'a':
#             my_result_list3.append(value)
# print(my_result_list3)



# 4. Дан список my_list в котором могум быть как строки так и целые числа.
# Создать новый список в который поместить только строки из my_list.
# my_list4 = ['list', 'int', 23, '54', 98, 101, '0']
# my_result4 = []
# for value in my_list4:
#     if type(value) == str:
#         my_result4.append(value)
#     else:
#         pass
# print(my_result4)


# 
# 5. Дана строка my_str. Создать список в который поместить те символы из my_str,
# которые встречаются в строке только один раз.
# my_str5 = 'privet medved, kak tvoi dela? hochu skazat, chto moi dela otlichni'
# result5 = []
# for s in set(my_str5):
#     result5.append(s)
# print(result5)


# 6. Даны две строки. Создать список в который поместить те символы,
# которые есть в обеих строках хотя бы раз.
# str6_1 = 'kdjfhkjghkdjfhgkjdfhgkhdfk'
# str6_2 = 'skdfhgskjkjsfkshdfkjhsdkfh'
# result6 = []
# for s in set(str6_2).intersection(set(str6_1)):
#     result6.append(s)
# print(result6)



# 7. Даны две строки. Создать список в который поместить те символы, которые есть в обеих строках,
# но в каждой только по одному разу.

str7_1 = 'aaaassseeeedffh'
str7_2 = 'skdfhgskjkjsfkyshdfkjhsdkfh'
uni_str7_1 = [s for s in str7_1 if str7_1.count(s) == 1]
uni_str7_2 = [s for s in str7_2 if str7_2.count(s) == 1]
print(uni_str7_1)
print(uni_str7_2)
result7 = []
result 7

for s in set(uni_str7_2).intersection(set(uni_str7_1)):
    result7.append(s)
print(result7)
result7_1 = []

# # print(str7_1.count('0'))
# for s in str7_2:
#     if str7_1.count(s) == 1:
#         result7_1.append(s)
# print(result7_1)
# print(uni_str7_1)
# print(result7)
# print(count.str7_1)

# print(result7)
# print(set(str7_1))
# print(set(str7_2))



# 8. Описать с помощью словаря следующую структуру для конкретного человека (можно придумать):
# Фамилия
# Имя
# Возраст
# Проживание
#     Страна
#     Город
#     Улица
# Работа
#     Наличие
#     Должность
# 
# 9. Описать с помощью словаря следующую структуру (рецепт ненастоящего торта,
# придумать и указать граммы для продуктов):
# Составляющие
#     Коржи
#         Мука
#         Молоко
#         Масло
#         Яйцо
#     Крем
#         Сахар
#         Масло
#         Ваниль
#         Сметана
#     Глазурь
#         Какао
#         Сахар
#         Масло