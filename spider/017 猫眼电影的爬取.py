from fake_useragent import UserAgent
import requests
from lxml import etree
from time import sleep


# 获取一个页面的Html信息
def get_html(url):
    headers = {'User-Agent': UserAgent().chrome}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        response.encoding = 'utf-8'
        return response.text
    else:
        return None


# //div/a[@data-act='movies-click'] movies_name
# 将页面上所有电影的Url地址返回
def parse_list(html):
    # 构造一个xpath解析对象
    e = etree.HTML(html)
    # movies_url = ['https://maoyan.com{}'.format(url) for url in e.xpath('//div[@class="movie-item"]/a/@href')]
    movies_url = ['https://maoyan.com' + url for url in e.xpath('//div[@class="movie-item"]/a/@href')]
    return movies_url


# 返回已经提取好的电影信息
def parse_index(html):
    e = etree.HTML(html)
    name = e.xpath('//h3[@class="name"]/text()')[0]
    type = e.xpath('//li[@class="ellipsis"][1]/text()')[0]
    actors = e.xpath('//div[@class="celebrity-container"]//a[@class="name"]/text()')
    actors = solve_actors(actors)
    return {'name': name, 'type': type, 'actors': actors}


def solve_actors(actors):
    actors1 = []
    for actor in actors:
        actors1.append(actor.strip())
    return set(actors1)


def main():
    num = eval(input('请输入要爬取多少页：'))
    for i in range(num):
        url = 'https://maoyan.com/films?showType=3&offset={}'.format(i * 30)
        list_html = get_html(url)
        movies_url = parse_list(list_html)
        #print(movies_url)
        # 处理一部电影
        for movie in movies_url:
            sleep(2)
            movie_html = get_html(movie)
            info = parse_index(movie_html)
            print(info)

    # for url in movies_url:
    #     print(url)


if __name__ == '__main__':
    main()
