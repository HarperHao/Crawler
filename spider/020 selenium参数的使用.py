from selenium import webdriver

options = webdriver.ChromeOptions()


# 开启无头浏览器
def headless():
    options.add_argument('--headless')
    # 构造浏览器
    chrome = webdriver.Chrome(options=options)
    url = "https://www.baidu.com/"
    chrome.get(url)
    print(chrome.page_source)
    chrome.quit()


# 添加代理
def proxy():
    # options.add_argument('--proxy-server=type://if:port')
    #options.add_argument('--headless')
    options.add_argument('--proxy-server=http://39.137.69.10:80')
    # 构造浏览器
    chrome = webdriver.Chrome(options=options)
    url = "https://httpbin.org/get"
    chrome.get(url)
    print(chrome.page_source)
    chrome.quit()


proxy()
