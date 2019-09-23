#!/usr/bin/env python

import os, time
import pandas as pd

def operation_time(func):
    def inner(*args):
        start_time = time.time()
        print('Processing %s...' %(func.__name__))
        func(*args)
        print('  Completed in %.2f s' %(time.time() - start_time))
    return inner
    
class Inspect_Data(object):
    """
    TBW.
     
    Outputs:
    --------
    ./../outputs/X'
    """    
    
    def __init__(self):
        
        self.D = {}
        
        self.top_dir = os.path.abspath(
          os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
        self.run_preproc_data()
    
    @profile
    @operation_time
    def load_data(self):
        for i in range(12):
            tag = ('%02d' % (i + 1))
            fname = 'inflammation-' + tag + '.csv' 
            fpath = os.path.join(self.top_dir + '/data/data/' + fname)
            self.D[fname] = pd.read_csv(fpath)

    def run_preproc_data(self):
        self.load_data()

