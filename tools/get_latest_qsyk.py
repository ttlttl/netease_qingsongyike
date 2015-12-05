import json
import sys
sys.path.extend(['..'])
import requests
from flask_sqlalchemy import SQLAlchemy
from manage import app
from app.models import Qingsongyike

db = SQLAlchemy(app)
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
    article_list = get_article_list(url, key)
    qingsongyike_list = [a for a in article_list if "每日轻松一刻" in a['title']]
    return qingsongyike_list

def get_qingsongyike_body(docid, timeout=20):
    url = "http://c.3g.163.com/nc/article/%s/full.html" % str(docid)
    r = requests.get(url, timeout=timeout)
    if r.status_code != 200:
        print('Unable to load url %s, status code: %s' % (url, r.status_code))
        return None
    data = r.json()
    if data:
        data = data[docid]
        imgs = data['img']
        body = data['body']
        for img in imgs:
            body = body.replace(img['ref'], "<img class=\"img-responsive\" src=\"" + img['src'] + "\"/><hr>")
        body = body.replace('%', '%%')
    return body

def save_qingsongyike_to_db(qingsongyike):
    new = Qingsongyike()
    new.ptime = qingsongyike['ptime']
    new.docid = qingsongyike['docid']
    new.title = qingsongyike['title']
    new.cover_img = qingsongyike['imgsrc']
    new.url_3g = qingsongyike['url']
    new.body = get_qingsongyike_body(qingsongyike['docid'])

    db.session.add(new)
    db.session.commit()


def get_latest_qingsongyike():
    url = "http://c.m.163.com/nc/article/list/T1350383429665/0-1.html"
    key = "T1350383429665"
    qingsongyike_list = get_qingsongyike_list(url, key)
    for qingsongyike in qingsongyike_list:
        save_qingsongyike_to_db(qingsongyike)
    db.session.query()
    db.session.close()

if __name__ == '__main__':
    get_latest_qingsongyike()