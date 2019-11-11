#!/usr/bin/env python

import os

from initialize_run import Init_Run
from preprocess_data import Preproc_Data
from fit_distributions import Fit_Distr
from plot_ir import Plot_Ir
from plot_structure import Plot_Structure
from plot_std import Ir_Std
from plot_corr import Plot_Corr

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
    def __init__(self, curr='USD', application='simple_diff', t_ival=None):
       
        incr = [1, 25, 130, 253] #[1d, 1m, 6m, 1yr]
        #incr = [1, 25] #[1d, 1m, 6m, 1yr]
        tenor = [1, 3, 12]
        outdir = Init_Run(curr, application).run_init()
        
        M = Preproc_Data(curr, t_ival, application, tenor, incr).run_preproc_data()
        #Fit_Distr(M, tenor, incr, outdir).run_fitting()
        #Plot_Ir(M, application, tenor, incr, outdir).make_plot()
        #Plot_Structure(M, tenor, incr, outdir).make_plot()
        #Ir_Std(M, tenor, incr, outdir, 'ir').make_plot() 
        #Ir_Std(M, tenor, incr, outdir, 'ir_transf').make_plot() 
        Plot_Corr(M, curr, tenor, outdir).make_plot() 
       
if __name__ == '__main__':
    Master(application='simple_diff', t_ival=['2010/01/01', '2016/01/01'])
    #Master(t_ival=['2012/01/01', '2018/06/01'], application='log_ratio')
