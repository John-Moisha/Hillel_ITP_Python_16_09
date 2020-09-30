## ##                 ДЗ - Тип Данных - Пясковский Кирилл

###                              Задача 2
# value = input('Введите целое число:')
# value = int(value)
#
# if value % 5 == 0:
#     print(value * 2)
# elif not value % 5 == 0:
#     print(0)
# else:
#     print('Oops')
###### конец задачи 2 ####


###                               Задача 3
# fe = 'февраль'
# Fe = 'Февраль'
# ap = 'апрель'
# Ap = 'Апрель'
# Jun = 'Июнь'
# jun = 'июнь'
# Sep = 'Сентябрь'
# sep = 'сентябрь'
# Nov = 'Ноябрь'
# nov = 'ноябрь'
# jan = 'январь'
# Jan = 'Январь'
# mar = 'март'
# Mar = 'Март'
# maj = 'май'
# Maj = 'Май'
# jul = 'июль'
# Jul = 'Июль'
# aug = 'август'
# Aug = 'Август'
# oct = 'октябрь'
# Oct = 'Октябрь'
# dec = 'декабрь'
# Dec = 'Декабрь'
# value = input("В каком месяце вас интересует количество дней?:")
# value = str(value)
# if value == '4' or value == '04' or value == '6' or value == '06' or value == '9' or value == '09' or value == '11':
#     print('В "' + value + '" месяце 30 дней')
# elif value == '1' or value == '01' or value == '3' or value == '03' or value == '5' or value == '05' or value == '7' or value == '07' or value == '8' or value == '08' or value == '10' or value == '12':
#     print('В  "' + value + '" месяце 31 дней')
# elif value == '2' or value == '02':
#     print('В "' + value + '" месяце 28')
# elif value == ap or value == Ap or value == jun or value == Jun or value == Sep or value == sep or value == Nov or value == nov:
#     print('В месяце "' + value + '" 30 дней')
# elif value == jan or value == Jan or value == mar or value == Mar or value == maj or value == Maj or value == jul or value == Jul or value == aug or value == Aug or value == oct or value == Oct or value == dec or value == Dec:
#     print('В месяце "' + value + '" 31 дней')
# elif value == fe or value == Fe:
#     print('В месяце "' + value + '" 28 дней')
# else:
#     print('"'+ value +'" такого месяца не существует,\n может попробуете снова?')
##### конец задачи 3


###     другой вариант решение 3 задачи но его еще не доделал
###     не понимаю как сделать чтоб при значении value type(str) выполнялись одни значения
###     а при type(int) выполнялиьс другие, и при значении остальных типов писалась просто ошибка.
#
#
##   в таком варианте класно работает если type(int) но как добавить еще type(str)
#
value = input("В каком месяце вас интересует количество дней?:")
if 0 <= float(value) > 0:
   print("такого не может быть")
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
  print('Oops')
#
# ###