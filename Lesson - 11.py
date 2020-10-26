# import requests
# import json

########### Module Requests
# def get_response(url):
#     response = requests.get(url)
#     return response.json()
#
# def post_response(url, data):
#     response = requests.post(url, data=data)
#     return print(response.status_code)
#
# # "http://54.37.125.181/api/v1/basic/hello-world/"
# url_base = "http://54.37.125.181/api/v1/basic"
# url_hello = f"{url_base}/hello-world"
# url_ip = f"{url_base}/get-my-ip/"
# url_status = f"{url_base}/status" #/418
# url_text = f"{url_base}/text/"
# # response = requests.get(url_status)
# # status_code = response.status_code
# # text = response.text
#
#
#
# data = {"Kto zdes'?": "Prived Medved!"}
#
# post_response(url_text, data)
#
# res_json = get_response(url_text)
# print(json.dumps(res_json, indent=2), type(res_json))

############ F сортировки
# my_list = [1, 4, -5, 0]
# sort_list = sorted(my_list, reverse=True, key=abs)
# print(sort_list)

# my_list = ["1", "4", "zasd", "-5", "!0", "qwe", "zxc"]
# sort_list = sorted(my_list, key=len)
# print(sort_list)
# print(ord("!"), ord("4"))

# def sort_key(tmp_dict):
#     for key in tmp_dict:
#         return key
#
# my_list_dict = [{1945 : "Okonchanie VOV"},
#                 {1991 : "Nezavisimost Ukraini"},
#                 {988 : "Kreshenie Rusi"}]


# my_list_dict = [{"name" : "John", "age": 23},
#                 {"name" : "John", "age": 13},
#                 {"name" : "James", "age": 53},
#                 {"name" : "Jack", "age": 18}]
#
# def sort_key(tmp_dict):
#     return len(tmp_dict["name"]), tmp_dict["name"], tmp_dict["age"]
#
# sort_dict = sorted(my_list_dict, key=sort_key)
# print(sort_dict)

################### Регулярные вырожения
import re

my_str = "My e-mail: zontov@gmail.com.ua"
my_ip = "sdfsjdhfkjhsdf 213.123.12.3sdfsdfds234234234wer"
my_hw = "2nd July 1961"
# reg_ex = r"[a-z]+@[a-z]+.[a-z]+"
# reg_ip = r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}"
reg_hw = r"[0-9]{1,2}[a-z]{2} [A-Z]{1}[a-z]+ [0-9]{4}"
result = re.findall(reg_hw, my_hw)
# result = re.findall(reg_ip, my_ip) # список

print(result)