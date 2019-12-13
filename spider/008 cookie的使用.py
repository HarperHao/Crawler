from urllib.request import Request, build_opener, HTTPCookieProcessor
from fake_useragent import UserAgent
from urllib.parse import urlencode
#此网站已为404，需要换网站
login_url = 'http://www.sxt.cn/index/login/login'
form_data = {
    'user': '17703181473',
    'password': '123456'
}
info_url = 'http://www.sxt.cn/index/user.html'
headers = {
    'User-Agent': UserAgent().chrome
}
request = Request(login_url, headers=headers, data=urlencode(form_data).encode())
handler = HTTPCookieProcessor()
opener = build_opener(handler)
response = opener.open(request)
# ---------------登录成功----------------
request = Request(info_url, headers=headers)
response = opener.open(request)
print(response.read().decode())
