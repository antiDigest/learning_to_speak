
import math
from collections import Counter

import numpy as np


def tf(question, word=None):
    if word == None:
        count = dict(Counter(question))
        q_len = len(question)
        q_tf = []
        for word in question:
            q_tf.append(float(count[word]) / float(q_len))

        return q_tf
    else:
        count = dict(Counter(question))
        q_len = len(question)
        return float(count[word]) / float(q_len)


def n_containing(qlist, word=None, question=None):
    if word == None and question == None:
        raise "You need to provide at least the word if not the question"
    elif word == None and question != None:
        n_count = []
        for word in question:
            n_count.append(float(sum([1 for q in qlist if word in q])))
        return n_count
    else:
        sum([1 for q in qlist if word in q])


def idf(qlist, word=None, question=None):
    if word == None and question == None:
        raise "You need to provide at least the word if not the question"
    elif word == None:
        q_idf = []
        for value in n_containing(qlist, question=question):
            q_idf.append(math.log(len(qlist) / (1 + value)))
        return q_idf
    else:
        return math.log(len(qlist) / (1 + n_containing(qlist, word=word)))


def tfidf(question, qlist, word=None):
    if not word:
        tf_idf = []
        q_tf = tf(question)
        q_idf = idf(qlist, question=question)
        for i in range(len(question)):
            tf_idf.append(q_tf[i] * q_idf[i])
        return tf_idf
    else:
        return tf(question, word=word) * idf(qlist, word=word)
