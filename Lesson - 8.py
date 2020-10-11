from functions import generade_list_ip_adress

number = 5
musk = "xxx.xx.xx.x"
# ip_list = generade_list_ip_adress(number, True, True)

# print(ip_list)

# open_file = open("Files/file_1.txt", "r")
# for line in open_file.readlines():
#     print("******")
#     print(line)
#     print("******")
# open_file.close()



data = []
with open("Files/simple_file.txt", "r") as open_file:
    data = [line.strip() for line in open_file.readlines()]
    # for line in open_file.readlines():
    #     data.append(int(pertrip()))

print(data)