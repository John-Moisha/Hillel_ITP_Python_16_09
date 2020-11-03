# import re
# text_ = "c. 287 BC – 212 BC"
# # split_text = text_
# # print(split_text)
# re_ = r'[0-9]+'
# result = re.findall(re_, text_)
# -212 -270
# print(result)

# b = int(result[-1])
# a = -int(result[-1])
# list_ =[a, b]
# print(sorted(list_))
#
# # print(int(result[-1]))
# # print(-int(result[-1]))
# # print(type(-int(result[-1])))
# # print(result)
#
list_ = []

txt = '_12_ab'
if txt[0] != '_':
    list_.append({"1":"a", "2": txt[0]})
    print('отлично')
elif txt[0] == '_':
    print('hernya')

print(list_)

