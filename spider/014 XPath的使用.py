import requests
from lxml import etree
from fake_useragent import UserAgent

url = 'https://www.qidian.com/rank/hotsales'
headers = {'User-Agent': UserAgent().chrome}
response = requests.get(url, verify=False, headers=headers)
e = etree.HTML(response.text)
names = e.xpath(r'//h4/a/text()')
# print(type(e))
authers = e.xpath(r'//p[@class="author"]/a[@class="name"]/text()')
for name, auther in zip(names, authers):#元组列表
    print(name, ':', auther)
