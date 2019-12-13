from urllib.request import Request, urlopen
from time import sleep

url = 'https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start={}&limit=100'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
}
i = 0
while True:
    request = Request(url.format(i * 20), headers=headers)
    response = urlopen(request)
    info = response.read().decode()
    if info == '[]':
        break
    else:
        i += 1
    filename='第'+str(i)+'页'
    with open(filename,'w',encoding='utf-8')as f:
        f.write(info)
    sleep(2)
