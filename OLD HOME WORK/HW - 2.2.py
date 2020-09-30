# value = input('Введите целое число:')
# value = int(value)
#
# if value % 5 == 0:
#     print(value * 2)
# elif not value % 5 == 0:
#     print(0)
# else:
#     print('Oops')


# 02 февраль  — 28
#
# 01 январь — 31
# 03 март  — 31
# 05 май — 31
# 07 июль — 31
# 08 август — 31
# 10 октябрь — 31
# 12 декабрь — 31
#
# 04 апрель — 30
# 06 июнь — 30
# 09 сентябрь — 30
# 11 ноябрь — 30
# value = input('Введите месяц: \n (пример - 04 / Апрель):')
# name_m = str(value)
# numb_m = int(value)

# mon30 = (int(4) and not 6) or 9 or 11
#
# mon31 = (int(1) or int(3) or int(5) or int(7) or int(8) or int(10) or int(12))

# april = "Апрель" or "апрель"
# value = input("В каком месяце вас интересует количество дней?:")
# # if not value == str(value) or value == int(value):
# #     print("Не правильно написали месяц!")
# if int(value) == 4 or int(value) == 6 or int(value) == 9 or int(value) == 11:
#     print('В этом месяце 30 дней')
# elif int(value) == 1 or int(value) == 3 or int(value) == 5 or int(value) == 7 or int(value) == 8 or int(value) == 10 or int(value) == 12:
#     print('В этом месяце 31 дней')
# elif int(value) == 2:
#     print('В этом месяце 28 дней')
# elif int(value) > 12:
#     print('В году только 12ь месяцев')
# elif int(value) <= 0:
#     print("Разве такое возможно?")
# elif value == april:
#     print("april")
#
# else:
#     print('0ops')


mon30_int = [4, 6, 9, 11]
mon31_int = [1, 3, 5, 7, 8, 10, 12]
mon28_int = [2]
mon30_str = ['Апрель','апрель','Июнь','июнь','Сентябрь','сентябрь','Ноябрь','ноябрь']
mon31_str = ['Январь','январь','Март','март','Май','май','Июль','июль','Август','август','Окьябрь','октябрь','Декабрь','декабрь']
mon28_str = ['Февраль','февраль']

value = input("В каком месяце вас интересует количество дней?:")
# value_int =
# value_str = str(value)
# april = str("апрель")
if 0 <= float(value) > 0:
    print("takogo ne mojet bit")
# if value = str("april"):
#     print('В этом месяце 30 дней')
elif int(value) == 4 or int(value) == 6 or int(value) == 9 or int(value) == 11:
    print('В этом месяце 30 дней')
elif int(value) == 1 or int(value) == 3 or int(value) == 5 or int(value) == 7 or int(value) == 8 or int(value) == 10 or int(value) == 12:
    print('В этом месяце 31 дней')
elif int(value) == 2:
    print('В этом месяце 28 дней')
elif int(value) > 12:
    print('В году только 12ь месяцев')
elif int(value) <= 0:
    print("Разве такое возможно?")
else:
    print("Oops")

    ### elif not type(value) == str or not type(value) == int:
    ### print("попробуйте вести правильное значени, )"

    # value = input("Введи десятичную дробь:")
    # result = float(value) * 5
    # # result = str(result)
    # result_str = str(result)
    # print("Result:", result, type(result))
    # print("Result_str:", result_str, type(result))

    #
    # try:
    #     val = int(num)
    #     print("Input is an integer number.")
    #     print("Input number is: ", val)
    #     break;
    # except ValueError:
    #     try:
    #         float(num)
    #         print("Input is an float number.")
    #         print("Input number is: ", val)
    #         break;
    #     except ValueError:
    #         print("This is not a number. Please enter a valid number")



# if str(value) == апрель or str(value) == июнь or str(value) == сентябрь or str(value) == ноябрь:
#     print('В этом месяце 30 дней')
# elif str(value) == январь or str(value) == март or str(value) == май or str(value) == июль or str(value) == август or str(
#         value) == октябрь or str(value) == декабрь:
#     print('В этом месяце 31 дней')
# elif str(value) == февраль:
#     print('В этом месяце 28 дней')




#    res = 0
# elif float(value) <= 1:
#     res = 1
# elif float(value) > 1:
#     res = float(value) ** 2
# else:
#     print("Если ты видешь это сообщение, ты ошибся!")
#
# print("Result:", res)
