import spacy
import webvtt
import sys
nlp = spacy.load('en')

def parse_sentence(sentence):
    item = {'sentence': sentence, 'POS':[]}
    doc = nlp(sentence)
    for token in doc:
        item['POS'].append({'text': token.text, 'pos': token.pos_})
    return item

def parse_vtt(vttfile):
    result = []
    for caption in webvtt.read(vttfile):
        item = parse_sentence(caption.text)
        item['start'] = caption.start
        item['end'] = caption.end
        result.append(item)
    return result

if __name__ == '__main__':
    vtt = sys.argv[1]
    print(parse_vtt(vtt))

