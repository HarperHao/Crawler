"""
学习了os
学习了图片的保存
学习了xpath快速写法
学习了urlparse对url的快速分割
"""
import os
import requests
from fake_useragent import UserAgent
from lxml import etree
from urllib.parse import urlparse

url = 'https://www.xiachufang.com/'
headers = {'User-Agent': UserAgent().chrome}
response = requests.get(url, headers=headers)
# print(response.status_code)


# 爬取图片
e = etree.HTML(response.text)
images_url1 = e.xpath('//div/ul[@class="plain"]/li/div/a[@class="cover"]/img/@src')
images_url = []

# 对爬取的图片网址进行加工
for url in images_url1:
    n = urlparse(url)
    i = r"{0}://{1}{2}".format(n.scheme, n.netloc, n.path.split('@')[0])
    images_url.append(i)
# 爬取美食名字
names = e.xpath('//div[@title]/@title')
names.reverse()  # 将列表反向
print(names)
print(images_url)
# 将图片保存到文件中
mydir = r'K:\计设\food_images'
#os.mkdir(mydir)
for image_url in images_url:
    name = names.pop()  # 出栈
    image_path = mydir + '\\' + name + '.jpg'
    r = requests.get(image_url)
    with open(image_path, 'wb')as f:
        f.write(r.content)
