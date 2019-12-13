from urllib.request import urlopen, Request
from urllib.parse import quote


def get_html(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
    }
    request = Request(url, headers=headers)
    response = urlopen(request)
    print(response.getcode())
    return response.read().decode()


def save_html(html, filename):
    with open(filename, 'w', encoding='utf-8')as f:
        f.write(html)


def main():
    num = eval(input('请输入要获取多少页：'))
    content = input('请输入要获取哪个贴吧：')
    for i in range(num):
        url = 'http://tieba.baidu.com/f?fr=wwwt&kw={}&ie=utf-8&pn={}'.format(quote(content), i * 50)
        html = get_html(url)
        filename = '第' + str(i + 1) + '页.html'
        save_html(html, filename)


if __name__ == '__main__':
    main()
