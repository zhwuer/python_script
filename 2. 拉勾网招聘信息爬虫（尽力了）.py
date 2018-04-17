#!/usr/bin/python
# encoding=utf-8

import requests, codecs, json
from bs4 import BeautifulSoup


DOWNLOAD_URL = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false&isSchoolJob=0'

headers = {
    'Cookie':'JSESSIONID=ABAAABAABGFABEF171F7FC627E690F33989AB4A4D7A3BAC',
    'Host':'www.lagou.com',
    'Origin':'https://www.lagou.com',
    'Referer':'https://www.lagou.com/jobs/list_python?oquery=python&fromSearch=true&labelWords=relative',
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
    'X-Requested-With':'XMLHttpRequest'
}

def parse_json(json_data, page_num):
    json_obj = json.loads(json_data)
    content = json_obj.get('content').get('positionResult').get('result')
    for i in range(len(content)):
        data = content[i].get('companyShortName')+', '+content[i].get('positionName')+', '+content[i].get('salary')
        info.append(data)
    return DOWNLOAD_URL + '&pn=%d' % page_num

def download_page(url):
    return requests.get(url, headers=headers).content

def file_io(name, list_name):
    with codecs.open('%s.txt' % name, 'wb', encoding='utf-8') as f:
        f.write(u'{}'.format('\n'.join(list_name)))

def main():
    url = DOWNLOAD_URL
    global info
    page_num = 1
    info = []
    while url:
        page_num = page_num + 1
        json_data = download_page(url)
        try:
            url = parse_json(json_data, page_num)
        except AttributeError as e:
            break
    file_io('拉勾网招聘信息', info)
    print len(info)
     
    
if __name__ == '__main__':
    main()