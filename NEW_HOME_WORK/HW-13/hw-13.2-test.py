import random
import string

name_for_card = '___6'

def gen_list_dict(name_f,rand_width)->list:
    out_list = []
    part_w = (rand_width // 4)
    if name_f[0] != '_':
        out_list.append({"object": {'class': name_f[0], "x_min": 0, "x_max": part_w * 1}})
    if name_f[1] != '_':
        out_list.append({"object": {'class': name_f[1], "x_min": part_w * 1, "x_max": part_w * 2}})
    if name_f[2] != '_':
        out_list.append({"object": {'class': name_f[2], "x_min": part_w * 2, "x_max": part_w * 3}})
    if name_f[3] != '_':
        out_list.append({"object": {'class': name_f[3], "x_min": part_w *3, "x_max": rand_width}})
    return out_list

print(gen_list_dict(name_for_card, 400))

    #
    #
    # a = [
    #                 {"object": {'class': name_f[0], "x_min": 0, "x_max": part_w * 1}},
    #                 {"object": {'class': name_f[1], "x_min": part_w * 1, "x_max": part_w * 2}},
    #                 {"object": {'class': name_f[2], "x_min": part_w * 2, "x_max": part_w * 3}},
    #                 {"object": {'class': name_f[3], "x_min": part_w * 3, "x_max": rand_width}}
    #             ]


# def gen_data_for_file(name_f = name_for_card)->dict:


# print(gen_data_for_file())


# def gen_json(min_key=5, max_key=20):
#     alphavit = str(string.ascii_letters + string.punctuation)
#     return {(''.join(random.choice(alphavit) for _ in range(5))): random.randint(1,3) for key in range(random.randint(min_key, max_key))}
#
# print(gen_json())