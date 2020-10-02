import requests
import re
from fake_useragent import UserAgent

url = r'https://www.qiushibaike.com/text/'
headers = {
    'User-Agent': UserAgent().chrome
}
response = requests.get(url, headers=headers)
print(response.status_code)
response.encoding = 'utf-8'
print(response.text)
contents = re.findall(r'<div class="content">\s*<span>\s*(.+)<\span>', response.text)#\s匹配任意空白字符
with open('段子.txt', 'a', encoding='utf-8')as f:
    for info in contents:
        f.write(info + '\n\n')
