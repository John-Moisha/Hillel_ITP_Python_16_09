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
# my_list_6_1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# my_list_6_2 = [3, 4, 5, 6, 7, 8]
# my_result6 = []
#
# if len(my_list_6_2) < len(my_list_6_1):
#     my_list_6_1, my_list_6_2 = my_list_6_2, my_list_6_1
#
# list_len6 = len(my_list_6_1)
# for index in range(list_len6):
#     my_result6.append(my_list_6_1[index])
#     my_result6.append(my_list_6_2[index])
#     # my_result6.extend([my_list_6_1[index], my_list_6_2[index]])
# my_result6.append("")
# my_result6.extend(my_list_6_2[list_len6:])
# print(my_result6)
#
# """
# 7)
# Даны списки my_list_1 и my_list_2.
# Создать список my_result в который вначале поместить четные элементы из my_list_1,
# а потом все нечетные элементы из my_list_2.
# """
# my_list_7_1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# my_list_7_2 = [3, 4, 5, 6, 7, 8]
# my_result7 = my_list_7_1[::2] + my_list_7_2[1::2]
# print(my_result7)
# """
# 8)
# Дано целое число. Определить сколько цифр в этом числе.
# """
# number = 746527310
# print(len(str(number)))
#
# """
# 9)
# Дано целое число. Определить наибольшую цифру в этом числе.
# """
# number = 746527310
# print(max(str(number)))
# print(min(str(number)))
#
#
# """
# 10)
# Дано целое число. Составить число с цифрами в обратном порядке.
# """
# number10 = 746527310
# print(int(str(number10)[::-1]))
#
#
# """
# 11)
# Дано целое число. Составить число с цифрами в порядке возрастания.
# """
# number11 = 746527310
# numb_list11 = list(str(number11))
# numb_list11.sort(reverse=False)
# str_numb11 = ''.join(numb_list11)
# new_numb11 = int(str_numb11)
# print(new_numb11)
# #
# #
# # # сортировка списка
# my_list11 = [3, 5, -6]
# # my_list11.sort()
# # print(my_list11)
# #
# #
# # # сортировка копии списка
# new_list11 = sorted(my_list11)
# print(my_list11)
# print(new_list11)

#
# # ключ сортировки, порядок списка
#
# """
# Цикл с условием( while)
# Игра с угадыванием числа.
# ""
# mind_number12 = 34
# number12 = int(input('угадай число:'))
# while number12 != mind_number12:
#     try:
#         if number12 < mind_number12:
#             number12 = int(input("Bolshe"))
#         else:
#             number12 = int(input('Menshe'))
#     except:
#         number12 = int(input('celoe chislo'))
# print('Molodec Ugadal')

mind_number12 = 34
# number12 = int(input('угадай число:'))
# solved = False
# while not solved:
#     try:
#         number12 = int(input('Vvedi chislo'))
#         if number12 < mind_number12:
#             number12 = print("Bolshe")
#         elif number > mind_number12:
#             number12 = print('Menshe')
#         else:
#             solved = true
#     except:
#         pass
# print('Molodec Ugadal')