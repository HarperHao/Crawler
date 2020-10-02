from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
url = 'https://www.baidu.com/'
driver.get(url)
# 输入要搜索的内容
driver.find_element_by_xpath('//input[@name="wd"]').send_keys('python')
# # 点击搜索按钮
driver.find_element_by_xpath('//input[@id="su"]').click()
# 获取源代码
sleep(3)
html = driver.page_source
print(html)
driver.quit()
