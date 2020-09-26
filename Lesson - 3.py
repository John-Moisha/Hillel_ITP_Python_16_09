# x = int (input("Введи целое число"))

# if x > 0:
#     y = 3
# else:
#     y = -1
#
# print (y)

# y = 3 if x > 0 else -1
#
# print(y)

# result = 7 if x % 7 == 0 else 0
# result = 7 if not x % 7 else 0
# print(result)

# my_value = 12345.6789
# my_str = f"my_value = {my_value:.2f}"
# print(len(my_str), my_str)

# my_value = 123.45678
#
# my_str = f"my_value = {my_value}"
# print(len(my_str), my_str[2:6])
#
# new_str = my_str[4:6]
# new_str = new_str[::-1]
# print(new_str)
# print(my_str[::-2])

# print(my_str[100:120])
# print(my_str[100])

# index = 10
# my_str = my_str[:index] + "_" + my_str[index + 1:]
# print(my_str.upper())
#
# value = "02"
# if value.isdigit():
#     print(int(value),'eto cifri')
# if value.isalpha():
#     print("eto bukvi")
# if value.isalnum():
#     print("eto cifri i bukvi")

test_str = "qweRty_Uiop"
# if "i" in test_str:
#     print("takaya podstroka est")

# for symbol in test_str:
#     if symbol not in 'eyuioa':
#         print(symbol * 10)

for symbol in test_str:
    if not symbol.isupper():
        print(symbol * 10)