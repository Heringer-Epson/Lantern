#!/usr/bin/env python

import os

class Init_Run(object):
    """
    TBW.
                    
    Outputs:
    --------
    None
    """    
    
    def __init__(self, tenor, curr, incr, application):
        self.tenor = tenor
        self.curr = curr
        self.incr = incr
        self.application = application
        
        self.outdir = None
    
    def init_outdir(self):
        
        run_dir = self.curr + '_' + self.tenor + '_' + str(self.incr)\
                  + '_' + self.application
        self.outdir = os.path.join('./../OUTPUTS/RUNS/', run_dir)
        if not os.path.isdir(self.outdir):
            os.mkdir(self.outdir)
        
    def run_init(self):
        self.init_outdir()
        return self.outdir
