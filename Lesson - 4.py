# # value = input('введи число:')
# # try:
# #     value = float(value)
# # except:
# #     print('не коректный ввод')
# #     value = 0.0
# #
# # print(value)
# # # if value != 0.0:
# # #     result = 1 / value
# # # else:
# # #     result = "Oops!!!"
# # try:
# #     result = 1 / value
# # except:
# #     print("на 0 делить нельзя")
# #     result = None
# # print(result)
#
# # try:
# #     value = float(value)
# #     result = 1 / value
# # except ValueError:
# #     print('Не коректный ввод!')
# #     result = None
# # except ZeroDivisionError:
# #     print('На 0 делить нельзя')
# #     result = 0.0
#
# # try:
# #     value = float(value)
# #     result = 1 / value
# # except (ValueError,ZeroDivisionError):
# #     print('Что-то не так')
# #     result = None
# #
# # print(result)
#
# # структура данных
# # Кортеж - tuple
# # tuple_1 = (1, 3, "5", 8, "abc")
# # tuple_2 = (4, 8)
# # # tuple_3 = (tuple_1, tuple_2)
# #
# # # print(tuple_1, type(tuple_1), len(tuple_1))
# # # print(tuple_2 [0]) #!!!
# # # print(tuple_3)
# # #
# # # for value in tuple_1 [2:-1]:
# # #     print(value)
# #
# # a = 5
# # b = 7
# # a, b = b, a
# # print(a, b)
# #
# # # распаковка кортежей
# # # a, b, c = tuple_2
# # val_1, *sdfsdfsdf = tuple_1
# # print(sdfsdfsdf)
#
# # List - Список
# print('---------------')
# list_1 = [1, 3, "5", 8, "abc"]
# list_2 = [4, 8]
# # list_3 = [list_1, list_2]
# # list_2[1] = 100
# # print(list_1, type(list_1), len(list_1))
# # print(list_2 [1])
# # print(list_3)
#
# tmp_value_none = list_1.append(list_2)
# print(tmp_value_none)
# list_1.append("list_2")
# list_1.append(len)
# tmp_value = list_1.pop()
# print("temp_value:", tmp_value)
# list_1.pop()
# print(list_1)
#
# print(tmp_value(list_2))
#
# list_1.extend(list_2)
# list_1.pop(-3)
# print(list_1)
#
# my_str_list = []
#
# for value in list_1:
#     value = str(value)
#     my_str_list.append(value)
#     # my_str_list.append(str(value))
#
# print(my_str_list)
#
# result_str = "_,_".join(my_str_list)
# print(result_str)
# print('abc' in my_str_list)
#
# value = input()
#
# if value in ["01", "03", "05" ,"07" ,"08" ,"10" ,"12", "yanvar"]:
#     print("31")
# elif value in ["04", "06", "11"]:
#     print("30")


my_indexes = [10, 25, 50, 145, 70]
my_string = [0, 1, 2, 4, 3]
for index in my_string:
	print(my_indexes[index])
