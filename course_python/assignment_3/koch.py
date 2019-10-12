import sys
import os
import time
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.ticker import MultipleLocator
from collections import Counter
%matplotlib inline

#Set matplotlib variables for prettier plots.
mpl.rcParams['mathtext.fontset'] = 'stix'
mpl.rcParams['mathtext.fontset'] = 'stix'
mpl.rcParams['font.family'] = 'STIXGeneral'
fs = 36.

#https://stackoverflow.com/questions/2827393/angles-between-two-n-dimensional-vectors-in-python
def unit_vector(vector):
    """ Returns the unit vector of the vector.  """
    return vector / np.linalg.norm(vector)

def angle_between(v1, v2):
    """ Returns the angle in radians between vectors 'v1' and 'v2'::

            >>> angle_between((1, 0, 0), (0, 1, 0))
            1.5707963267948966
            >>> angle_between((1, 0, 0), (1, 0, 0))
            0.0
            >>> angle_between((1, 0, 0), (-1, 0, 0))
            3.141592653589793
    """
    v1_u = unit_vector(v1)
    v2_u = unit_vector(v2)
    return np.arccos(np.clip(np.dot(v1_u, v2_u), -1.0, 1.0))

import math
 
def getAngle(a, b, c):
    ang = math.degrees(math.atan2(c[1]-b[1], c[0]-b[0]) - math.atan2(a[1]-b[1], a[0]-b[0]))
    return ang + 360 if ang < 0 else ang

from itertools import cycle
colors = ['k', 'b', 'g']
theta = 1./3.*np.pi
angles = cycle([1./3.*np.pi, -2./3.*np.pi, 1./3.*np.pi, ])

plt.xlim(-1.,1.5)
plt.ylim(-1.,1.5)

def koch_line(A,B,l, theta):
    """Given a line segment that starts at A and ends at B,
    return 3 points that define an equilateral triangle whose
    base intersects the segment symmetrically. The length l
    is passed as a parameter to avoid repeating the same calculation.
    """
    
    #theta = getAngle(np.array([A[0]+1.e5,0.]),A,B) * np.pi / 180.
    new_l = l/3.
    angle_out = []
    
    angle_out.append(theta)
    c1 = A + np.array([new_l*np.cos(theta), new_l*np.sin(theta)])
    theta += next(angles)
    
    angle_out.append(theta)
    c2 = c1 + np.array([new_l*np.cos(theta), new_l*np.sin(theta)])
    theta += next(angles)
    
    angle_out.append(theta)
    c3 = c2 + np.array([new_l*np.cos(theta), new_l*np.sin(theta)])
    theta += next(angles)

    angle_out.append(theta)
    c4 = c3 + np.array([new_l*np.cos(theta), new_l*np.sin(theta)])
    
    return [A,c1,c2,c3,c4], angle_out

def make_initial_shape(x):
    """Compute the vertice positions of a equilateral triangle
    of length x, with a vertice a (0,0).
    """
    side_len = x/3.
    v1 = np.array([0.,0.])
    v2 = np.array([side_len*np.cos(np.pi/3.),side_len*np.sin(np.pi/3.)])
    v3 = np.array([side_len,0.])
    angles = [np.pi/3., -np.pi/3., -np.pi]
    return [v1,v2,v3,v1], angles

def koch_figure(x):
    
    out = {}
    angles = {}
    out['0'], angles['0'] = np.asarray((make_initial_shape(x)))
    for i in range(1,3):
        out[str(i)] = []
        angles[str(i)] = []
        vertices = out[str(i-1)]
        l = x/(3.**i)
        for v, v_next, theta in zip(vertices, vertices[1:], angles[str(i-1)]):
            seg, ang = koch_line(v, v_next,l, theta)
            out[str(i)] += seg
            angles[str(i)] += ang
        out[str(i)] = np.asarray(out[str(i)])
    return out
        
results = koch_figure(3.)
data = np.transpose(results['0'])
plt.plot(data[0], data[1], c='k')

for i in range(1,3):
    #data = np.transpose(results[str(i)][0:3])
    data = np.transpose(results[str(i)])
    #plt.plot(data[0], data[1], marker='s', lw=3-float(i), c=colors[i])
    plt.plot(data[0], data[1], marker='s', lw=3-float(i), c=colors[i])




#plt.plot(out[0], out[1], ls='-', marker='s')

#Test
#data = np.asarray(koch_line(np.array([0.,0.]), np.array([-1.,0.]),1.)).transpose()
#plt.plot(data[0], data[1], marker='s', lw=float(i), c=colors[i])
