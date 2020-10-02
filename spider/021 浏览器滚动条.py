from selenium import webdriver
from lxml import etree
from time import sleep

chrome = webdriver.Chrome()
url = 'https://search.jd.com/Search?keyword=%E7%AF%AE%E7%90%83%E9%9E%8B&enc=utf-8&wq=%E7%AF%AE%E7%90%83xie&pvid=649b9e8e275c40bb811ea883f8394754'
chrome.get(url)
# 先让滚动条拉到最后
js = 'document.documentElement.scrollTop=100000'
chrome.execute_script(js)
# 等待3s，让网页代码加载完
sleep(5)
html = chrome.page_source
e = etree.HTML(html)
#names的xpath路径有毛病
names = e.xpath('//div[@id="J_goodsList"]//li//a[@target="_blank"]//em/text()[2]')
temp_price = e.xpath('//div[@id="J_goodsList"]//div[@class="p-price"]/strong//i/text()')
price = [p.strip() for p in temp_price]
for name, _price in zip(names, price):
    print(name, ":", _price)
print(len(names))
print(len(temp_price))
chrome.quit()
