#!/usr/bin/env python

import os
import numpy as np
import pandas as pd
from scipy import stats

import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.ticker import MultipleLocator

mpl.rcParams['mathtext.fontset'] = 'stix'
mpl.rcParams['mathtext.fontset'] = 'stix'
mpl.rcParams['font.family'] = 'STIXGeneral'
fs = 24.

class Fit_Distr(object):
    """
    TBW.
    """    
    
    def __init__(self, df, outdir):
        self.y = df.ir_transf.values[1:] #First value is always nan.
        self.outdir = outdir

        self.fig, self.ax = plt.subplots(1,1, figsize=(10,10))
        self.xdom = None
                        
    def set_fig_frame(self):
 
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
          self.y, bins=30, normed=True, histtype='stepfilled', alpha=0.4)
        
        #Use range from plotted histogram to define domain for distributions.
        xticks = self.ax.get_xticks()
        xmin, xmax = min(xticks), max(xticks)
        #self.xdom = np.linspace(xmin, xmax, len(self.y)) 
        self.xdom = np.linspace(xmin, xmax, len(self.y)) 
        #key2distr = {'normal': stats.norm, 'gamma':stats.gamma}
        #distr_obj = key2distr[key]
    
    def describe_obs_distr(self):
        print('Mean {}'.format(np.mean(self.y))) 
        print('Standard deviation {}'.format(np.std(self.y))) 
        print('Skewness {}'.format(stats.skew(self.y))) 
        print('Kurtosis {}'.format(stats.kurtosis(self.y)))

    def fit_normal(self):
        mu, sd = stats.norm.fit(self.y)
        y_theor = stats.norm.pdf(self.xdom, mu, sd)
        self.ax.plot(
          self.xdom, y_theor, ls='-', color='b', lw=3., marker='None',
          label=r'Normal')

    def fit_beta(self):
        a, b, c, d = stats.beta.fit(self.y)
        y_theor = stats.beta.pdf(self.xdom, a, b, c, d)
        self.ax.plot(
          self.xdom, y_theor, ls='--', color='r', lw=3., marker='None',
          label=r'Beta') 

    def fit_gamma(self):
        if all(self.y>0.):
            a, b, c = stats.gamma.fit(self.y)
            y_theor = stats.gamma.pdf(self.xdom, a, b, c)
            self.ax.plot(
              self.xdom, y_theor, ls='-.', color='g', lw=3., marker='None',
              label=r'Gamma')

    def fit_eweibull(self):
        #Valid only if x>0?
        a, b, c, d = stats.exponweib.fit(self.y)
        y_theor = stats.exponweib.pdf(self.xdom, a, b, c, d)
        self.ax.plot(
          self.xdom, y_theor, ls=':', color='c', lw=3., marker='None',
          label=r'Exp Weibull')        
        #print(stats.chisquare(self.y, f_exp=y_theor))

    def fit_lognorm(self):
        if all(self.y>0.):
            a, b, c = stats.lognorm.fit(abs(self.y))
            y_theor = stats.lognorm.pdf(self.xdom, a, b, c)
            self.ax.plot(
              self.xdom, y_theor, ls=':', color='m', lw=3., marker='None',
              label=r'Log normal')   

    def make_legend(self):
        self.ax.legend(
          frameon=False, fontsize=fs, labelspacing=.1, numpoints=1, loc=2,
          handlelength=1.5)        

    def manage_output(self):
        fpath = os.path.join(self.outdir, 'Fig_distributions.pdf')
        plt.savefig(fpath, format='pdf')
        
    def run_fitting(self):
        self.set_fig_frame()
        self.plot_histogram()
        self.describe_obs_distr()
        self.fit_normal()
        self.fit_beta()
        self.fit_gamma()
        self.fit_eweibull()
        self.fit_lognorm()
        self.make_legend()
        self.manage_output()
        
        
