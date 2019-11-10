#!/usr/bin/env python

import os
import math
import numpy as np
import pandas as pd
from scipy import stats
from itertools import cycle
import scipy.stats

import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.ticker import MultipleLocator

mpl.rcParams['mathtext.fontset'] = 'stix'
mpl.rcParams['mathtext.fontset'] = 'stix'
mpl.rcParams['font.family'] = 'STIXGeneral'
fs = 24.
c = cycle(['#e41a1c','#377eb8','#4daf4a','#984ea3','#ff7f00','#ffff33',
           '#a65628','#f781bf'])
ls = cycle(['-', '-.', '--', ':'])

class Fit_Distr(object):
    """
    TBW.
    """    
    
    def __init__(self, M, tenor, incr, outdir):
        self.M = M
        self.tenor = tenor
        self.incr = incr
        self.outdir = outdir

        self.fig = None
        self.ax = None
        self.xdom = None
        self.y = None

    def get_plotting_values(self, key):
        self.y = self.M[key]['ir_transf_mean'].values
                        
    def set_fig_frame(self):

        self.fig, self.ax = plt.subplots(1,1, figsize=(10,10))
 
        self.ax.tick_params(axis='y', which='major', labelsize=fs, pad=8)      
        self.ax.tick_params(axis='x', which='major', labelsize=fs, pad=8)
        self.ax.tick_params('both', length=12, width=2., which='major',
                             direction='in', right=True, top=True)
        self.ax.tick_params('both', length=6, width=2., which='minor',
                             direction='in', right=True, top=True) 
        
        #self.ax.yaxis.set_minor_locator(MultipleLocator(.1))
        #self.ax.yaxis.set_major_locator(MultipleLocator(.5))
        self.ax.set_ylabel(r'Normalized Count', fontsize=fs)
        self.ax.set_xlabel(r'Transformed IR', fontsize=fs)

    def plot_histogram(self):
        aux = self.ax.hist(
          self.y, bins=40, normed=True, histtype='stepfilled', alpha=0.7,
          color='grey')
        
        #Use range from plotted histogram to define domain for distributions.
        xticks = self.ax.get_xticks()
        xmin, xmax = min(xticks), max(xticks)
        self.xdom = np.linspace(xmin, xmax, len(self.y)) 
    
    def describe_obs_distr(self):
        print('Mean {}'.format(np.mean(self.y))) 
        print('Standard deviation {}'.format(np.std(self.y))) 
        print('Skewness {}'.format(stats.skew(self.y))) 
        print('Kurtosis {}'.format(stats.kurtosis(self.y)))

    def make_fits(self):
        #Based on example from:
        #http://www.aizac.info/simple-check-of-a-sample-against-80-distributions/
        pdfs = ['norm', 'exponweib', 'beta']
        if all(self.y > 0.):
            pdfs += ['gamma', 'lognorm']
        
        for pdf in pdfs:
            
            #Fit distribution and get most likely parameters.
            pars = eval('scipy.stats.' + pdf + '.fit(self.y)')
            
            if not any([math.isnan(p) for p in pars]):
                arg = ', '.join([str(val) for val in pars])
                y_theor = eval(
                  'scipy.stats.' + pdf + '.pdf(self.xdom, '+ arg + ')')
     
                #Compute and print goodness of fit KS test.
                D, p = scipy.stats.kstest(self.y, pdf, args=pars)
                print(pdf.ljust(18) + ('D: {}'.format(D).ljust(30))
                      + ('p: {}'.format(p).ljust(45)))

                #For reasonable distributions, add curve to plot.
                if D < 0.2:
                    self.ax.plot(
                      self.xdom, y_theor, ls=next(ls), color=next(c), lw=3.,
                      label=pdf + ': p={:.3f}'.format(p))

    def make_legend(self):
        self.ax.legend(
          frameon=False, fontsize=fs, labelspacing=.1, numpoints=1, loc=2,
          handlelength=1.5)        

    def manage_output(self, key):
        fname = 'distributions/Fig_distr_{}.pdf'.format(key)
        plt.savefig(os.path.join(self.outdir, fname), format='pdf')
        
    def run_fitting(self):
        for tenor in self.tenor:
            for incr in self.incr:
                key = '{}m_{}d'.format(str(tenor), str(incr))                
                self.get_plotting_values(key)
                self.set_fig_frame()
                self.plot_histogram()
                self.describe_obs_distr()
                self.make_fits()
                self.make_legend()
                self.manage_output(key)
                plt.close()
            
        
