from pyquery import PyQuery as pq
import requests
from fake_useragent import UserAgent

headers = {
    'User-Agent': UserAgent().chrome
}
url = 'https://movie.douban.com/chart'
html = requests.get(url, headers=headers).text
# 创建一个pq对象
doc = pq(html)

# print(doc('#content > div > div.article > div > div > table:nth-child(5) >tr >td >a').attr('title'))
table_names = doc(' #content > div > div.article > div > div>table>tr>td>a ')
table_stars = doc(' #content > div > div.article > div > div>table>tr>td:nth-child(2)').find(
    'span[class="rating_nums"]')
names = []
stars = []
# 获取电影的名字
for item in table_names:
    name = item.attrib.get('title')
    names.append(name)
# 获取电影的评分
for item in table_stars:
    star = item.text
    stars.append(star)

results = zip(names, stars)
with open("paihang.txt", 'a', encoding='utf-8')as f:
    for item in results:
        f.write(str(item))
        f.write('\n')
