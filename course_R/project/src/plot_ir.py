#!/usr/bin/env python

import os
import numpy as np
import pandas as pd
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.ticker import MultipleLocator

mpl.rcParams['mathtext.fontset'] = 'stix'
mpl.rcParams['mathtext.fontset'] = 'stix'
mpl.rcParams['font.family'] = 'STIXGeneral'
fs = 24.

applic2label = {'simple_diff':r'$\Delta(\mathrm{IR})_{\mathrm{1~day}}$',
                'log_ratio': r'$\mathrm{log}\ (R_{i+1}/R_i)$'}

class Plot_Ir(object):
    """
    Description:
    ------------
    TBW.

    Parameters:
    -----------
    TBW.

    Outputs:
    --------
    ./../OUTPUTS/RUNS/Fig_IR.pdf
    """        
    def __init__(self, df, application, outdir):
        self.df = df
        self.application = application
        self.outdir = outdir

        self.fig, self.ax = plt.subplots(
          2,2, gridspec_kw = {'height_ratios':[1, 1], 'width_ratios':[3, 1]},
          figsize=(12,8))
                        
    def set_fig_frame(self):
 
        plt.subplots_adjust(
          left=.12, right=.97, bottom=0., top=0.92, wspace=.02, hspace=.05)
        axes = [self.ax[0,0], self.ax[1,0], self.ax[0,1], self.ax[1,1]]
 
        for ax in axes:
            ax.tick_params(axis='y', which='major', labelsize=fs, pad=8)      
            ax.tick_params(axis='x', which='major', labelsize=fs, pad=8)
            ax.tick_params('both', length=12, width=2., which='major',
                                 direction='in', right=True, top=True)
            ax.tick_params('both', length=6, width=2., which='minor',
                                 direction='in', right=True, top=True) 
        
        self.ax[0,0].tick_params(labelbottom=False) 
        self.ax[0,1].tick_params(labelbottom=False, labelleft=False) 
        self.ax[1,1].tick_params(labelbottom=False, labelleft=False) 
        self.ax[0,0].yaxis.set_minor_locator(MultipleLocator(.1))
        self.ax[0,0].yaxis.set_major_locator(MultipleLocator(.5))
        self.ax[1,0].xaxis.set_minor_locator(mdates.MonthLocator(interval=1))
        self.ax[0,0].set_ylabel(r'IR', fontsize=fs)
        self.ax[1,0].set_xlabel(r'Date', fontsize=fs)
        self.ax[1,0].set_ylabel(applic2label[self.application], fontsize=fs)
   
    def plot_quantities(self):
        
        self.ax[0,0].plot(
          self.df.date, self.df.ir, ls='-', lw=2., marker='None', color='k')
        self.ax[1,0].plot(
          self.df.date, self.df.ir_transf, ls='-', lw=2., marker='None', color='k')

    def plot_histograms(self):
        nbins = 15
        self.ax[0,1].set_ylim(self.ax[0,0].get_ylim())
        self.ax[0,1].hist(
          self.df.ir.values, bins=nbins, align='mid', color='grey',
          orientation='horizontal')

        self.ax[1,1].set_ylim(self.ax[1,0].get_ylim())
        self.ax[1,1].hist(
          self.df.ir_transf.values, bins=nbins, align='mid', color='grey',
          orientation='horizontal')

    def manage_output(self):
        self.fig.autofmt_xdate()
        fpath = os.path.join(self.outdir, 'Fig_IR.pdf')
        plt.savefig(fpath, format='pdf')

        plt.close(self.fig)    

    def make_plot(self):
        self.set_fig_frame()
        self.plot_quantities()
        self.plot_histograms()
        self.manage_output()             

