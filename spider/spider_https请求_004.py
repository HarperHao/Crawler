from urllib.request import Request,urlopen
import ssl
url='https://www.12306.cn/index/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
}
request=Request(url,headers=headers)
#忽略证书
context=ssl._create_unverified_context()
response=urlopen(request,context=context)
print(response.read().decode())