# CKY Parser
from cfg import CFG

import nltk
import itertools
import sys
from tabulate import tabulate
from texttable import Texttable


class CKY():

    def display(self):
        print 'Table'
        print
        print tabulate(self.cky_table)
        # t = Texttable()
        # t.add_rows(self.cky_table)
        # print t.draw()
        # for line in self.cky_table:
        #     for cell in line:
        #         print '-30'
        #     print

    def cky_parse(self, words, grammar):

        self.cky_table = []
        for j in range(0, len(words) + 1):
            table = []
            for i in range(0, len(words) + 1):
                table.append([])
            self.cky_table.append(table)

        # self.display()
        for j in range(1, len(words) + 1):
            self.cky_table[j - 1][j] = list(set([x
                                                 for x in grammar.return_rule([words[j - 1]])]))
            for i in range(j - 1, -1, -1):
                for k in range(i, j):
                    a = self.cky_table[i][k]
                    b = self.cky_table[k][j]

                    c = [grammar.return_rule(r)[0]
                         for r in itertools.product(a, b) if grammar.return_rule(r) != []]

                    self.cky_table[i][j] = self.cky_table[i][j] + c

        self.display()

if __name__ == '__main__':
    cfg = CFG('midterm.cfg')
    cky = CKY()

    cky.cky_parse(['flies', 'like', 'arrows'], cfg)
