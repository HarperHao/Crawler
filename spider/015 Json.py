import json

dict1 = {'name': '吕昊'}
# dumps将dict类型转换为str(json字符串)类型
str1 = json.dumps(dict1, ensure_ascii=False)
# loads将json字符串类型转化为Python类型
dict2 = json.loads(str1)
# print(dict2)
# dump将python内置类型转化为json字符串类型后保存到文件中去
# 序列化时默认按ascill编码转
json.dump(dict2, open('individual.txt', 'w', encoding='utf-8'), ensure_ascii=False)
# 将文件中的json文件转化为Python类型后，读取出来
obj = json.load(open('individual.txt', 'r', encoding='utf-8'))
print(type(obj))
