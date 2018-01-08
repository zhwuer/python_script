#!/usr/bin/python
# encoding=utf-8

from matplotlib.font_manager import FontProperties
font = FontProperties(fname='/Library/Fonts/Microsoft/Microsoft Yahei.ttf') #设置中文字体
import matplotlib
matplotlib.use('Agg')    #不显示图片，直接保存下来，方便扔服务器上跑
import numpy as np
import matplotlib.pyplot as plt
import requests, codecs, time, sys
reload(sys)
sys.setdefaultencoding('utf-8')    #中文字体。。。
from bs4 import BeautifulSoup


Name = sys.argv[1]
ISOTIMEFORMAT = '%Y-%m-%d %X'
DOWNLOAD_URL = 'https://www.douyu.com/directory/game/DOTA2'

def get_time():
    return time.strftime(ISOTIMEFORMAT, time.localtime())

def parse_html(html):
    soup = BeautifulSoup(html, "html.parser")
    next = soup.find('div', attrs={'class':'container'})
    next = next.find('div', attrs={'class':'tse-content padding-left0 padding-right0'})
    live_list = next.find('div', attrs={'class':'items items01 item-data clearfix'})
    for each in live_list.find_all('li'):
        anchor_name = each.find('span', attrs={'class':'dy-name ellipsis fl'}).getText().strip()
        if Name in anchor_name:
            anchor_popu = each.find('span', attrs={'class':'dy-num fr'}).getText().strip()
            list_data.append(get_time() + ', ' + anchor_popu)
            return float(anchor_popu[0:-1])
            
    
def download_page(url):
    return requests.get(url, headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
        }).content
        
def file_io(name, list_name):
    with codecs.open('%s.txt' % name, 'wb', encoding='utf-8') as f:
        f.write(u'{}'.format('\n'+'\n'.join(list_name)))

def main():
    url = DOWNLOAD_URL
    global list_data
    list_data = []
    x_data = []
    y_data = []
    plt.xlabel('(分钟)', color='g', FontProperties=font)
    plt.ylabel('(万/人)', color='g', FontProperties=font)
    while True:
        html = download_page(url)
        x_data.append(get_time()[10:16].strip())
        x = range(len(x_data))
        y = parse_html(html)
        y_data.append(y)    #加入新的监测数据
        plt.title('%s %s直播间人数' % (get_time()[:10], Name), color='g', FontProperties=font)
        plt.xticks(x, x_data, rotation=90)
        plt.subplots_adjust(bottom=0.15)
        try:
            plt.plot(x, y_data)
            plt.savefig('%s.png' % Name)
        except BaseException as e:        #如果主播下播了，就抛出Exception，程序停止
            print e
            break
        file_io('%s' % Name, list_data)
        plt.pause(1)

if __name__ == '__main__':
    main()