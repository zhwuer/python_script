#!/usr/bin/python
# encoding=utf-8

import requests, codecs
from bs4 import BeautifulSoup

DOWNLOAD_URL = ''

def parse_html(html):
    soup = BeautifulSoup(html, "html.parser")

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
    
if __name__ == '__main__':
    main()