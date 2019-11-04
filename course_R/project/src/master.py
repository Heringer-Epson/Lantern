#!/usr/bin/env python

import os

from initialize_run import Init_Run
from preprocess_data import Preproc_Data
from transform_data import Transform_Data
from plot_ir import Plot_Ir
from fit_distributions import Fit_Distr


class Master(object):
    """
    Main routine that calls methods to read, pro-process and analyse the data.

    Parameters:
    -----------
    tenor : ~str
        Tenor to be used. Accepts '1m', '3m' and '12m'. Default is '1m'.
    curr : ~str
        Currency to be used. Accepts 'USD' and 'CAD'. Default is 'USD'.
    incr : ~str
        Time step to be used. Includes only bussiness days. Accepts '1d' and
        '25d'. Default is '1d'.
                     
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
    def __init__(self, tenor='1m', curr='USD', t_ival=None, incr=2,
                 application='simple_diff'):
       
        outdir = Init_Run(tenor, curr, incr, application).run_init()
        data = Preproc_Data(tenor, curr, t_ival).run_preproc_data()
        data = Transform_Data(data, incr, application).run_transform_data()
        Plot_Ir(data, application, outdir).make_plot()
        Fit_Distr(data, outdir).run_fitting()
        
        #print(data.head(n=10))
        
        
        

       
if __name__ == '__main__':
    #Master(t_ival=['2017/01/01', '2018/06/01'])
    Master(t_ival=['2012/01/01', '2018/06/01'], application='log_ratio')
