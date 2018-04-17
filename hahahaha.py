#!/usr/bin/python
# encoding=utf-8

import requests, codecs, os, sys
reload(sys)
sys.setdefaultencoding('utf-8')
from bs4 import BeautifulSoup


def update_url(url):
    return requests.get(url).url

DOWNLOAD_URL = 'https://www.uuu113.com/'
DOWNLOAD_URL = update_url(DOWNLOAD_URL)
print(DOWNLOAD_URL)
kind_list = ['/htm/novellist1/','/htm/novellist2/','/htm/novellist4/','/htm/novellist5/','/htm/novellist6/','/htm/novellist8/','/htm/novellist9/','/htm/novellist10/']
    
def download_all_article(url, string):
    if not os.path.exists('ml/%s' % string):
        os.mkdir('ml/%s' % string)
    num = 50
    while num > 0:
        html = download_page(url)
        soup = BeautifulSoup(html, "html.parser")
        name = soup.find('head').find('title').getText().split('-')[0]
        text = soup.find('div', attrs={'class':'novelContent'}).getText().replace('<br/>','')
        file_io(name, text, string)
        url = DOWNLOAD_URL + soup.find('span', attrs={'class':'next'}).find('a')['href']
        num = num - 1

def get_first_article(html):
    soup = BeautifulSoup(html, "html.parser")
    next = soup.find('ul', attrs={'class':'textList'})
    first = next.find_all('li')[0]
    return DOWNLOAD_URL + first.find('a')['href']

def download_page(url):
    return requests.get(url, headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
        }).content
        
def file_io(name, list_name, path):
    try:
        if '/' in name:
            name = name.replace('/', '')
        with codecs.open('ml/%s/%s.txt' % (path, name), 'wb', encoding='utf-8') as f:
            f.write(u'{}'.format(list_name))
    except IOError as e:
        print e

def main():
    if not os.path.exists('ml'):
        os.mkdir('ml')
    for each in range(len(kind_list)):
        url = DOWNLOAD_URL + kind_list[each]
        html = download_page(url)
        first_article = get_first_article(html)
        download_all_article(first_article, str(each))
    
if __name__ == '__main__':
    main()