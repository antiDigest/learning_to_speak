from collections import Counter
from glob import glob
import json
import argparse
import re
import pandas as pd


def routine():
    for file in glob('speeches/*.txt'):
        fopen = open(file, 'r')
        print file
        text = fopen.read().split(' ')
        print json.dumps(Counter(text), indent=4, separators=(',', ': '))
        break


def trump():
    fopen = open('trump_speeches.txt', 'r')
    text = re.split(r'[\n*\s\b\'\.\,\\\/\?\"\[\]\-\u\()\_]',
                    fopen.read().lower())
    # values = Counter(text).values()
    text = [i for i in text if i != '']
    data = Counter(text)
    data = sorted(data.items(), key=lambda i: i[0])
    # dat = zip(data.keys(), data.values())
    df = pd.DataFrame.from_dict(data)
    df.to_csv('trump.csv', index=False, header=['word', 'count'])
    # print sum(values)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Processing speeches.')
    parser.add_argument('--trump', dest='trump', action='store_const',
                        const=sum, default=max,
                        help='For all trump speeches processing')

    args = parser.parse_args()
    if trump:
        trump()
