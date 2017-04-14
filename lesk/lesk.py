
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

    def getAll(self, word):
        senses = wn.synsets(word.lower())

        if senses == []:
            return word.lower(), senses

        gloss = {}
        nyms = ['hypernyms', 'hyponyms',
                'member_meronyms', 'part_meronyms', 'substance_meronyms']
        for i in nyms:
            gloss[i] = []

        for sense in senses:

            for i in nyms:
                try:
                    for syn in getattr(sense, i)():
                        gloss[i].append((syn, str(syn.definition())))
                except AttributeError as e:
                    print e
                    pass

        return gloss

    def computeOverlap(self, signature, context):

        # Base
        overlap = 0

        # Step
        for word in context:
            if word in signature:
                overlap += 1

        return overlap

    def Score(self, set1, set2):
        # Base
        overlap = 0

        # Step
        for i in range(len(set1)):
            for j in range(len(set2)):
                for word in set1[i][1]:
                    if word in set2[j][1]:
                        overlap += 1

        return overlap

    def overlapScore(self, word1, word2):
        nyms = ['hypernyms', 'hyponyms',
                'member_meronyms', 'part_meronyms', 'substance_meronyms']

        gloss_set1 = self.getAll(word1)
        gloss_set2 = self.getAll(word2)

        score = {}
        for i in nyms:
            score[i] = {}
            for j in nyms:
                score[i] += self.Score(gloss_set1[i], gloss_set2[j])

        print score

    def adaptedLesk(self, sentence, word, k):
        maxOverlap = 0
        context = word_tokenize(sentence.lower())

        index = context.index(word.lower())
        context = context[index - k:index + k]

        if senses == []:
            return None

        print self.overlapScore('pine', 'cone')
        # for sense in senses:

    def simplifiedLesk(self, sentence, word):

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

if __name__ == '__main__':
    sense = Lesk()

    print sense.overlapScore('pine', 'cone')
