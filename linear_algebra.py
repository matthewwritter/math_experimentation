import requests
import pandas as pd
import matplotlib.pyplot as plt


# From last section of https://tinyletter.com/data-is-plural/letters/data-is-plural-2017-08-30-edition
# url = 'https://int.nyt.com/newsgraphics/2017/2017-07-17-got-matrix/mean.json'
# r = requests.get(url)
raw_df = pd.DataFrame(r.json()).set_index('character')


# Center everybody
df = raw_df.copy()
df['moral'] = df['moral'].sub(df['moral'].mean())
df['physical'] = df['physical'].sub(df['physical'].mean())
plt.scatter(x=df.physical, y=df.moral)

# Get the first character's vector
# Figure out the rotation to the second character
#  Ax = b
#  A<first> = <second>
# Apply that rotation to the third character, and see what other character that's near
# Draw it
# For each pair, find rotation, then apply to every other character and find distance