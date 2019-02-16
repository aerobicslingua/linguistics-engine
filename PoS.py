#!/usr/bin/python3
import spacy
import webvtt
import sys
nlp = spacy.load('en')

vttfile = '/home/develop/Videos/sub.vtt'
def parse_sentence(sentence):
    item = {'sentence': sentence, 'POS':[]}
    doc = nlp(sentence)
    for token in doc:
        item['POS'].append({'text': token.text, 'pos': token.pos_})
    return item

if __name__ == '__main__':
    vttfile = sys.argv[1]
    for caption in webvtt.read(vttfile):
        item = parse_sentence(caption.text)
        item['start'] = caption.start
        item['end'] = caption.end
        print(item)
