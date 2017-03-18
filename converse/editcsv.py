import pandas as pd
import re

f = pd.read_csv('data/movie_lines.txt',
                sep=r' \+\+\+\$\+\+\+ ', engine="python")

print f

df = f[['line']]

df.to_csv('data/text.txt', index=False)
