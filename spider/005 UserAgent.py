from urllib.request import Request, urlopen
from fake_useragent import UserAgent

url = r'http://httpbin.org/get'
ua = UserAgent()
headers = {
    'User-Agent': ua.chrome
}
request = Request(url, headers=headers)  # headers=只接受字典请求
response = urlopen(request)
print(response.read().decode())
