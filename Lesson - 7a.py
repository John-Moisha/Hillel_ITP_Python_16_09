# import random
from random import randint, choice
# # from random import *
#
# value = randint(1,10)
# print(value)
#
# rand_list = [randint(1,100) for _ in range(value)]
# print(rand_list)
# print(choice(rand_list))
# print(symbol_dict)

# Function

def special_print(min_value, max_value): # область видимости переменной
    print("ЭТО value из тела функции :", value_)
    print("min_value:", min_value, "max_value:", max_value)
    value = randint(min_value, max_value)
    print(f'This is random value is {value}')
    return value * value_

# value_1 = special_print(10,50) #позиционными аргументами (параметры)
# # print(max_value)
# value_2 = special_print(100, 200)
# print(value_1, value_2)
value_ = 10000
value_ = special_print(1, 10)
print(value_)

def generate_random_list(num_list, min_va, max_val):
    return [randint(min_va, max_val) for _ in range(num_list)]

rand_list = generate_random_list()
