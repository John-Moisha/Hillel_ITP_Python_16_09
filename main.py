my_list = ['123', 'abc', 'next', '890']
new_list = []
for index, value in enumerate(my_list):
    if index % 2 == 0:
        new_list.append(value[::-1])
    else:
        new_list.append(value)
print(new_list)


my_list1_1 = ['qwe', 'rty', 'uio', 'asd', 'fgh', 'jkl']
my_new_list1 = []
for index, value in enumerate(my_list1_1):
    if index % 2 != 0:
        my_new_list1.append(value[::-1])
    else:
        my_new_list1.append(value)
print("Задача 1:", my_new_list1)