#!/usr/bin/python
# encoding=utf-8

import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
import requests, codecs, time, sys
from bs4 import BeautifulSoup



Name = sys.argv[1]
ISOTIMEFORMAT = '%Y-%m-%d %X'
DOWNLOAD_URL = 'https://www.douyu.com/directory/game/DOTA2'

def parse_html(html):
    soup = BeautifulSoup(html, "html.parser")
    next = soup.find('div', attrs={'class':'container'})
    next = next.find('div', attrs={'class':'tse-content padding-left0 padding-right0'})
    live_list = next.find('div', attrs={'class':'items items01 item-data clearfix'})
    for each in live_list.find_all('li'):
        anchor_name = each.find('span', attrs={'class':'dy-name ellipsis fl'}).getText().strip()
        if Name in anchor_name:
            anchor_popu = each.find('span', attrs={'class':'dy-num fr'}).getText().strip()
            list_data.append(time.strftime(ISOTIMEFORMAT, time.localtime()) + ', ' + anchor_popu)
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
    x = 0
    pic, = plt.plot([], [])
    plt.xlabel('(mins)', color='g')
    plt.ylabel('(w)', color='g')
    plt.title('%s' % Name, color='g')
    while True:
        html = download_page(url)
        y = parse_html(html)
        pic.set_xdata(np.append(pic.get_xdata(), x))
        pic.set_ydata(np.append(pic.get_ydata(), y))
        try:
            plt.plot(x, y)
            plt.savefig('%s.png' % Name)
        except BaseException as e:
            break
        x += 1
        file_io('%s' % Name, list_data)
        plt.pause(1)

if __name__ == '__main__':
    main()