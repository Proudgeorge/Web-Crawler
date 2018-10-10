#！/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'CZH'
import requests
import re
import pprint
import json
import time
from requests.exceptions import RequestException
'''
    作者：陈自豪
    功能：抓取猫眼上评分前100的电影名称、时间、评分、图片等信息
    版本：1.0
    日期：09/10/2018
'''
def get_one_page(url):
    '''
    抓取一页的信息
    :param url:
    :return:
    '''
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0(Macintosh;Intel Mac OS X 10_11_4)AppleWebKit/537.76(KHTML,like Gecko)'
                'Chrome/52.0.2743.116 Safari/537.36'
        }
        response = requests.get(url,headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None

def parse_one_page(html):
    '''
    利用正则化表达式获取电影排名、图片、电影名、主演、上映时间、评分等信息
    :param html:
    :return:
    '''
    pattern = re.compile(
              '<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?name.*?a.*?>(.*?)</a>.*?star.*?>(.*?)</p>'
              '.*?releasetime.*?>(.*?)</p>.*?integer.*?>(.*?)</i>.*?fraction.*?>(.*?)</i>.*?</dd>',re.S)
    items = re.findall(pattern,html)
    for item in items:
        yield {
            'index':item[0],
            'image':item[1],
            'title':item[2].strip(),
            'actor':item[3].strip()[3:] if len(item[3]) > 3 else '',
            'time':item[4].strip()[5:] if len(item[4]) > 5 else '',
            'score':item[5].strip()+item[6].strip()
        }
    # pprint.pprint(items)

def write_to_file(content):
    '''
    将爬取的内容整理好后写入文件
    :param content:
    :return:
    '''
    with open('movie_board.txt','a',encoding='utf_8') as f:
        print(type(json.dumps(content)))
        f.write(json.dumps(content,ensure_ascii=False)+'\n')

def main(offset):
    url = 'http://maoyan.com/board/4?offset='+str(offset)
    html = get_one_page(url)
    # print(html)
    parse_one_page(html)
    for item in parse_one_page(html):
        print(item)
        write_to_file(item)

if __name__ == '__main__':
    for i in range(10):
        main(offset=i*10)
        time.sleep(1)  #为了应对反爬虫设置延时等待

