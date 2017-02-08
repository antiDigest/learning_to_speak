
import nltk
from nltk import word_tokenize
import argparse

import ngram
import smoothing

import json


def probability(word, unigram_count, given=None, vocab=None, bigram_count=None):

    if not given:
        unigrams = dict(unigram_count)
        N = float(sum(unigrams.values()))
        return (float(unigram_count[word])) / float(N)

    else:
        if bigram_count == None:
            print "You need to provide the bigram count for prob(word|<some text>)."
            return
        try:
            given = given[-1]
        except Exception, e:
            # print 'Something wrong'
            raise RuntimeError(
                "There does not seem to be text 'given' for a bigram probability !")
        return float("{0:.3f}".format(((float(bigram_count[(given, word)])) / (float(unigram_count[given])))))


def prob_gtd(tokens, bigram_count, N_total):

    bigram_prob = {}
    print "\n"
    print "The bigram-probability table:"
    print tokens
    for token1 in tokens:
        element = []
        for token2 in tokens:
            bigram_prob[(token1, token2)] = float("{0:.4f}".format(
                float(bigram_count[(token1, token2)]) / float(N_total)))
            element.append(bigram_prob[(token1, token2)])

        print element, token1

    return bigram_prob


def prob_table(tokens, unigram_count, bigram_count, vocab):

    bigram_prob = {}
    print "\n"
    print "The bigram-probability table:"
    print tokens
    for token1 in tokens:
        element = []
        for token2 in tokens:
            bigram_prob[(token1, token2)] = probability(token2, unigram_count,
                                                        given=[
                                                            token1], vocab=vocab,
                                                        bigram_count=bigram_count)
            element.append(bigram_prob[(token1, token2)])
        print element, token1

    return bigram_prob


def sentence_prob(sentence, bigram_prob):

    sent_list = word_tokenize(sentence)
    print
    print "Probability of Sentence :", sentence, ":",

    mul = 1
    for word in sent_list[1:]:
        index = sent_list.index(word)
        given = sent_list[index - 1]
        mul *= bigram_prob[(given, word)]

    print float("{0:.30f}".format(mul))

    return
