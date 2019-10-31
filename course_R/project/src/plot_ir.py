#!/usr/bin/env python

import numpy as np
import pandas as pd
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.ticker import MultipleLocator


mpl.rcParams['mathtext.fontset'] = 'stix'
mpl.rcParams['mathtext.fontset'] = 'stix'
mpl.rcParams['font.family'] = 'STIXGeneral'
fs = 36.
c = ['#fdae61', '#3288bd']

class Plot_Ir(object):
    """
    Description:
    ------------
    TBW.

    Parameters:
    -----------
    show_fig : ~bool
        True of False. Whether to show or not the produced figure.
    save_fig : ~bool
        True of False. Whether to save or not the produced figure.

    Outputs:
    --------
    ./../OUTPUTS/RUNS/Fig_IR.pdf
    """        
    def __init__(self, df):
        self.df = df

        self.fig, self.ax = plt.subplots(
          2,2, gridspec_kw = {'height_ratios':[1, 1], 'width_ratios':[3, 1]},
          figsize=(12,8))
                        
    def set_fig_frame(self):
 
        plt.subplots_adjust(
          left=.12, right=.95, bottom=.15, top=0.92, wspace=.05, hspace=.1)
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
        self.ax[1,0].xaxis.set_major_locator(mdates.MonthLocator(interval=6))
        #self.ax[1,0].yaxis.set_minor_locator()
        #self.ax[1,0].yaxis.set_major_locator()
        
        self.ax[0,0].set_ylabel(r'IR', fontsize=fs)
        self.ax[1,0].set_xlabel(r'Date', fontsize=fs)
        self.ax[1,0].set_ylabel(r'Transformed IR', fontsize=fs)
   
    def plot_quantities(self):
        
        self.ax[0,0].plot(
          self.df.date, self.df.ir, ls='-', lw=2., marker='None', color='k')
        self.ax[1,0].plot(
          self.df.date, self.df.ir_transf, ls='-', lw=2., marker='None', color='k')
                  
        '''
        #Remove objects outside shown range.
        Dcolor = self.df['Dcolor_gr'].values
        r_abs = self.df['abs_r'].values
        hosts = self.df['is_host'].values
        r_err = self.df['petroMagErr_g'].values
        Dcolor_err = np.sqrt(self.df['petroMagErr_g'].values**2.
                             + self.df['petroMagErr_r'].values**2.)

        #Draw CMD (on self.ax).
        self.ax.plot(Dcolor, r_abs, ls='None', marker='o', markersize=2.,
                     markeredgecolor=c[0], color=c[0], zorder=1.)

        self.ax.errorbar(
          Dcolor[hosts], r_abs[hosts], xerr=r_err[hosts], capsize=0.,
          elinewidth=3., markeredgecolor=c[1], zorder=2., ls='None',
          marker='*', markersize=16., color=c[1])      
        
        #Draw histogram (on self.axx).
        xbins = np.arange(x_range[0], x_range[1] + 1.e-5, 0.01)
        Dcolor_hosts = np.repeat(Dcolor[hosts], 100)
        
        self.axx.hist(Dcolor, bins=xbins, align='mid', color=c[0])
        self.axx.hist(Dcolor_hosts, bins=xbins, align='mid', color=c[1])

        #Draw histogram (on self.axy).
        ybins = np.arange(y_range[0], y_range[1] + 1.e-5, 0.1)
        r_abs_hosts = np.repeat(r_abs[hosts], 100)

        self.axy.hist(
          r_abs, bins=ybins, align='mid', color=c[0],orientation='horizontal')
        self.axy.hist(
          r_abs_hosts, bins=ybins, align='mid', color=c[1],
          orientation='horizontal')
        '''

    def make_legend(self):
        self.axx.plot(
          [np.nan], [np.nan], ls='-', marker='None', lw=15., color=c[0],
          label=r'Control Galaxies')
        self.axx.plot(
          [np.nan], [np.nan], ls='-', marker='None', lw=15., color=c[1],
          label=r'Hosts $(\times\, 100)$')
        self.axx.legend(
          frameon=False, fontsize=fs, labelspacing=.1, numpoints=1, loc=2,
          handlelength=1.5, bbox_to_anchor=(0.,1.1))

    def manage_output(self):
        #self.fig.autofmt_xdate()
        fpath = './../OUTPUTS/Fig_IR.pdf'
        plt.savefig(fpath, format='pdf')

        plt.close(self.fig)    

    def make_plot(self):
        self.set_fig_frame()
        self.plot_quantities()
        #self.make_legend()
        self.manage_output()             

