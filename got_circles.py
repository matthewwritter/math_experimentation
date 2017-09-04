import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# From last section of https://tinyletter.com/data-is-plural/letters/data-is-plural-2017-08-30-edition
# url = 'https://int.nyt.com/newsgraphics/2017/2017-07-17-got-matrix/mean.json'
# r = requests.get(url)
# raw_df = pd.DataFrame(r.json()).set_index('character')


# Center everybody
df = raw_df.copy()
df['moral'] = df['moral'].sub(df['moral'].mean())
df['physical'] = df['physical'].sub(df['physical'].mean())

f, axarr = plt.subplots(1,1, figsize=(5,5))
ax = axarr
assert isinstance(ax, plt.Axes)
ax.set_xlim(-1,1)
ax.set_ylim(-1,1)
ax.set_xlabel('Physical')
ax.set_ylabel('Moral')

ax.scatter(x=df.physical, y=df.moral, c='grey', linewidths=0)

i = 0
ax.scatter(x=df.iloc[0].physical, y=df.iloc[0].moral, c='green', linewidths=0)
radius = (df.iloc[i,0]**2+df.iloc[i,1]**2)**.5
xs = np.linspace(-radius,radius)
ys = (radius**2-xs**2)**.5
ys = np.concatenate([ys, -1*ys])

def draw_circle(a3, ax):
    xs = np.linspace(-a3, a3)
    ys = (a3 ** 2 - xs ** 2) ** .5

    ax.plot(xs, ys, c='grey')
    ax.plot(xs, -1*ys, c='grey')

draw_circle(radius, ax)


ax.scatter(x=df.iloc[1].physical, y=df.iloc[1].moral, c='red', linewidths=0)

b = df.iloc[:2,0].pow(2).as_matrix()
A = np.concatenate([
    df.iloc[:2,1:].pow(2).mul(-1).as_matrix(),
    np.ones([2, 1]),
],axis=1)
x = np.linalg.solve(A,b)

domain = (x[1]/x[0])**.5
xs = np.linspace(-domain,domain,300)
ys = (-x[0]*xs**2+x[1])**.5
ax.plot(xs, ys, c='grey')
ax.plot(xs, -1*ys, c='grey')
