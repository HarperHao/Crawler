import requests
import json
from fake_useragent import UserAgent
from jsonpath import jsonpath

url = 'https://www.lagou.com/lbs/getAllCitySearchLabels.json'
headers = {'User-Agent': UserAgent().chrome}
response = requests.get(url, headers=headers)
obj = json.loads(response.text)
print(type(obj))
# citynames = jsonpath(obj, '$..name')
# cityids = jsonpath(obj, '$..id')
# # print(type(cityids))
# with open('city.json', 'w', encoding='utf-8')as f:
#     citydict = dict(zip(citynames, cityids))
#     json.dump(citydict, f, ensure_ascii=False)
