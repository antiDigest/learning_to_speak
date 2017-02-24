
import sys


class Viterbi(object):
    # Viterbi Class

    def __init__(self, sequence):
        """
            The observations.csv is the file containing the observations.
            The hmm.csv is the file containing the Markov Model.

            Initialises the p_table taking the conditional probability table for observations 
            from conditional probability table and the p_chain for the markov chain related to 
            the hidden markv mmodel to be used.

        """
        OBS = 'data/observations.csv'
        HMM = 'data/hmm.csv'
        self.initPROB(OBS)
        self.initHMM(HMM)
        self.number = list(sequence)
        self.out_seq = []

    def initPROB(self, OBS):
        """
            Initialising the p_table taking the conditional probability table for observations
            from conditional probability in the file in "OBS".
        """
        file = open(OBS).read().split('\n')
        self.p_table = {}
        for i, line in enumerate(file):
            if i == 0:
                header = line.split(',')
                for head in header:
                    self.p_table[head] = []
            else:
                elements = line.split(',')
                for i, element in enumerate(elements):
                    self.p_table[header[i]].append(element)

    def initHMM(self, HMM):
        """
            Initialising the p_chain taking the markov chain table for the hidden markov model
            in the file in "HMM".
        """
        file = open(HMM).read().split('\n')
        self.p_chain = {}
        for i, line in enumerate(file):
            if i == 0:
                header = line.split(',')
                for head in header:
                    self.p_chain[head] = []
            else:
                elements = line.split(',')
                for i, element in enumerate(elements):
                    self.p_chain[header[i]].append(element)

    def viterbi(self):
        """
            The State sequence generator, takes as input the probability of next state given the first
            and the probability of having one state given an observation and maximises the sequence that
            can be made.
        """

        states = self.p_table.keys()

        viterbi = [{}]

        for state in states:
            prob = float(self.probNext(state, 'START')) * \
                float(self.probGiven(int(self.number[0]), state))
            viterbi[0][state] = {'prob': prob, 'prev': None}

        for t in range(1, len(self.number)):
            viterbi.append({})
            for state in states:
                maxProb, prevState = max([(float(self.probNext(state, prev)) *
                                           viterbi[t - 1][prev]['prob'], prev)
                                          for prev in states], key=lambda i: i[0])
                maxProb = maxProb * \
                    float(self.probGiven(int(self.number[t]), state))

                viterbi[t][state] = {'prob': maxProb, 'prev': prevState}

            # print viterbi[t]

        max_elem, max_prob, max_prev = max([(key, value["prob"], value['prev'])
                                            for key, value in viterbi[-1].items()], key=lambda i: i[1])

        sequence = []
        sequence.insert(0, max_elem)

        k = len(viterbi) - 2
        while max_prev != None:
            sequence.insert(0, max_prev)
            max_prev = viterbi[k][max_prev]['prev']
            k -= 1

        self.printStateSeq(sequence)

    def nextMax(self, number, previous):
        """
            Returns the next state with maximum probability.
        """
        states = []
        for state in self.p_table.keys():
            states += [(state, float(self.probGiven(number, state)) *
                        float(self.probNext(state, prev[0])) *
                        prev[1]) for prev in previous]
        return states

    def probGiven(self, a, given):
        """
            Returns the probability of a state given an observation.
        """

        return self.p_table[given][a - 1]

    def probNext(self, second, first):
        """
            Returns the probability of a state given the previous state.
        """

        index = self.p_chain['STATE'].index(first)

        return self.p_chain[second][index]

    def printStateSeq(self, sequence):
        """
            Prints the sequence of states.
        """

        print 'Weather (Output Sequence): ',
        for state in sequence:
            if state == 'HOT':
                sys.stdout.write('H')
            if state == 'COLD':
                sys.stdout.write('C')

        print
