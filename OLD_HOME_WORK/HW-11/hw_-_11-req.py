import requests
import json
import csv
import time
from random import randint

star_time = time.time()
url_req = "https://api.forismatic.com/api/1.0/"

def get_requests(key=False):
    if not key:
        key = randint(1,99999)
    params = {"method": "getQuote",
              "lang": "ru",
              "key": key,
              "format": "json"}
    r = requests.get(url_req, params=params)
    r_json = r.json()
    return {"Автор": r_json['quoteAuthor'], "Цитата": r_json['quoteText'], "Link": r_json['quoteLink']}

def list_from_requests(quantity=False):
    if not quantity:
        quantity = 100
    quotes_list = []
    q = 1
    while q <= quantity:
        r = get_requests()
        if (r['Автор'] != '') and (r not in quotes_list) and (r['Link'] not in quotes_list):
            quotes_list.append(r)
            q += 1
    return quotes_list

list_with_requests = list_from_requests()

def key_sort_author(dict_):
    return dict_['Автор']

to_file = sorted(list_with_requests, key=key_sort_author)

def write_json_requests(path: str):
    with open(path, "w") as file:
        json.dump(to_file, file, ensure_ascii=False, indent=2)
    end_time = time.time()
    all_time = end_time - star_time
    print("Записано в файл 'JSON' завершена!\n", f"За: {all_time}'s\n", "Файл:", path)

path_json = "Json_requests.json"
write_json_requests(path_json)
print("=========================")
def write_csv_requests(path):
    fieldsnames = list(to_file[0].keys())

    with open(path, 'w') as file:
        csvwriter = csv.DictWriter(file, fieldnames=fieldsnames, delimiter=',', lineterminator=f'\r\n --> ')
        csvwriter.writeheader()
        csvwriter.writerows(to_file)
    end_time = time.time()
    all_time = end_time - star_time
    print("Записано в файл 'CSV' завершена!\n", f"За: {all_time}'s\n", "Файл:", path)

path_csv = "csv_requests.csv"
write_csv_requests(path_csv)