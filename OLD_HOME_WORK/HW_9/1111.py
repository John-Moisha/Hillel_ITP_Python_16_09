from dateutil.parser import parse
a = "14th January 1898 - Lewis Carroll's birthday, author of Alice in Wonderland"

def from_text_to_digital(date_in_text: str) -> str:
    return str(parse(date_in_text).strftime("%Y/%m/%d"))

def list_to_dicts(line_from_list: str) -> dict:

    dict_name = {'name': line_from_list.split("-")[1].split("'")[0].strip()}
    dict_date = {'date': from_text_to_digital(line_from_list.split("-")[0].strip())[2:]}
    dict_name_date = {'name' : dict_name['name'], 'date': dict_date['date']}
    return dict_name_date

list_to_dicts(a)