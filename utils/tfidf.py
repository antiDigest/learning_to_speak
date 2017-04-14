
import math


def tf(question, word):
    if word not in question:
        return 0
    count = dict(Counter(question))
    q_len = len(question)
    return float(count[word]) / float(q_len)


def n_containing(qlist, word):
    return qlist[word]


def idf(qlist, word):
    return math.log(len(qlist) / (1 + n_containing(qlist, word)))


def tfidf(question, qlist, word):
    return tf(question, word) * idf(qlist, word)
