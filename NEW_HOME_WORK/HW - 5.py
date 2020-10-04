# 1. Дано целое число (int). Определить сколько нулей в этом числе.
number1 = 12312312300340034
print(str(number1).count('0'))

# 2. Дано целое число (int). Определить сколько нулей в конце этого числа.
number2 = 1243534500004500000
number2_str = str(number2)[::-1]
count2 = ''
for symbol in number2_str:
    if symbol == '0':
            count2 += symbol
    else:
        break
print(len(count2))

# 3. даны списки my_list_1 и my_list_2. создать список my_result в который
# вначале поместить четные элементы (именно элементы) из my_list_1 и потом нечетные элементы из my_list_2.
# my_list_1 = [1,2,3,4,5], my_list_2 = [10, 15, 20, 25] -> my_result [2, 4, 15, 25]
my_list3_1 = [1, 2, 3, 4, 5, 6]
my_list3_2 = [10, 20, 30, 40, 50, 60, 70, 80]
my_result3 = []
for symbol in my_list3_1[1::2]:
    my_result3.append(symbol)
for symbol in my_list3_2[1::2]:
    my_result3.append(symbol)
print(my_result3)


# 4. дан список my_list. создать список new_list у которого первый элемент из my_list
# стоит на последнем месте. если my_list [1,2,3,4], то new_list [2,3,4,1]
my_list4 = [1, 2, 3, 4]
new_list4 = []
# ####### вариант 1
# # new_list4 = my_list4[1::]
# ####### вариант 2
for i in my_list4[1::]:
    new_list4.append(i)
new_list4.append(my_list4[0])
print(new_list4)

# 5.дан список my_list. в этом списке первый элемент переставить на последнее место.
# [1,2,3,4] -> [2,3,4,1]. пересоздавать список нельзя! (используйте метод pop)
my_list5 = [1, 2, 3, 4]
my_list5.append(my_list5.pop(0))
print(my_list5)



# 6. дана строка в которой есть числа (разделяются пробелами).
# например "43 больше чем 34 но меньше чем 56". найти сумму всех чисел (а не цифр) в этой строке.
# для данного примера ответ - 133.
str6 = '43 больше чем 34 но меньше чем 56'
clear_str6 = ''
result6 = 0
for symbol in str6:
    if not symbol.isalpha():
        clear_str6 += symbol
sum_clear6 = clear_str6.split(' ')
sum6 = []
for index in range(len(sum_clear6)):
    if sum_clear6[index].isdigit():
        sum6.append(int(sum_clear6[index]))
for i6 in sum6:
    result6 += int(i6)
print(result6)



#
# 7. дана строка my_str. разделите эту строку на пары из двух символов и поместите эти пары в список.
# если строка содержит нечетное количество символов, пропущенный второй символ последней пары должен
# быть заменен подчеркиванием ('_'). примеры: 'abcd' -> ['ab', 'cd'], 'abcde' -> ['ab', 'cd', e_']
from typing import List

my_str7 = 'abcd3'
result7 = []
if len(my_str7) % 2 != 0:
    my_str7 += '_'
for index in range(0, len(my_str7), 2):
    result7.append(my_str7[index:index+2])
print(result7)

#
# 8. дана строка my_str в которой символы не повторяются и два символа l_limit, r_limit,
# которые точно находятся в этой строке. причем l_limit левее чем r_limit.
# в переменную sub_str поместить часть строки между этими символами.
# my_str = "my_long str", l_limit = "o", r_limit = "t" -> sub_str = "ng s"
my_str8 = "my_long str"
l_limit8 = 'o'
l_limit8_str = my_str8.index(l_limit8)
r_limit8 = 't'
r_limit8_str = my_str8.index(r_limit8)
result8 = my_str8[l_limit8_str+1:r_limit8_str]
print(result8)



#
# 9. дана строка my_str в которой символы могут повторяться и два символа l_limit, r_limit,
# которые точно находятся в этой строке. причем l_limit левее чем r_limit.
# в переменную sub_str поместить наибольшую часть строки между этими символами.
# my_str = "My long string", l_limit = "o", r_limit = "g" -> sub_str = "ng strin".
my_str9 = "My long string"
l_limit9 = "o"
l_limit9_str = my_str9.index(l_limit9)
r_limit9 = "g"
r_limit9_str = my_str9.rindex(r_limit9)
sub_str9 = my_str9[l_limit9_str+1:r_limit9_str]
print(sub_str9)



#
# 10. Дан список чисел. Определите, сколько в этом списке элементов,
# которые больше двух своих соседей (слева и справа), и НАПЕЧАТАЙТЕ КОЛИЧЕСТВО таких элементов.
# Крайние элементы списка никогда не учитываются, поскольку у них недостаточно соседей.
# Для списка [2,4,1,5,3,9,0,7] ответом будет 3 потому что 4 > 2+1, 5 > 1+3, 9>3+0
my_list10 = [2, 4, 1, 5, 3, 9, 35, 7]
my_result10 = []
for index in range(len(my_list10)):
    if index != 0 and index != len(my_list10)-1 and my_list10[index] > (my_list10[index-1] + my_list10[index+1]):
        my_result10.append(my_list10[index])

print(my_result10)

