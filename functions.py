from random import randint

# def get_rand():
#     print(randint(0, 255))

def get_rand_0_255():
    return randint(0, 255)

def get_ip():
    ip_parts = [str(get_rand_0_255()) for _ in range(4)]
    return ".".join(ip_parts)

def sort_ip_key(ip):
    ip_parts = ip.split(".")
    # print("=====",ip_parts)
    # key_list = []
    # for part in ip_parts:
    #     print("---->", part)
    #     key_list.append(int(part))
    # print(key_list)
    # return key_list
    return [int(part) for part in ip.split(".")]


def generade_list_ip_adress(number: int, repeat=True, sort=False) -> list:
    # print(repeat)
    ip_list = []
    for _ in range(number):
        ip_list.append(get_ip())
    if not repeat:
        ip_list = list(set(ip_list))
    if sort:
        ip_list.sort(key=sort_ip_key)
    return ip_list
