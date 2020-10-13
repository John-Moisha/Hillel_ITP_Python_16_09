# from random import randint
# # mask = "xx.xx.xxx.x"
#
# def mask_num():
#
#     return num_x
#
# def open_names(fileurl):
#
#     file = open(fileurl, "r")
#     return [line.strip().split("\t")[1] for line in file]
#     return num_x
#
#
#
# def get_rand_0_255(num_x):
#     value_num_x = 0
#     if len(str(num_x)) == 1:
#         value_numx + randint(1, 9)
#     if len(str(num_x)) == 2:
#         value_num_x + randint(1,99)
#     if len(str(num_x)) == 3:
#         value_num_x + randint(1,255)
#     return value_num_x
#
#
#
# print(get_rand_0_255(1))
# # value_num_x = 0 + randint(1,100)
# # print(value_num_x)

mask = "xx.xxx.x.xx"
def mask_num(mask_str):
    return str(mask_str.split(".")[0])
    # num_x = 'dsf'
    # return num_x
print(mask_num(mask))