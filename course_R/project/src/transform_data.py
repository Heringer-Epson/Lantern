#!/usr/bin/env python

import os
import numpy as np
import pandas as pd

class Transform_Data(object):
    """
    This class takes the clean IR data and applies a transformation to it.
    Common applications are the simple daily difference, fractional derivative,
    ratios and logarithimic.
                
    RETURN:
    -------
    A dataframe with the following columns:
      $date: array of np.datetime64 times.
      $ir: intrabank interest rate
      $ir_clean: intrabank interest rate where spikes have been removed.
    
    Outputs:
    --------
    None
    """    
    
    def __init__(self, df, incr, application):
        self.df = df
        self.incr = incr
        self.application = application

    def increment_bin(self):
        #Smooth the IR data using bin sizes of "increment" days and taking the
        #IR median in each.
        group_index = np.arange(len(self.df))//self.incr
        aggregator = {'date' : 'first', 'ir' : 'mean'}
        self.df = self.df.groupby(group_index).agg(aggregator)

    def run_transform_data(self):
        self.increment_bin()

        if self.application == 'simple_diff':
            self.df['ir_transf'] = self.df['ir'].diff(-1)
            #print(self.df)
        elif self.application == 'log_ratio':
            self.df['ir_transf'] = np.log10(self.df.ir / self.df.ir.shift())
        else:
            raise ValueError(
              'Application %s is not supported' %self.application)
        
        return self.df
