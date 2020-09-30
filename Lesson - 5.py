# # my_str = ''
# #
# # """
# # 1) У вас есть переменная my_str, тип - str. И переменная my_symbol, тип - str.
# # Напечатать столько раз my_symbol, сколько он встречается в my_str.
# # Пример:  my_str="blablacar", my_symbol="bla".
# # Вывод на экран:
# # bla
# # bla
# # """
# my_str1 = "blablacar"
# my_symbol1 = "bla"
# count1 = my_str1.count(my_symbol1)
# #1
# text_symbol1 = my_symbol1 + '\n'
# text1 = text_symbol1 * count1
# text1= text1.strip()
# #2
# text_list1 = [my_symbol1] * count1
# text1 = "\n".join(text_list1)
# #3
# for _ in range(count1):
#     print(my_symbol1)
#
# # print(text_list1)
# # print(text1)
# # print('--------')

#########
# """
# 2) У вас есть переменная my_str, тип - str. И переменная my_symbol, тип - str.
# Напечатать ЧИСЛО сколько раз my_symbol встречается в my_str.
# Пример:  my_str="blablacar", my_symbol="bla".
# Вывод на экран:
# 2
# """
# my_str2 = "blablacar"
# my_symbol2 = "bla"
# count = my_str1.count(my_symbol1)
# print(count)

# """
# 3) У вас есть переменная my_str, тип - str. Напечатать ЧИСЛО сколько РАЗНЫХ символов встречается в my_str.
# Большая и маленькая буква считается как один символ. Пробелы, запятые и т.д. считаем тоже как символы.
# Пример:  my_str="bla BLA car".
# Вывод на экран:
# 6
# """
# my_str3 = "bla BLA car"
# lower_str3 = my_str3.lower()
# unique_str3 = ''
# for symbol in lower_str3:
#     if symbol not in unique_str3:
#         unique_str3 += symbol
# print(len(unique_str3))

#
# """
# 4)
# Дана строка my_str и пустой список my_list.
# Заполнить my_list символами из my_str, которые стоят на четных местах в строке
# """

# my_str4 = "qwerty"
#
# # # решение через приведение типов
# # my_list4 = list(my_str4[::2])
# my_list4.extend(list(my_str4[::2]))
# print(my_list4)
# # # решение через цикл
# my_list4_2 = []
# for symbol in my_str4[::2]:
#     my_list4_2.append(symbol)
# print(my_list4_2)

#
# """
# 5)
# Дана строка my_str, список str_index целых чисел в диапазоне от 0 до длинны строки, пустой список my_list.
# Заполнить my_list символами из my_str, которые стоят на местах с индексами из str_index
# """
my_list = []
my_str = "qwerty"
str_index = [0, 5, 3, 3, 4]
for index in str_index:
    symbol = my_str[index]
    my_list.append(symbol)
    # my_list.append(my_str[index]) однострочный код
print(my_list)
#
#
# """
# 6)
# Даны списки my_list_1 и my_list_2.
# Создать список my_result в который поместить элементы из my_list_1 и my_list_2 через один.
# a) кол-во эл-тов одинаковое
# б) кол-во эл-тов разное
# """
# my_list_1 = [10, 20, 30, 40, 50]
# my_list_2 = [3, 4, 5, 6, 7]
# my_result = []
#
#
# """
# 7)
# Даны списки my_list_1 и my_list_2.
# Создать список my_result в который вначале поместить четные элементы из my_list_1,
# а потом все нечетные элементы из my_list_2.
# """
#
# """
# 8)
# Дано целое число. Определить сколько цифр в этом числе.
# """
# number = 746527310
#
# """
# 9)
# Дано целое число. Определить наибольшую цифру в этом числе.
# """
# number = 746527310
#
#
# """
# 10)
# Дано целое число. Составить число с цифрами в обратном порядке.
# """
# number = 746527310
#
#
# """
# 11)
# Дано целое число. Составить число с цифрами в порядке возрастания.
# """
# number = 746527310
#
#
# # сортировка списка
# my_list = [3, 5, -6]
#
#
# # сортировка копии списка
# new_list = sorted(my_list)
#
# # ключ сортировки, порядок списка
#
# """
# Цикл с условием( while)
# Игра с угадыванием числа.
# """