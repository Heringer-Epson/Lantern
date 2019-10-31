#!/usr/bin/env python

import os
import numpy as np
import pandas as pd
from scipy.signal import savgol_filter

class Preproc_Data(object):
    """
    This class contains methods to read and preprocess the data. Preprocessing
    includes removing spikes and smoothing the data.
                
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
    
    def __init__(self, tenor, curr, t_ival):
        self.tenor = tenor
        self.curr = curr
        self.t_ival = t_ival
        self.df = None
    
    def load_data(self):
        data_dir = './../data/'
        fname = 'LIBOR_' + self.tenor + '_' + self.curr + '.csv'
        fpath = os.path.join(data_dir, fname)
        self.df = pd.read_csv(fpath, header=0, names=['date', 'ir'])[::-1]      
        
    def prepare_data(self):

        #Convert date column type to a datetime object.
        self.df['date'] = pd.to_datetime(self.df['date'])
        
        #Trim the data to include only the time interval requested.
        if self.t_ival is not None:
            cond = ((self.df['date'] >= self.t_ival[0])
                    & (self.df['date'] <= self.t_ival[1]))
            self.df = self.df[cond]

        #Some rows have a dot as entries for the intrabank rate. Romore these.
        self.df = self.df[self.df['ir'].map(lambda x: str(x)!='.')]         

        #Change type of the ir column to numeric.
        self.df['ir'] = pd.to_numeric(self.df['ir'])

    def remove_spikes(self):
        #Smooth the data and compute a rolling standard deviation day-wise
        #using 5 days windows.
        ir = self.df['ir'].values
        dates = self.df['date'].values
        ir_smooth = savgol_filter(ir, 9, 3)
        hw = pd.Timedelta(4., 'D') #date half window.
        
        sd = []
        for i,d in enumerate(dates):
            cond = ((self.df['date'] >= d - hw) & (self.df['date'] <= d + hw))
            diff = self.df['ir'][cond].values - ir_smooth[cond]
            sd.append(np.sqrt(np.sum(np.power(diff, 2))))
        
        self.df = self.df[(self.df['ir'] - ir_smooth).abs() < 5*np.array(sd)]

    def run_preproc_data(self):
        self.load_data()
        self.prepare_data()
        self.remove_spikes()
        return self.df
