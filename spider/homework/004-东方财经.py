from multiprocessing import Pool
import requests
import re, json
from bs4 import BeautifulSoup
import time
import os

host = 'http://datainterface.eastmoney.com//EM_DataCenter/js.aspx?type=SR&sty=HYSR&sc=486&js=var%20kdOTUkVJ={%22data%22:[(x)],%22pages%22:%22(pc)%22,%22update%22:%22(ud)%22,%22count%22:%22(count)%22}&ps=5349&p=1&mkt=0&stat=0&rt=51109092'
# 链接里面有count,放在ps里面总数
testdownUrl = 'http://data.eastmoney.com/report/20180802/hy,APPIRJa63l8CIndustry.html'

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:55.0) Gecko/20100101 Firefox/55.0',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Connection': 'keep-alive',
    'Accept-Encoding': 'gzip, deflate',
    'Upgrade-Insecure-Requests': '1',
}


def savePdf(url, title):
    url_re = requests.get(url, headers=headers)
    folder = 'down/'
    if url_re.status_code == 200:  # 200是http响应状态
        # print('准备保存')
        if not os.path.exists(folder):  # 没有文件夹，则创建文件夹
            os.mkdir(folder)
        with open(folder + title + '.pdf', 'wb') as pdf:
            for chunk in url_re.iter_content(chunk_size=1024):
                if chunk:
                    pdf.write(chunk)

        print("文件地址为：" + folder + title + '.pdf')


def downPdf(url):
    try:
        url_re = requests.get(url, headers=headers)
        soup = BeautifulSoup(url_re.text, 'lxml')
        tag = soup.select_one('body > div.mainFrame > div > div.c62 > div > div > span > a')
        if tag == None: return
        downUrlString = tag.get('href')
        titleTag = soup.select_one('body > div.mainFrame > div > div.c62 > div > div > div.report-title > h1')
        title = titleTag.string.strip()
        title = title.replace('/', '与')
        savePdf(downUrlString, title)

    except Exception as e:
        print(e.message)
    # finally:
    # print("All words downloaded!")
    return


def getUrlsArray():
    url_rs = requests.get(host, headers=headers)
    print(url_rs.text)
    dict = url_rs.text.replace('var kdOTUkVJ=', '')
    jsonDict = json.loads(dict)
    array = jsonDict.get('data')
    newArray = []
    for dataString in array:
        stringArray = dataString.split(',')
        dateTime = stringArray[1]
        key = stringArray[2]
        formatDataTime = time.strptime(dateTime, "%Y/%m/%d %H:%M:%S")  # 转time obj
        formatDataTime = time.strftime('%Y%m%d', formatDataTime)
        url = 'http://data.eastmoney.com/report/{}/hy,{}.html'.format(formatDataTime, key)
        newArray.append(url)
        print(url)
        # url = 'http://data.eastmoney.com/report/20190703/hy,APPJ76sVaQftIndustry.html'
    return newArray


if __name__ == '__main__':
    urls = getUrlsArray()
    pool = Pool(processes=20)
    pool.map(downPdf, urls)
    # downPdf(testdownUrl)
