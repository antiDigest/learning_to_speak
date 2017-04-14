
import nltk
from nltk.corpus import wordnet as wn
from nltk import word_tokenize
from nltk.corpus.reader import NOUN

import re
import numpy as np


class Lesk(object):

    def __init__(self):
        pass

    def getMostFrequent(self, word):
        senses = wn.synsets(word.lower())
        # print word.lower(), senses
        if senses == []:
            return word.lower(), senses
        maxValSense = len(senses[0].examples())
        freqSense = senses[0]
        for sense in senses:
            # print len(sense.examples())
            if len(sense.examples()) > maxValSense:
                maxValSense = len(sense.examples())
                freqSense = sense

        return freqSense, senses

    def computeOverlap(self, signature, context):

        # Base
        overlap = 0

        # Step
        for word in context:
            if word in signature:
                overlap += 1

        return overlap

    def adaptedLesk(self, sentence, word=None, context=None)

    def simplifiedLesk(self, sentence, word=None):

        if not word == None:
            bestSense, senses = self.getMostFrequent(word)
            maxOverlap = 0
            context = word_tokenize(sentence.lower())

            if senses == []:
                return 'ERROR: Cannot find a proper sense for the word !'

            for sense in senses:
                examples = [sense.definition()] + sense.examples()
                signature = []
                for example in examples:
                    signature += list(
                        set(re.split('[^\w]* [^\w]*', example.lower())))
                signature = list(set(signature))
                # print signature
                overlap = self.computeOverlap(signature, context)
                if overlap > maxOverlap:
                    maxOverlap = overlap
                    bestSense = sense

            return bestSense, bestSense.definition()

        else:
            sentence_senses = []
            for word in sentence:
                bestSense, senses = self.getMostFrequent(word)
                maxOverlap = 0
                context = sentence

                for sense in senses:
                    examples = [sense.definition()] + sense.examples()
                    signature = []
                    for example in examples:
                        signature += list(
                            set(re.split('[^\w]* [^\w]*', example.lower())))
                    signature = list(set(signature))
                    # print signature
                    overlap = self.computeOverlap(signature, context)
                    if overlap > maxOverlap:
                        maxOverlap = overlap
                        bestSense = sense

                sentence_senses.append((word, bestSense))
            return sentence_senses
