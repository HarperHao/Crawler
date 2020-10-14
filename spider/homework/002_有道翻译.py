"""
Author:HarperHao
TIME:2020.10.9
FUNCUTION：英汉翻译
"""
import requests
from fake_useragent import FakeUserAgent
from parsel import Selector

word = input('请输入您要翻译的词:')
print('输入“0”停止查找！！！')
while word != '0':
    url = 'http://dict.youdao.com/search?q={}&keyfrom=new-fanyi.smartResult'.format(word)
    headers = {
        "User-Agent": FakeUserAgent().chrome
    }
    req = requests.get(url, headers=headers)
    sel = Selector(req.text)
    temp = sel.css('#phrsListTab > div.trans-container > ul ::text ').extract()
    res = [x.strip() for x in temp if (x.strip() != '')]
    for item in res:
        # 处理中文翻译的问题
        if item != ';' and not item.endswith('.'):
            print(item)
    print('--------------------------------------------------------------------')
    word = input('请输入您要翻译的词:')

print('查找结束！！！')
