from dateutil.parser import parse


path = "../Files/authors.txt"

def list_from_line(path):
    file = open(path, "r")
    datal = []

    for line in file:
        if "birthday" in line or "death" in line:
            datal.append(line.replace("\n", ""))

    return datal

lfl = list_from_line(path)
print("list ===>", list_from_line(path))

def back_date_name(list_a):
    dict1 = {}
    for item in list_a:
        itempars = item.split('-')[0].strip()
        key = item.split('-')[1].split("'")[0].strip()
        try:
            value = parse(itempars).strftime('%Y/%m/%d')
        except:
            value = '1962/07/06'
        dict1.update({key:value})
    return dict1

d_from_l = back_date_name(lfl)
print("dict ===>", back_date_name(lfl))

def dicts_from_dict(dict):
    my_str = []
    for key in dict:
        if key in dict:
            my_str.append({key: dict.get(key)})
    return my_str
print("dsfd ===>",dicts_from_dict(d_from_l))