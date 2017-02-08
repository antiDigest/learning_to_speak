from glob import glob
import re

for file in glob('speeches/*.txt'):
    fopen = open(file, 'r+')
    print file
    l = [i for i in fopen.read().split('\n') if i != '' and i != ' ']
    # print l
    # index = l.index('George Washington')
    # print index
    id2 = l.index('CONTENTSBIBLIOGRAPHICRECORD')
    # print id2
    record = str('\n'.join(l[51:id2 - 1]))
    record = re.sub('\.[0-9]\n', '.', record)
    fopen.close()
    fopen = open(file, 'w')
    fopen.write(record)
    # break
