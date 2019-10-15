#!/usr/bin/env python

import sys
import os
import pickle
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

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
    ./../OUTPUTS/analyses/X.pdf
    
    """        
    def __init__(self, show_fig, save_fig):
        self.show_fig = show_fig
        self.save_fig = save_fig
        
        #Get the path to the top directory.
        self.top_dir = os.path.abspath(
          os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))

        self._M = {}
                
        #Call all functions below to produce the figure.
        self.make_plot()
        
    def retrieve_data(self):
        #Read heart data.
        fpath = os.path.join(self.top_dir + '/OUTPUTS/master_data.pkl')
        with open(fpath, 'rb') as f:
            self.M = pickle.load(f)

    def test_plot(self):
        print(self.M['heartrate'].columns)
        sns.lmplot(x='duration', y='heart_rate', data=self.M['heartrate'])
        plt.show()

    def make_plot(self):
        self.retrieve_data()
        self.test_plot()
        #self.manage_output()             

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

