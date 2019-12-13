from urllib.request import urlopen, Request
from urllib.parse import urlencode
from multiprocessing import Process

url = r"https://www.google.com/search?"
headers = {
    "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}
args = {
    'q': 'python'
}
url = url + urlencode(args)
# 构造好请求
request = Request(url, headers=headers)
print(request)
#print(dir(request))
# 发送请求
response = urlopen(request)
print(response.getcode())
info = response.read()
print(info.decode())
print(info)
