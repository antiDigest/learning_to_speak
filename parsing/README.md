
Table

For: The large can can hold the water

Given CFG:
S → NP VP         the: ART
NP → ART ADJ N    large:ADJ
NP → ART N        can:N, AUX, V
VP → AUX VP       hold: N,V
VP → V NP         water:N, V

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
