#!/usr/bin/env python

import sys
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.ticker import MultipleLocator

from clean_timestamps import Clean_Timestamps

mpl.rcParams['mathtext.fontset'] = 'stix'
mpl.rcParams['mathtext.fontset'] = 'stix'
mpl.rcParams['font.family'] = 'STIXGeneral'
fs = 28. #Default font size for plots.

class Plot_Heart(object):
    """
    Description:
    ------------
    This code investigates the data given as part of a Lantern assignment.
    In particular, the heart rate and sleep data.

    Parameters:
    -----------
    show_fig ~ bool
        Flag to determine whether or not to display the figure.
    save_fig ~ bool
        Flag to determine whether or not to save the figure.    

    Outputs:
    --------
    ./../OUTPUTS/analyses/Fig_heart_sleep.pdf
    
    """        
    def __init__(self, show_fig, save_fig):
        self.show_fig = show_fig
        self.save_fig = save_fig

        #Initialize figure and its axes.
        self.fig = plt.figure(figsize=(8,10))
        self.ax1 = self.fig.add_subplot(211)
        self.ax2 = self.fig.add_subplot(212)
        
        #Initialize master dictionary that will contain the data. Impose type.
        self._M = {}
        
        #Record a reference time.
        self.time_ref = None

        #Get the path to the top directory.
        self.top_dir = os.path.abspath(
          os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
                
        #Call all functions below to produce the figure.
        self.make_plot()
        
    def set_fig_frame(self):
    
        xlabel = r'Time'
        ylabel = r'Heart Rate [bpm]'
        self.ax1.set_xlabel(xlabel, fontsize=fs)
        self.ax1.set_ylabel(ylabel, fontsize=fs)
        self.ax1.set_xlim(0., 700.)
        self.ax1.set_ylim(25., 175.)
        self.ax1.tick_params(axis='y', which='major', labelsize=fs, pad=8)      
        self.ax1.tick_params(axis='x', which='major', labelsize=fs, pad=8)
        self.ax1.tick_params('both', length=12, width=2., which='major',
                             direction='in', right=True, top=True)
        self.ax1.tick_params('both', length=6, width=2., which='minor',
                             direction='in', right=True, top=True) 
        self.ax1.xaxis.set_minor_locator(MultipleLocator(20.))
        self.ax1.xaxis.set_major_locator(MultipleLocator(100.))
        self.ax1.yaxis.set_minor_locator(MultipleLocator(25.))
        self.ax1.yaxis.set_major_locator(MultipleLocator(50.))

        xlabel = r'Duration'
        ylabel = r'Heart Rate [bpm]'
        self.ax2.set_xlabel(xlabel, fontsize=fs)
        self.ax2.set_ylabel(ylabel, fontsize=fs)
        #self.ax2.set_xlim(1.e9, 1.e12)
        self.ax1.set_ylim(25., 175.)
        self.ax2.tick_params(axis='y', which='major', labelsize=fs, pad=8)      
        self.ax2.tick_params(axis='x', which='major', labelsize=fs, pad=8)
        self.ax2.tick_params('both', length=12, width=2., which='major',
                             direction='in', right=True, top=True)
        self.ax2.tick_params('both', length=6, width=2., which='minor',
                             direction='in', right=True, top=True) 
        #self.ax2.xaxis.set_minor_locator(MultipleLocator(20.))
        #self.ax2.xaxis.set_major_locator(MultipleLocator(100.))
        self.ax2.yaxis.set_minor_locator(MultipleLocator(25.))
        self.ax2.yaxis.set_major_locator(MultipleLocator(50.))

    def retrieve_data(self):
        #Read heart data.
        fpath = os.path.join(self.top_dir + '/data/heart_rate.csv')
        self.M = pd.read_csv(fpath, header=0, index_col=0, low_memory=False)
        #print(self.M)

    def preprocess_data(self):
        #Treat nan is data and use standard notation for the time stamps.
        
        #Only a few irrelevant columns contain nan. Drop these columns.
        drop_cols = self.M.columns[self.M.isna().any()].tolist()
        #print(drop_cols)
        self.M.drop(drop_cols, axis=1, inplace=True)
               
        start_t = self.M['start_time'].values
        start_obj = Clean_Timestamps(start_t, t_format='%Y-%m-%d %H:%M:%S.%f')
        
        #By inspecting the relative times, one sees that the earlist times
        #are spurious. The were also used as a reference to compute time
        #lapses. Remove these entries (rows) and re-compute time lapses.
        #print(start_obj.get_relative_time())
        #print(start_obj.t_ref_idx)
        self.M.drop(start_obj.t_ref_idx, inplace=True)
        del(start_obj)
        
        start_t = self.M['start_time'].values
        start_obj = Clean_Timestamps(start_t, t_format='%Y-%m-%d %H:%M:%S.%f')
        self.time_ref = start_obj.dt_ref #Assign reference time.
        
        #Data note: the column 'end_time' is identical to 'start_time' and
        #the columns 'update_time' and 'create_time' are also identical.
        #Using 'update_time' for end_time. Actual meaning is not clear.
        end_t = self.M['update_time'].values
        end_obj = Clean_Timestamps(
          end_t, t_format='%Y-%m-%d %H:%M:%S.%f', dt_ref=self.time_ref)

        #Update dataframe with relative start, end and duration times (days).
        self.M['start_time_rel'] = start_obj.get_relative_time()
        self.M['end_time_rel'] = end_obj.get_relative_time()
        self.M['duration'] = self.M['end_time_rel'] - self.M['start_time_rel']
        self.M['duration'] = self.M['duration']*24*60. #Convert days to min.

        #get standard edviation for duration time and remove spurious values.
        duration_std = np.std(self.M['duration'].values)
        self.M.drop(
          self.M[self.M['duration'] > 5.*duration_std].index, inplace=True)

        #Sort dataframe according to starting_time.
        self.M.sort_values(by ='start_time_rel', inplace=True)
        
    def plot_quantities(self):
        self.ax1.plot(
          self.M['start_time_rel'], self.M['heart_rate'], ls='None', marker='s',
          markersize=8., color='k')

        self.ax2.plot(
          self.M['duration'], self.M['heart_rate'], ls='None', marker='o',
          markersize=8., color='k')

    def manage_output(self):
        plt.tight_layout()
        if self.save_fig:
            fpath = './../OUTPUTS/analyses/Fig_heart_sleep.pdf'
            plt.savefig(fpath, format='pdf')
        if self.show_fig:
            plt.show()
        plt.close(self.fig)    

    def make_plot(self):
        self.set_fig_frame()
        self.retrieve_data()
        self.preprocess_data()
        self.plot_quantities()
        self.manage_output()             

    #Decorators.
    @property
    def M(self):
        return self._M
    
    @M.setter
    def M(self, value):
        if not (isinstance(value, dict) or isinstance(value, pd.DataFrame)):
            raise ValueError('The variable M must always be a dictionary.')
        self._M = value

if __name__ == '__main__':
    Plot_Heart(show_fig=False, save_fig=True)

