from urllib.request import Request, build_opener, ProxyHandler
from fake_useragent import UserAgent

url = 'http://httpbin.org/get'
headers = {
    'User-Agent': UserAgent().chrome
}
request = Request(url, headers=headers)
handler = ProxyHandler({'http': '183.146.213.157:80'})
#对于需要付费的ip需要有name和password
#handler=ProxyHandler({'http':'name:password@ip:port'})
opener = build_opener(handler)
response = opener.open(request)
print(response.read().decode())
