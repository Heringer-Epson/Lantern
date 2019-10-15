import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from itertools import cycle

#%matplotlib inline

angles = cycle([1./3.*np.pi, -2./3.*np.pi, 1./3.*np.pi])

def koch_line(A,l,theta):
    """Given a line segment that starts at A and ends at B,
    return 3 points that define an equilateral triangle whose
    base intersects the segment symmetrically. The length l
    is passed as a parameter to avoid repeating the same calculation.
    """
    new_l = l/3.
    angle_out = []
    
    def update_seg(v,theta):
        angle_out.append(theta)
        return v + np.array([new_l*np.cos(theta), new_l*np.sin(theta)])
    
    c1 = update_seg(A,theta)
    theta += next(angles)        
    c2 = update_seg(c1,theta)
    theta += next(angles)  
    c3 = update_seg(c2,theta)
    theta += next(angles)  
    c4 = update_seg(c3,theta)
    
    return [A,c1,c2,c3], angle_out, [new_l, new_l, new_l, new_l]

def make_triangle_shape(x):
    """Compute the vertice positions of a equilateral triangle
    of length x, with a vertice a (0,0).
    """
    side_len = x/3.
    v1 = np.array([0.,0.])
    v2 = np.array([side_len*np.cos(np.pi/3.),side_len*np.sin(np.pi/3.)])
    v3 = np.array([side_len,0.])
    angles = [np.pi/3., -np.pi/3., -np.pi]
    lengths = [side_len, side_len, side_len]
    return [v1,v2,v3,v1], angles, lengths

def make_P_shape(x):
    """Compute the vertice positions of a equilateral triangle
    of length x, with a vertice a (0,0).
    """
    v1 = np.array([0.,0.])
    v2 = np.array([0.,2.*x/5.])
    v3 = np.array([x/5.,2.*x/5.])
    v4 = np.array([x/5.,x/5.])
    v5 = np.array([0.,x/5.])
    angles = [np.pi/2., 0.,-np.pi/2. , -np.pi]
    lengths = [2.*x/5.,x/5.,x/5.,x/5.]
    return list([v1,v2,v3,v4,v5]), angles, lengths

def koch_figure(x):
    
    out, angles, lengths = {}, {}, {}
    #out['0'], angles['0'], lengths['0'] = make_triangle_shape(x)
    out['0'], angles['0'], lengths['0'] = make_P_shape(x)
    for i in range(1,6):
        out[str(i)] = []
        angles[str(i)] = []
        lengths[str(i)] = []
        for v, v_next, theta, l in zip(
          out[str(i-1)], out[str(i-1)][1:], angles[str(i-1)],
          lengths[str(i-1)]):
            seg, ang, leng = koch_line(v,l,theta)
            out[str(i)] += seg
            angles[str(i)] += ang
            lengths[str(i)] += leng
        out[str(i)].append(out[str(i-1)][0])
    return out
        
def make_figure(results):
    fig = plt.figure()
    for i in range(6):
        ax = fig.add_subplot(2,3,i+1)
        ax.set_xticklabels([])
        ax.set_yticklabels([])
        ax.tick_params(axis='both', which='both', bottom=False, left=False)
        data = np.transpose(results[str(i)])
        ax.plot(data[0], data[1], lw=1, c='k')
    plt.subplots_adjust(wspace=0., hspace=0.)
    plt.savefig('fig.png', format='png')

results = koch_figure(3.)
make_figure(results)
