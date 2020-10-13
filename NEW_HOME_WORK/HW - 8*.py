from random import randint


def get_rand_0_255():
    return randint(0, 255)


def get_ip():
    ip_parts = [str(get_rand_0_255()) for _ in range(4)]
    return ".".join(ip_parts)


def part_for_musk(num: int):
    part_ip = 0
    if num == 1:
        part_ip = randint(0, 9)
    if num == 2:
        part_ip = randint(10, 99)
    if num == 3:
        part_ip = randint(100, 255)
    return part_ip


def by_musk(mask: str):
    ip_parts = []

    part1 = int(len(str(mask.split(".")[0])))
    ip_parts.append(str(part_for_musk(part1)))

    part2 = int(len(str(mask.split(".")[1])))
    ip_parts.append(str(part_for_musk(part2)))

    part3 = int(len(str(mask.split(".")[2])))
    ip_parts.append(str(part_for_musk(part3)))

    part4 = int(len(str(mask[::-1].split(".")[0])))
    ip_parts.append(str(part_for_musk(part4)))

    return ".".join(ip_parts)


def sort_ip_key(ip):
    return [int(part) for part in ip.split(".")]


def generate_list_ip_address(number: int, musk=False, repeat=True, sort=False) -> list:
    ip_list = []
    for _ in range(number):
        if not musk:
            ip_list.append(get_ip())
        else:
            ip_list.append(by_musk(musk))
    if not repeat:
        ip_list = list(set(ip_list))
    if sort:
        ip_list.sort(key=sort_ip_key)
    return ip_list


number = 3
mask = "x.xxx.xx.xx"
ip_list = generate_list_ip_address(number, mask)
print(ip_list)