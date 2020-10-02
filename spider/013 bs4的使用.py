from bs4 import BeautifulSoup
from bs4.element import Comment

html = """
<title>尚学堂</title>
<div id='title' float='left'>Welcome to SXT</div>
<div class='info' float='right'>
    <span>Good Good Study</span>
    <a href='www.bjsxt.cn'></a>
    <strong><!--没用--></strong>
</div>"""
soup = BeautifulSoup(html, 'lxml')
# print('-------------获取标签-----------------')
# print(soup.title)
# print(soup.span)
# print(soup.div)
# print('-------------获取属性-----------------')
# print(soup.div.attrs)
# print(soup.a['href'])
# print(soup.div.get('float'))
# print('-------------获取内容-----------------')
# print(soup.strong.string)  # 会把注释也输出来
# print(soup.strong.text)  # 不会把注释输出来
# if (type(soup.strong.string) == Comment):
#     print('有注释')
#     print(soup.strong.prettify())
# else:
#     print(soup.strong.string)
# print('-------------find_all()-----------------')
# print(soup.find_all('div'))
# print(soup.find_all(class_='info'))
# print(soup.find_all('div', attrs={'float': 'right'}))
print('-------------css选择器-----------------')
# print(soup.select('div.info>span'))
# print(soup.select('title'))
# print(soup.select('#title'))
# print(soup.select('.info'))
print(soup.select('div[class ="info"]'))
