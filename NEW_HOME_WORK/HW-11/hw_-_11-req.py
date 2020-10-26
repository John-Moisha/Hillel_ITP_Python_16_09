import requests
import json
from random import randint

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

def json_requests(path: str):
    with open(path, "w") as file:
        json.dump(to_file, file, ensure_ascii=False, indent=2)
    print("Записано в файл завершена!\n", "Файл:", path)

path = "./Json_requests.json"
json_requests(path)