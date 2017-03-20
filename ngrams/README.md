# README.txt

--------------------------------------------------------PART A--------------------------------------------------------

#	PART A:

##	EXPLANATION:
The file for PART A is "ngram.py" which has two functions as told to calculate the bigrams and unigrams: 
		
		bigrams(text, corpus=False) ; unigrams(text,corpus=False)

RUN: These two functions can be run by simply running in the terminal:
		
		python ngram.py

It saves the bigrams and unigrams in files "bigram_counts.json" and "unigram_counts.json" respectively, which can be accessed in "data/"folder. The "data/" folder also stores the "corpus.txt" file which was used to generate the bigrams and unigrams.

------------------------------------------------------PARTS B, C, D------------------------------------------------------

#	PART B, C, D:

##	EXPLANATION:
The files for these parts are "sentence_parsing.py", "smoothing.py" and "probability.py".

**	The commands for all three: no smoothing, add-one smoothing and good-turing discounting print the output for all the three parts. **

The following items get printed when the command for any of the above is run:

1.	The sentences in their raw state and how they are being worked on.

2.	The no smoothing table is printed (if one of the other smoothing methods is called, if not only no smoothing table needs to be printed). The no-smoothing bigram table is followed by any of the smoothing tables (if called).

3.	The bigram probability table is printed.

4.	The probability of the two sentences is printed

##	RUN: 

NO SMOOTHING:					python sentence_parsing.py --no

ADD-ONE SMOOTHING:				python sentence_parsing.py --aos

GOOD-TURING DISCOUNTING:		python sentence_parsing.py --gtd

To run all simultaneously:

			python sentence_parsing.py --no --aos --gtd


------------------------------------------------------SPECIFIC NOTES------------------------------------------------------


**	SPECIFIC NOTES: In Good-Turing Smoothing, "N(c+1) = 0" when "c = 2". You (TA) suggested to take "0" wherever "0" occured, but a "0" here makes the probability of the sentence go to "0.0". So, I have taken the value of "log(c)" whenever "N(c+1) = 0", which is not equal to the actual initial value, and is also not very small (since, c = 2 in itself is large and needs some credit).


**	REQUIREMENTS:

1.	NLTK: The nltk library was used extensively for tokenizing the words.

The "requirements.txt" file holds the name of the item and the version as it was used on my system. You might probably already have it.

** "NLTK" is not already installed in csgrads1 **
