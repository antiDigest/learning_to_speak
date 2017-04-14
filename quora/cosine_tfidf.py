
from nltk import word_tokenize
import pandas as pd

import sys
sys.path.append('../.')
from utils.similarity import cosine
from utils.tfidf import tfidf

reload(sys)
sys.setdefaultencoding('utf-8')

train = pd.read_csv('../quora/data/train.csv')
test = pd.read_csv('../quora/data/test.csv')

train_qs = train[['id', 'question1', 'question2', 'is_duplicate']]
test_qs = test[['test_id', 'question1', 'question2']]

qlist = []
for row in train_qs.itertuples():
    # print row
    try:
        if len(list(row[2])) > 10:
            qlist.append(word_tokenize(
                row[2].decode('utf8', errors='ignore')))
        if len(list(row[3])) > 10:
            qlist.append(word_tokenize(
                row[3].decode('utf8', errors='ignore')))
    except TypeError or UnicodeDecodeError:
        pass

# print len(qlist)
# print 'All Questions added to list'

for row in test_qs.itertuples():
    wordvec1 = word_tokenize(row[2])
    wordvec2 = word_tokenize(row[3])
    words = wordvec1 + wordvec2
    words = list(set(words))

    v1 = tfidf(wordvec1, qlist)
    v2 = tfidf(wordvec2, qlist)
    vec1 = []
    vec2 = []
    for word in words:
        try:
            vec1.append(v1[wordvec1.index(word)])
        except ValueError:
            vec1.append(0)
        try:
            vec2.append(v2[wordvec2.index(word)])
        except ValueError:
            vec2.append(0)

    print str(row[1]) + "," + str(cosine(vec1, vec2))
