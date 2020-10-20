import random
import string
import json
import csv

############### 1
def gen_txt(min_len=100, max_len=1000)-> str:
    alphavit = str(string.ascii_letters + string.digits + ' ' + '.' + ','+ ';')
    stroka100_1000 = (''.join(random.choice(alphavit) for _ in range(random.randint(min_len, max_len))))
    inxs_random = list(set([random.randint(1, len(stroka100_1000) - 1) for _ in range(9)]))
    list_s_100_1000 = list(stroka100_1000)
    for index, value in enumerate(list_s_100_1000):
        for i in inxs_random:
            if index == i:
                list_s_100_1000.remove(value)
                list_s_100_1000.insert(i, '\n')
            else:
                pass

    return "".join(list_s_100_1000)


print('1. ===>', 'длина:', len(gen_txt()), gen_txt())

################## 2
def rand_chois_val(val):
    if val == 1:
        t_or_f =[True, False]
        val = random.choice(t_or_f)
    if val == 2:
        val = random.randint(-100, 100)
    if val == 3:
        val = random.uniform(0, 1)
    return val

def gen_json(min_key=5, max_key=20):
    alphavit = str(string.ascii_letters + string.punctuation)
    return {(''.join(random.choice(alphavit) for _ in range(5))): rand_chois_val(random.randint(1,3)) for key in range(random.randint(min_key, max_key))}

print('2. ===>', 'длина:', len(gen_json()), gen_json())

####################### 3
def gen_csv(n_min=3, m_max=10):
    n_stroka = random.randint(n_min, m_max)
    m_stolb = random.randint(n_min, m_max)
    tabl_out = [[random.randint(0, 1) for _ in range(m_stolb)] for _ in range(n_stroka)]
    return tabl_out

print('3. ===>',gen_csv())

############# file_writer

def for_txt(path: str):
    with open(path, 'w') as file:
        file.write(gen_txt())

def for_csv(path: str):
    with open(path, 'w') as file:
        writer = csv.writer(file, dialect='excel')
        writer.writerows(gen_csv())

def for_json(path: str):
    with open(path, 'w') as file:
        json.dump(gen_json(), file, indent=2)

def file_writer(path: str):
    mode = path.rsplit(".")[-1]
    if mode == "txt":
        for_txt(path)
    elif mode == "json":
        for_json(path)
    elif mode == "csv":
        for_csv(path)
    else:
        raise Exception("Unsupported file format!")

file_writer("/Users/clz/PycharmProject/Git Hillel Project/Hillel_ITP_Python_16_09/NEW_HOME_WORK/HW_10/test10.json")
