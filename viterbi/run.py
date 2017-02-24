
# Importing Libraries
import argparse

# Importing Classes
from viterbi import Viterbi

if __name__ == '__main__':

    sequence = ''

    # Checking arguments
    parser = argparse.ArgumentParser(description='Output Viterbi Sequence.')
    parser.add_argument('sequence', metavar='N', type=str, nargs='+',
                        help='an integer for the sequence')
    parser.add_argument('-s', '--sequence', action='store_const',
                        dest='sequence',
                        const=sequence,
                        default=None,
                        help='A sequence of numbers for the output sequence :: Required for any output.')
    args = parser.parse_args()

    sequence = args.sequence[0]

    # If sequence not provided, return help and exit
    if not sequence:
        parser.print_help()
        exit()

    print 'Observation(Input Sequence):', sequence

    element = Viterbi(sequence)
    element.viterbi()
