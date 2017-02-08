import nltk
from nltk import word_tokenize
from collections import Counter
import json
import re


def get_tokens(text):
    text = re.sub('[\.]', '. ^', text)

    tokens = list(set(word_tokenize(text)))
    # vocab = len(tokens)

    return tokens


def unigrams(text, corpus=False):
    # Finding unigram -- single word -- counts and storing in a file for later
    # use

    if corpus:
        file = open('data/corpus.txt', 'r')
        text = file.read()

    text = re.sub('[\.]', '. ^', text)
    tokens = word_tokenize(text)

    unigram_counts = Counter(tokens)

    return unigram_counts, unigrams


def bigrams(text, corpus=False):
    # Finding bigrams and storing their counts in a file for later use

    if corpus:
        file = open('data/corpus.txt', 'r')
        text = file.read()

    text = re.sub('[\.]', '. ^', text)
    tokens = word_tokenize(text)

    bigrams = [(token, tokens[i + 1])
               for i, token in enumerate(tokens) if token != tokens[-1]]

    bigram_counts = Counter(bigrams)

    return bigram_counts, bigrams


def get_vocab(text, corpus=False):
    # Finding bigrams and storing their counts in a file for later use

    if corpus:
        file = open('data/corpus.txt', 'r')
        text = file.read()

    tokens = get_tokens(text)
    vocab = len(tokens)

    return vocab

if __name__ == '__main__':
    file = open('data/corpus.txt', 'r')
    text = file.read()

    unigram_counts, _ = unigrams(text)
    unigram_counts = {k: v for k, v in unigram_counts.items()}
    with open('data/unigram_counts.json', 'w') as file:
        json.dump(unigram_counts, file, indent=2)

    bigram_counts, _ = bigrams(text)
    bigram_counts = {str(k): v for k, v in bigram_counts.items()}
    with open('data/bigram_counts.json', 'w') as file:
        json.dump(bigram_counts, file, indent=2)

    print "Training done. Bigrams and Unigrams stored in bigram_counts.json and unigram_counts.json respectively."
