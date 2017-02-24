// ReadMe.txt

----------------------------------------------------------------GIVEN------------------------------------------------------------

The files in the folder "data" are:

1. "observations.csv" : This file contains the observations as shown in the tables of the figure.

2. "hmm.csv" : This file contains the hidden markov model as shown in the figure.


--------------------------------------------------------------HOW TO RUN---------------------------------------------------------

The "run.py" files handle all the running of the program. To run the viterbi algorithm for the output as suggested in the homework:

			"python run.py --seq <sequence of digits>"

"<sequence of digits>" -> This should be just numbers without any quotes.

Example: To run the example as given in the homework:

			"python run.py --seq 331122313"

----------------------------------------------------------------EXTRAS-----------------------------------------------------------

No extra python high level modules have been used in this. Only modules used are "sys" to print output in one line and "argparse" to parse the arguments provided on the command line.

---------------------------------------------------------------------------------------------------------------------------------