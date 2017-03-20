
import nltk
from nltk import word_tokenize
import argparse
import re
import probability

from ngram import get_tokens, get_vocab

import ngram
import smoothing


def run(args, text):

    tokens = list(set(word_tokenize(text)))
    vocab = get_vocab(text)

    if args.no:
        unigrams, bigrams = smoothing.bigram_table(text)
        bigram_prob = probability.prob_table(tokens, unigrams, bigrams, vocab)
        sentences = text.split('\n')
        for sentence in sentences:
            probability.sentence_prob(sentence, bigram_prob)

    if args.aos:
        _, _ = smoothing.bigram_table(text)
        unigrams, bigrams = smoothing.add_one(text)
        bigram_prob = probability.prob_table(tokens, unigrams, bigrams, vocab)
        sentences = text.split('\n')
        for sentence in sentences:
            probability.sentence_prob(sentence, bigram_prob)

    if args.gtd:
        _, _ = smoothing.bigram_table(text)
        N_total, bigrams = smoothing.good_turing(text)
        unigrams = None
        bigram_prob = probability.prob_gtd(tokens, bigrams, N_total)
        sentences = text.split('\n')
        for sentence in sentences:
            probability.sentence_prob(sentence, bigram_prob)


def parse(text):
    text = re.sub('\.', '$', text)

    sentences = text.split('\n')
    sentences = ['^ ' + i for i in sentences]

    text = '\n'.join(sentences)

    print "Sentences being worked on: "
    print text

    return text


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Processing speeches.')
    parser.add_argument('--aos', action='store_true',
                        help='Add-One Smoothing Output')
    parser.add_argument('--gtd', action='store_true',
                        help='Good-Turing Discounting Output')
    parser.add_argument('--all', action='store_true',
                        help='Showing all Outputs')
    parser.add_argument('--no', action='store_true',
                        help='Showing Output Without Smoothing')
    args = parser.parse_args()

    file = open('data/sentences.txt', 'r')
    sentences = file.read().lower()
    file.close()

    sentences = parse(sentences)

    run(args, sentences)
