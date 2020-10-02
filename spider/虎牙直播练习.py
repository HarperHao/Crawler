from selenium import webdriver
from time import sleep

# 构造一个浏览器
chrome = webdriver.Chrome()
url = 'https://www.huya.com/l'
chrome.get(url)
sleep(3)
while True:
    temp1 = chrome.find_elements_by_class_name('nick')
    temp2 = chrome.find_elements_by_class_name('js-num')
    # 主播名字
    names = [temp.text.strip() for temp in temp1]
    # 主播人气
    counts = [temp.text.strip() for temp in temp2]
    temp3 = sorted(zip(names, counts), key=lambda s: s[1], reverse=True)
    for name, count in temp3:
        print(name, ':', count)
    if chrome.page_source.find('laypage_next') != -1:
        chrome.find_element_by_class_name('laypage_next').click()
        sleep(3)
    else:
        break
chrome.quit()
