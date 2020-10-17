import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

headers = {
    'User-Agent': UserAgent().chrome
}
# 从0开始
url = r'https://movie.douban.com/subject/26885074/comments?start={}&limit=20&status=P&sort=new_score'

# 从1开始
css_names = '#comments > div:nth-child({}) > div.comment > h3 > span.comment-info > a'
css_contents = '#comments > div:nth-child({}) > div.comment > p > span'

names = []
contents = []
# 爬取3页的评论，每页有20个评论,总共才5页
for i in range(3):
    res = requests.get(url.format(i * 20), headers=headers)
    soup = BeautifulSoup(res.text, 'lxml')
    for j in range(20):
        name = soup.select(css_names.format(j + 1))[0].get_text()
        content = soup.select(css_contents.format(j + 1))[0].get_text()
        names.append(name)
        contents.append(content)

file_contents = list(zip(names, contents))
with open('yingping.txt', 'a', encoding='utf-8') as f:
    for item in file_contents:
        f.write(str(item))
        f.write('\n')
