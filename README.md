# Natural Language Processing

This repository is an attempt to implement all algorithms in the Speech and Language Processing, Second Edition book.

### Dependencies

The

```
installations.txt
```

files contains all the libraries needed for this.

Other than this, you will need to download WordNet and word_tokenize modules using

```
import nltk
nltk.download()
```

in a python shell in your terminal.


### How to Run ?

The simplest method right now to access each algorithm is to go to each of the folders, if there is a

```
run.py
```

file in the folder, you will be able to run it with simply

```
python run.py <arguments>
```

you can access what arguments each of those run files takes using the 

```
python run.py -h
```

option for argparse help.


## Done:

#### Simplified Lesk Algorithm

This algorithm finds the sense of the word by matching context with wordnet definitions and examples to identify a best sense.

#### Quora Question Pairs

Attempted to solve the [Quora Question Pairs](https://www.kaggle.com/c/quora-question-pairs) competition as part of the class project, so implemented three different basic methods to identify.

1. **Adapted Lesk Algorithm**: The Lesk algorithm was a good way to identify which words were being used in what sense and the output of the Lesk algorithm gave a semantic understanding of the sentence. When comparing two sentences, this understanding was used and a similarity score was generated based on the similarity of words in the two sentences.

2. **Cosine Similarity using TFIDF**: TFIDF is one of the basic methods to convert sentences to vectors. This is mostly used for numerical representation of words and so seemed a great method to vectorize and identify the similarity between the two sentences.

3. **LSTM using Doc2Vec**: Best implementation of the three. Actually this did not require a lot of implementation, just assembling of some methods and training the LSTM for hours over Doc2Vec input and class output.

#### Context Free Grammar Parser

CFG Parser loads the grammar and tags the sentences using the CFG. The program runs in O(n^2) and is a dynamic program as explained in the Speech and Language Processing book.

#### Probability Context Free Grammar Parser

This is an extension of the CFG parser where it selects only the most probable tagging of the text.


## TODO

*	Automata - NDRecognise

*	Automata - DRecognise

*	Conversational Bot (LSTM)

* Brill Tagger
