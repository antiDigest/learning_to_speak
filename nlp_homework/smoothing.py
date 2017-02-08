
import nltk
from nltk import word_tokenize
import ngram
from collections import Counter
import math

import json


def bigram_table(text):
    # For the Bigram Table - each element versus another element and their
    # count stored

    tokens = list(set(word_tokenize(text)))

    bigram_counts, _ = ngram.bigrams(text)
    unigram_counts, _ = ngram.unigrams(text)

    print "\nBigram Table without smoothing: "

    print tokens

    for token1 in tokens:
        element = []
        for token2 in tokens:
            element.append(bigram_counts[(token1, token2)])
        print element, "\t", token1

    return unigram_counts, bigram_counts


def add_one(text):
    tokens = list(set(word_tokenize(text)))
    vocab = len(tokens)

    bigram_counts, _ = ngram.bigrams(text)
    unigram_counts, _ = ngram.unigrams(text)

    print "\nBigram Table with add-one smoothing: "
    print tokens
    for token1 in tokens:

        unigram_counts[token1] += vocab
        element = []

        for token2 in tokens:
            if not bigram_counts[(token1, token2)]:
                bigram_counts[(token1, token2)] = 1
            else:
                bigram_counts[(token1, token2)] += 1
            element.append(bigram_counts[(token1, token2)])

        print element, token1

    return unigram_counts, bigram_counts


def good_turing(text):
    tokens = list(set(word_tokenize(text)))

    bigram_counts, _ = ngram.bigrams(text)
    unigram_counts, _ = ngram.unigrams(text)

    cs = list(set(dict(bigram_counts).values()))
    bigrams = dict(bigram_counts)

    N = {}
    for c in cs:
        N[c] = [word for word, count in bigrams.items() if count == c]

    N[0] = []
    for token1 in tokens:
        for token2 in tokens:
            if not bigram_counts[(token1, token2)]:
                N[0].append((token1, token2))

    N_total = 0
    for token in tokens:
        N_total += unigram_counts[token]

    print "\nBigram Table with Good-Turing smoothing: "
    print tokens
    for token1 in tokens:

        element = []
        for token2 in tokens:
            if not bigram_counts[(token1, token2)]:
                c = 0.0
                bigram_counts[(token1, token2)] = float("{0:.3f}".format(
                    (c + 1.0) * (float(len(N[c + 1])) / float(len(N[c])))))
            else:
                c = float(bigram_counts[(token1, token2)])
                if c == max(cs):
                    bigram_counts[(token1, token2)] = float(math.log(c))
                else:
                    bigram_counts[(token1, token2)] = \
                        float("{0:.3f}".format(
                            (c + 1.0) * (float(len(N[c + 1])) / float(len(N[c])))))
            element.append(bigram_counts[(token1, token2)])

        print element, token1

    return N_total, bigram_counts
