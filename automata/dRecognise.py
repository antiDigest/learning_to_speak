import nltk


def dRecognise(tape, transition):
    index = 0
    current = state[0]
    while tape[index] != '$':
        if transition[current][tape[index]] == '0':
            return 'reject'
        else:
            current = transition[current, tape[index]]
            index += 1

    if current == 'A':
        return 'accept'
    return 'reject'


if __name__ == '__main__':

    automata = {}

    with open('main.automata') as f:
        lines = f.read().split('\n')
        for line in lines:

            if not line.split()[0] == 'S':
                automata[line.split()[0]] = {}
                for i, cell in enumerate(line.split()[1:]):
                    automata[line.split()[0]][inputs[i + 1]
                                              ] = line.split()[i + 1]
            else:
                inputs = line.split()[1:]

        print automata
