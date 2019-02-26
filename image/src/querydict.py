import urllib.request
import json
import os

def query_one(url, word):
    query_url = url % (os.environ.get('DE_URL'), word)
    content = json.loads(urllib.request.urlopen(query_url).read())
    print(content)
    if len(content)==1:
        return content[0]
    else:
        return None


def query_more(url, words):
    rs = []
    for w in words:
        rs.append(query_one(url, w))
    return rs

if __name__ == '__main__':
    os.environ['DE_URL'] = '127.0.0.1:3000'
    url = 'http://%s/query/%s'
    words = ['hello', 'wonder', 'great']
    print(query_more(url, words))
