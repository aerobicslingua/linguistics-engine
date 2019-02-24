import urllib.request
import json
import os

def query_one(url, word):
    query_url = url % (os.environ.get('DICT_IP'), word)
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
    os.environ['DICT_IP'] = '127.0.0.1'
    url = 'http://%s:3000/query/%s'
    words = ['hello', 'wonder', 'great']
    print(query_more(url, words))
