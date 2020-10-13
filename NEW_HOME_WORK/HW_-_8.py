import random
# 1. Написать функцию, которая считывает из файла domains.txt
# названия некоторых интернет доменов и возвращает их в виде списка строк (названия возвращать без точки).

def open_domains(fileurl):
    file = open(fileurl, "r")
    return [line[1::].strip() for line in file]

print(open_domains("../Files/domains.txt"))
for_domains = open_domains("../Files/domains.txt")
# 2. Написать функцию, которая считывает данные из файла names.txt
# и возвращает список всех фамилий из файла.
# Каждая строка файла содержит номер, фамилию, страну, некоторое число (таблица взята с википедии)

def open_names(fileurl):
    file = open(fileurl, "r")
    return [line.strip().split("\t")[1] for line in file]

print(open_names("../Files/names.txt"))
for_fname = open_names("../Files/names.txt")

# 3. Написать функцию для генерирования e-mail в формате:
# фамилия.число_от_100_до_999@строка_букв_длинной_от_5_до_7_символов.домен
# фамилию и домен брать из списков, полученных в задачах 1 и 2.
# Строку и число генерировать случайным образом. Буквы могут повторяться.
# Пример: miller.249@sgdyyur.com
def gen_mail(fname,domains):
    name = random.choice(fname)
    domain = random.choice(domains)
    ABC_alpha = 'qwertyuiopasdfghjklzxcvbnm'
    r_num = str(random.randint(100, 999))
    r_str = str(''.join(random.choice(ABC_alpha) for _ in range(random.randint(5,7))))
    return (name + "." + r_num + "@" + r_str + "." + domain)

print(gen_mail(for_fname,for_domains))

