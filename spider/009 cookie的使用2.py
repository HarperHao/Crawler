from urllib.request import Request, build_opener, HTTPCookieProcessor
from fake_useragent import UserAgent
from urllib.parse import urlencode
from http.cookiejar import MozillaCookieJar


def get_cookie():
    login_url = 'http://learn.open.com.cn/Account/Login'
    form_data = {
        'user': 'jxt17703612482',
        'password': 'JXTjxt00'
    }

    headers = {
        'User-Agent': UserAgent().chrome
    }
    request = Request(login_url, headers=headers, data=urlencode(form_data).encode())
    cookie_jar = MozillaCookieJar()
    handler = HTTPCookieProcessor(cookie_jar)
    opener = build_opener(handler)
    response = opener.open(request)
    cookie_jar.save('cookie.txt', ignore_discard=True, ignore_expires=True)
    # ---------------登录成功----------------


def use_cookie():
    info_url = 'http://www.sxt.cn/index/user.html'
    headers = {
        'User-Agent': UserAgent().chrome
    }
    request = Request(info_url, headers=headers)
    cookie_jar = MozillaCookieJar()
    cookie_jar.load('cookie.txt', ignore_expires=True, ignore_discard=True)
    handler = HTTPCookieProcessor(cookie_jar)
    opener = build_opener(handler)
    response = opener.open(request)
    print(response.read().decode())


if __name__ == '__main__':
    get_cookie()
    use_cookie()
