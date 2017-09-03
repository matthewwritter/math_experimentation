#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 10:15:30 2017

@author: mritter
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.array([1,2])
b = np.array([5,3])


f, axarr = plt.subplots(1,2, figsize=(10,5))

ax = axarr[0]
ax.set_xlim(0,10)
ax.set_ylim(0,10)
ax.scatter(x[0],x[1], c='green')
ax.scatter(b[0],b[1], c='red')
ax.plot([1,1],[0,2], color='black', linestyle='-')
ax.plot([0,1],[2,2], color='black', linestyle='-')

ax.plot([1,1],[0,3], color='grey', linestyle='--')
ax.plot([0,1],[3,3], color='grey', linestyle='--')

ax.plot([0,4],[0,3], color='black', linestyle='--')
ax.plot([1,5],[0,3], color='black', linestyle='--')
ax.plot([4,5],[3,3], color='black', linestyle='--')
#ax.plot([3.5,5],[3,3], color='black', linestyle='--')

ax = axarr[1]
ax.set_xlim(0,10)
ax.set_ylim(0,10)
ax.scatter(x[0],x[1], c='green')
ax.scatter(b[0],b[1], c='red')
ax.plot([1,1],[0,2], color='black', linestyle='-')
ax.plot([0,1],[2,2], color='black', linestyle='-')

ax.plot([5,5],[0,2], color='grey', linestyle='--')
ax.plot([0,5],[2,2], color='grey', linestyle='--')

ax.plot([0,5],[2,3], color='black', linestyle='--')
ax.plot([0,5],[0,1], color='black', linestyle='--')
ax.plot([5,5],[1,3], color='black', linestyle='--')
ax.set_title("Two of the infinite number of ways one vector"
             "\ncan be transformed into another")

print("""There are two things the matrix can do, stretch and skew. 
      This is what a pure stretch in each direction looks like, followed by
      the necessary skew, but anything in between is also possible""")