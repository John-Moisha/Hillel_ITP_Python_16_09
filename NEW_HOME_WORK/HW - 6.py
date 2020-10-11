# 1. Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list по следующему правилу:
# Если строка стоит на нечетном месте в my_list, то ее заменить на
# перевернутую строку. "qwe" на "ewq".
# Если на четном - оставить без изменения.
# Задание сделать с использованием enumerate.
#

my_list1_1 = ['qwe', 'rty', 'uio', 'asd', 'fgh', 'jkl']
my_new_list1 = []
for index, value in enumerate(my_list1_1):
    if index % 2 != 0:
        my_new_list1.append(value[::-1])
    else:
        my_new_list1.append(value)
print("Задача 1:", my_new_list1)

# my_list1_2 = ['qwe', 'rty', 'uio', 'asd', 'fgh', 'jkl']
# for index, value in enumerate(my_list1_2):
#     if index % 2 != 0:
#         my_list1_2[index] = value[::-1]
#     else:
#         pass
# print("Задача 1 v2:", my_list1_2)

# 2. Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list у которых первый символ - буква "a".
my_list2 = ['qwe', 'arty', 'uio', 'asd', 'fgh', 'akl']
my_result_list2 =[]
for value in my_list2:
    for s in value:
        if s[0] == 'a':
            my_result_list2.append(value)
print("Задача 2:", my_result_list2)

#сразу не догадался можно чуть проще
# my_list2 = ['qwe', 'arty', 'uio', 'asd', 'fgh', 'akl']
# my_result_list2 =[]
# for value in my_list2:
#     if value[0] == 'a':
#        my_result_list2.append(value)
# print("Задача 2 v2:", my_result_list2)
#
# или можно вообще просто
# my_list2 = ['qwe', 'arty', 'uio', 'asd', 'fgh', 'akl']
# my_result_list2 = [value for value in my_list2 if value[0] == 'a']
# print("Задача 2 v3,", my_result_list2)

# 3. Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list в которых есть символ - буква "a" на любом месте.
my_list3 = ['qwe', 'arty', 'uiao', 'asd', 'fgh', 'akl']
my_result_list3 =[]
for value in my_list3:
    for s in value:
        if s == 'a':
            my_result_list3.append(value)
print("Задача 3:", my_result_list3)

# v2
# my_list3 = ['qwe', 'arty', 'uiao', 'asd', 'fgh', 'akl']
# my_result_list3 =[value for value in my_list3 if 'a' in value]
# print("Задача 3 v2", my_result_list3)

#сразу не догадался можно чуть проще
# my_list3 = ['qwe', 'arty', 'uiao', 'asd', 'fgh', 'akl']
# my_result_list3 =[]
# for value in my_list3:
#     if 'a' in value:
#         my_result_list3.append(value)
# print("Задача 3 v3:", my_result_list3)


# 4. Дан список my_list в котором могум быть как строки так и целые числа.
# Создать новый список в который поместить только строки из my_list.
my_list4 = ['list', 'int', 23, '54', 98, 101, '0']
my_result4 = []
for value in my_list4:
    if type(value) == str:
        my_result4.append(value)
    else:
        pass
print("Задача 4:", my_result4)

# #4v2
# my_list4 = ['list', 'int', 23, '54', 98, 101, '0']
# my_result4 = [_ for _ in my_list4 if type(_) == str]
# print("Задача 4v2:", my_result4)

# 
# 5. Дана строка my_str. Создать список в который поместить те символы из my_str,
# которые встречаются в строке только один раз.
my_str5 = 'privet medved, kak tvoi dela? hochu skazat, chto moi dela otlichni'
result5 = []
for s in my_str5:
    if my_str5.count(s) == 1:
        result5.append(s)
print("Задача 5:", result5)
# 5v2
# my_str5 = 'privet medved, kak tvoi dela? hochu skazat, chto moi dela otlichni'
# result5_2 = [s for s in my_str5 if my_str5.count(s) == 1]
# print("Задача 5 v2:", result5_2)



# 6. Даны две строки. Создать список в который поместить те символы,
# которые есть в обеих строках хотя бы раз.
str6_1 = 'kdjfhkjghkdjfhgkjdfhgkhdfk'
str6_2 = 'skdfhgskjkjsfkshdfkjhsdkfh'
result6 = []
for s in set(str6_2).intersection(set(str6_1)):
    result6.append(s)
print("Задача 6:", result6)



# 7. Даны две строки. Создать список в который поместить те символы, которые есть в обеих строках,
# но в каждой только по одному разу.

str7_1 = 'aaaassseeeedffhycctz'
str7_2 = 'aaaassseeeedffhyztttc'
result7 = []
uni_str7_1 = [s for s in str7_1 if str7_1.count(s) == 1]
uni_str7_2 = [s for s in str7_2 if str7_2.count(s) == 1]
for _ in list(set(uni_str7_2).intersection(set(uni_str7_1))):
    result7.append(_)
print("Задача 7:", result7)

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
Mesto = ["Israel", "Karmiel", "Dizingof '8'"]
Work = ["Have Work", "Worker"]
Persona8 = {"SName" : "Ivanov",
            "FName" : "Ivan",
            "Age" : "33",
            "Live in" : Mesto,
            "Work" : Work}
print("Задача 8:", Persona8)

# 9. Описать с помощью словаря следующую структуру (рецепт ненастоящего торта,
# придумать и указать граммы для продуктов):
KG = {50: "50 грамм",
      100: "100 грамм",
      200: "0,2 кг",
      500: "0,5 кг",
      1000: "Один кг"}
Korj = {"Мука": KG[200],
        "Молоко": KG[1000],
        "Масло": "150 г.",
        "Яйцо": "3 шт."}
Krem =  {"Сахар": KG[1000],
        "Масло": "50 г.",
        "Ваниль": "0,02 Кг.",
        "Сметана": "3 Ст.Л."}
Glazur = {"Какао": "1 стакан",
        "Сахар": "0,15 Кг.",
        "Масло": "30 г."}
Ing_step = {"Корж": Korj,
            "Крем": Krem,
            "Глазурь": Glazur}
Tort = {"Состовляющие торта": Ing_step}

print("Задача 9:", Tort)