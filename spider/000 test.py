from selenium import webdriver

chrome = webdriver.Chrome()
url = 'https://www.baidu.com/'
chrome.get(url)
chrome.quit()