a = "9th February 1881 - Dostoyevsky's death"
b = "9th February 1881 - Dostoyevsky's death"
a_2 = a.split('-')[1].split("death")[0].strip()
b_2 = b.split('-')[1].split("'")[0].strip()
dict = {}

print(a_2)
print(b_2)