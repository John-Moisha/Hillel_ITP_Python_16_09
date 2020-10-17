from dateutil.parser import parse
path = "../Files/authors.txt"

def bday_or_death(path):
    file = open(path, "r")

    datal = []
    for line in file:
        if "birthday" in line or "death" in line:
            datal.append(line.replace("\n", ""))

    day_b = [line for line in datal if "birthday" in line]
    day_d = [line for line in datal if "death" in line]

    dict_b = {}
    for item in day_b:
        itempars = item.split('-')[0].strip()
        key = item.split('-')[1].split("birthday")[0].strip()
        value = parse(itempars).strftime('%Y/%m/%d')
        dict_b.update({key: value})

    dict_d = {}
    for item in day_d:
        itempars = item.split('-')[0].strip()
        key = item.split('-')[1].split("death")[0].strip()
        try:
            value = parse(itempars).strftime('%Y/%m/%d')
        except:
            value = '1962/07/06'
        dict_d.update({key: value})

    dict_back = [{"Name": key, "B_day": dict_b.get(key), "D_day": dict_d.get(key)} for key in dict_b.keys() | dict_d.keys()]

    return dict_back
print(bday_or_death(path))