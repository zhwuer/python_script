#!/usr/bin/python
# encoding=utf-8

import requests, codecs
from bs4 import BeautifulSoup

DOWNLOAD_URL = 'https://www.douyu.com/directory/game/DOTA2'

def parse_html(html):
    soup = BeautifulSoup(html, "html.parser")
    next = soup.find('div', attrs={'class':'container'})
    next = next.find('div', attrs={'class':'tse-content padding-left0 padding-right0'})
    live_list = next.find('div', attrs={'class':'items items01 item-data clearfix'})
    for each in live_list.find_all('li'):
        live_name = each.find('h3', attrs={'class':'ellipsis'}).getText().strip()
        anchor_name = each.find('span', attrs={'class':'dy-name ellipsis fl'}).getText().strip()
        anchor_popu = each.find('span', attrs={'class':'dy-num fr'}).getText().strip()
        room_num = each.attrs['data-rid']
        list_data.append(live_name+', '+anchor_name+', '+anchor_popu+', '+room_num)
    
    
def download_page(url):
    return requests.get(url, headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
        }).content
        
def file_io(name, list_name):
    with codecs.open('%s.txt' % name, 'wb', encoding='utf-8') as f:
        f.write(u'{}'.format('\n'.join(list_name)))

def main():
    url = DOWNLOAD_URL
    global list_data
    list_data = []
    html = download_page(url)
    parse_html(html)
    file_io("斗鱼", list_data)

if __name__ == '__main__':
    main()