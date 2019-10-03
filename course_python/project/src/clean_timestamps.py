#!/usr/bin/env python

import sys
import os
import numpy as np
import pandas as pd
from datetime import datetime
from datetime import timedelta

class Clean_Timestamps(object):
    """
    Description:
    ------------
    Given a list of timestamps, convert it relative times in days.

    Parameters:
    -----------
    show_fig ~ bool
        Flag to determine whether or not to display the figure.

    Outputs:
    --------
    TBW.
    
    """        
    def __init__(self, t, t_format, dt_ref=None):
        self.t = t
        self.t_format = t_format
        self.dt_ref = dt_ref
        
        self.dt = None
        
        self.make_datetime_objs()
        
    def make_datetime_objs(self):
        #From the input varaibles, create datetime objects. If no reference
        #time was passed, assign a reference time as the earliest epoch.
        self.dt = np.array([
          datetime.strptime(T, self.t_format) for T in self.t])

        if self.dt_ref is None:
            self.dt_ref = min(self.dt)

        #Get the index(es) of the timestamp used as reference time.
        self.t_ref_idx = np.where(self.dt == self.dt_ref)[0]

    def get_relative_time(self):
        time_diff = self.dt - self.dt_ref
        delta_time = np.array(
          [(T.days*86400. + T.seconds)/86400. for T in time_diff])
        return delta_time



