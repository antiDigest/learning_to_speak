import nltk
import re


class CFG(object):

    def __init__(self, CFGFILE):
        self.import_cfg(CFGFILE)

    def import_cfg(self, FILE):
        if FILE.split('.')[1] != 'cfg':
            raise ValueError(
                'Not a context free grammar file. Please enter a ".cfg" file')
            return

        file = open(FILE, 'r')

        lines = file.read().split('\n')

        self.rules = {}
        for line in lines:
            if re.split(' *->[ ]*', line)[0] in self.rules.keys():
                for item in re.split(' *\|[ ]*', re.split(' *->[ ]*', line)[1]):
                    self.rules[re.split(
                        ' *->[ ]*', line)[0]].append(item)
            else:
                self.rules[re.split(' *->[ ]*', line)[0]] = re.split(' *\|[ ]*',
                                                                     re.split(' *->[ ]*', line)[1])

    def return_rule(self, tags):

        tags = list(tags)
        assert(type(tags) == list)

        tag = ' '.join(tags)
        applicable = []
        for rule in self.rules.items():
            if tag in rule[1]:
                applicable.append(rule[0])

        # print 'Checking rule', tag, 'to return', applicable
        return applicable

if __name__ == '__main__':

    cfg = CFG('main.cfg')
    print cfg.rules
    print cfg.return_rule(['Noun'])
    print cfg.return_rule(['I'])
