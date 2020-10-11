str6_1 = 'kdjfhkjghkdjfhgkjdfhgkhdfk'
str6_2 = 'skdfhgskjkjsfkshdfkjhsdkfh'
result6 = []
for s in set(str6_2).intersection(set(str6_1)):
    result6.append(s)
print("Задача 6:", result6)