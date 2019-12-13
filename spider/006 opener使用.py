from urllib.request import Request, build_opener
from fake_useragent import UserAgent
from urllib.request import HTTPHandler

url = r'http://httpbin.org/get'
ua = UserAgent()
# print(ua.random)
headers = {
    'User-Agent': ua.chrome
}
request = Request(url, headers=headers)
# HTTP控制器
handler = HTTPHandler()
opener = build_opener(handler)
response = opener.open(request)
print(response.read().decode())
