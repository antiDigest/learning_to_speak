from collections import Counter
from glob import glob
import json
import argparse
import re
import pandas as pd


def routine():
    vocab = {}
    pres = []
    for file in glob('speech/speeches/*.txt'):
        fopen = open(file, 'r')
        address = fopen.readline()
        name = fopen.readline().split('\n')[0]
        print name
        text = re.split(r'[\n*\s\b\'\.\,\\\/\?\"\[\]\-\u\()\_]',
                        fopen.read().lower())
        text = list(set(text))
        if name in pres:
            vocab[name] += len(text)
        else:
            vocab[name] = len(text)
            pres.append(name)

    data = {k: v for k, v in vocab.items()}
    data = sorted(data.items(), key=lambda i: i[1], reverse=True)
    df = pd.DataFrame.from_dict(data)
    df.to_csv('vocab.csv', index=False, header=['id', 'value'])
    # print json.dumps(Counter(text), indent=4, separators=(',', ': '))


def trump():
    fopen = open('speech/trump_speeches.txt', 'r')
    text = re.split(r'[\n*\s\b\'\.\,\\\/\?\"\[\]\-\u\()\_]',
                    fopen.read().lower())
    # values = Counter(text).values()
    text = [i for i in text if i != '']
    data = Counter(text)
    data = {k: v for k, v in data.items()}
    data = sorted(data.items(), key=lambda i: i[1], reverse=True)
    # dat = zip(data.keys(), data.values())
    df = pd.DataFrame.from_dict(data)
    df.to_csv('trump.csv', index=False, header=['id', 'value'])
    # print sum(values)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Processing speeches.')
    parser.add_argument('--trump', dest='trump', action='store_const',
                        const=sum, default=max,
                        help='For all trump speeches processing')

    args = parser.parse_args()
    if trump:
        trump()

    # if not trump:
    routine()
