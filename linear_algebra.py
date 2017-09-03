import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# From last section of https://tinyletter.com/data-is-plural/letters/data-is-plural-2017-08-30-edition
# url = 'https://int.nyt.com/newsgraphics/2017/2017-07-17-got-matrix/mean.json'
# r = requests.get(url)
raw_df = pd.DataFrame(r.json()).set_index('character')


# Center everybody
df = raw_df.copy()
df['moral'] = df['moral'].sub(df['moral'].mean())
df['physical'] = df['physical'].sub(df['physical'].mean())

# Get the each character's vector
for ix in df.index:
    df.loc[ix,'angle'] = np.arctan(df.loc[ix,'physical'] / df.loc[ix,'moral'])
    df.loc[ix, 'ortho_angle'] = df.loc[ix,'angle'] + np.pi/2.


# Draw it for char1
f, axarr = plt.subplots(1,1, figsize=(5,5))
ax = axarr
assert isinstance(ax, plt.Axes)
ax.set_xlim(-1,1)
ax.set_ylim(-1,1)
ax.set_xlabel('Physical')
ax.set_ylabel('Moral')

ax.scatter(x=df.physical, y=df.moral, c='grey', linewidths=0)

for ix in df.index:
    angle = df.loc[ix, 'angle']
    ortho_angle = df.loc[ix, 'ortho_angle']
    ax.plot([0, df.loc[ix, 'physical']], [0,df.loc[ix, 'moral']], linestyle='-', color='k')
    ax.plot([-np.sin(ortho_angle), np.sin(ortho_angle)], [-np.cos(ortho_angle),np.cos(ortho_angle)], linestyle='--', color='k')

    ix2 = df.loc[:, 'angle'].sub(df.loc[ix, 'ortho_angle']).apply(lambda x: x // 2*np.pi).idxmin()
    ax.scatter(df.loc[ix, 'physical'], df.loc[ix, 'moral'], c='blue', linewidths=0)
    ax.scatter(df.loc[ix2, 'physical'], df.loc[ix2, 'moral'], c='red', linewidths=0)

    print("{} is perpendicular to {}".format(ix,ix2))
    break