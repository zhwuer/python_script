#!/usr/bin/python
# encoding=utf-8

import requests, codecs
from bs4 import BeautifulSoup

DOWNLOAD_URL = 'https://movie.douban.com/top250'

def parse_html(html):
    soup = BeautifulSoup(html, "html.parser")
    movie_list = soup.find('ol', attrs = {'class':'grid_view'})
    
    for each in movie_list.find_all('li'):
        movie_name = each.find('span', attrs = {'class':'title'}).getText()
        movie_rate = each.find('span', attrs = {'class':'rating_num'}).getText()
        movies.append(movie_name + ' ' + movie_rate)
        
        next_page = soup.find('span', attrs={'class':'next'}).find('a')
    if next_page:
        return movies, DOWNLOAD_URL+next_page['href']
    return movies, None


def download_page(url):
    return requests.get(url, headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
        }).content

def file_io(name, list_name):
    with codecs.open('%s.txt' % name, 'wb', encoding='utf-8') as f:
        f.write(u'{}'.format('\n'.join(list_name)))
    
def main():
    url = DOWNLOAD_URL
    global movies
    movies = []
    while url:
        html = download_page(url)
        movies, url = parse_html(html)
    file_io('豆瓣_top250', movies)
    
if __name__ == '__main__':
    main()