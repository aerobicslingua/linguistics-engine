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
    os.environ['DICT_IP'] = '127.0.0.1'
    url = 'http://%s:3000/query/%s'
    print(parse_translate_vtt(url, vtt))
