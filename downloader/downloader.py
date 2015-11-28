#-*-coding: utf-8 -*-

import requests
import json

def get_article_list(url, key, timeout=20):
    r = requests.get(url, timeout=timeout)
    if r.status_code != 200:
        print('Unable to load url %s, status code: %s' % (url, r.status_code))
        return None
    content = r.content
    decoded_content = content.decode('utf-8')
    data = json.loads(decoded_content)
    if not key in data.keys():
        print('Key %s not found in response data %s', (key, data))
        return None
    article_list = data[key]
    return article_list

def get_qingsongyike_list(url, key):
    print('Processing url %s' % url)
    qingsongyike_list = get_article_list(url, key)
    return qingsongyike_list

def test():
    url = "http://c.m.163.com/nc/article/list/T1350383429665/0-1.html"
    key = "T1350383429665"
    qingsongyike_list = get_qingsongyike_list(url, key)
    for qingsongyike in qingsongyike_list:
        print(qingsongyike)

if __name__ == '__main__':
    test()