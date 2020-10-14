import requests
from fake_useragent import UserAgent
import json


def get_orgId(search_Id):
    url = 'http://www.cninfo.com.cn/new/information/topSearch/detailOfQuery'
    detailOfQuery = {
        'keyWord': search_Id,
        'maxListNum': '5',
        'maxSecNum': '10'
    }
    headers = {
        'User-Agent': UserAgent().chrome
    }
    res = requests.post(url, params=detailOfQuery, headers=headers)
    return res.json()['keyBoardList'][0]['orgId']


headers = {
    'User-Agent': UserAgent().chrome
}
pageNum = '1'
pageSize = '30'
startDate = '2020-04-12'
endDate = '2020-10-12'
seDate = startDate + '~' + endDate
search_Id = '601668'
orgId = get_orgId(search_Id)
stock = ''
pdf_url = 'http://www.cninfo.com.cn/new/hisAnnouncement/query'
query = {
    'category': '',
    'column': 'szse',
    'isHLtitle': 'true',
    'pageNum': pageNum,
    'pageSize': pageSize,
    'plate': '',
    'searchkey': '',
    'secid': '',
    'seDate': seDate,
    'sortType': '',
    'stock': stock,
    'tabName': 'fulltext',
    'trade': ''
}
res = requests.post(pdf_url, headers=headers, params=query)
static_url = 'http://static.cninfo.com.cn/'
temp = res.json()['announcements']
pdf_urls = [static_url + item["adjunctUrl"] for item in temp]
titles = [item["announcementTitle"] for item in temp]
print(len(pdf_urls))
print(len(titles))
result = zip(titles, pdf_urls)
print(list(result))
