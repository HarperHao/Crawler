import re

str = 'I study python3.7 everyday python'
# print('-' * 5 + 'match()' + '-' * 5)  # 从头开始匹配
# m1 = re.match(r'I', str)
# m2 = re.match(r'\w', str)
# m3 = re.match(r'.', str)
# m4 = re.match(r'\S', str)
# print(m4.group())
# print('-' * 5 + 'search()' + '-' * 5)  # 从任意位置开始匹配，匹配第一个
# s1 = re.search(r'study', str)
# s2 = re.search(r's\w+', str)
# s3 = re.search(r'I (\w+)', str)
# print(s3.group(1))
# print('-' * 5 + 'findall()' + '-' * 5)  # 从任意位置开始匹配，匹配所有
# f1 = re.findall(r'y', str)
# f2 = re.findall(r'python3.7', str)
# f3 = re.findall(r'p\w+3.7', str)#\w匹配字母数字及下划线
# f4 = re.findall(r'p.+\d', str)#\d匹配任意数字
# print(f4)
# print('-' * 5 + 'sub()' + '-' * 5)  # 替换所有
sub1 = re.sub(r'python', r'Python', str)
#sub2 = re.sub(r'p\w', r'Python', str)
print(sub1)
# print('-' * 5 + 'test()' + '-' * 5)  # 测试
