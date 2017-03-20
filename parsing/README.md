
Table

For: The large can can hold the water

Given CFG:
S -> NP VP
NP -> ART ADJ N
NP -> ART N
VP -> AUX VP
VP -> V NP
ART -> the
ADJ -> large
N -> can
AUX -> can
V -> can
N -> hold
V -> hold
N -> water
V -> water

(This was converted to CNF CFG before entering)

X|X|X|X|X|X|X|X
:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:
-|['ART']|['X']|['NP']|-|-|-|['S']|
-|-|['ADJ']|-|-|-|-|-|
-|-|-|['AUX', 'N', 'V']|-|-|-|['VP']|
-|-|-|-|['AUX', 'N', 'V']|-|-|['VP']|
-|-|-|-|-|['N', 'V']|-|['VP']|
-|-|-|-|-|-|['ART']|['NP']|
-|-|-|-|-|-|-|['N', 'V']|
-|-|-|-|-|-|-|-
