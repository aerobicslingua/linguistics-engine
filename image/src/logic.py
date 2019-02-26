import PoS
import querydict
import sys
import os

def parse_translate_vtt(url, filename):
    vtt_pos = PoS.parse_vtt(filename)
    for line in vtt_pos:
        for w in line['POS']:
            if w['pos'] not in ['PUNCT', 'SPACE', 'NUM', 'PART']:
                w['dict_content'] = querydict.query_one(url, w['text'])
    return vtt_pos


if __name__ == '__main__':
    vtt = sys.argv[1]
    os.environ['DE_URL'] = '127.0.0.1:3000'
    url = 'http://%s/query/%s'
    print(parse_translate_vtt(url, vtt))
