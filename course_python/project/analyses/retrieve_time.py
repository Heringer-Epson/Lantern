#!/usr/bin/env python

import numpy as np
from datetime import datetime
from datetime import timedelta
from dateutil import tz

class Retrieve_Timestamps(object):
    """
    Description:
    ------------
    Given a list of time strings, convert it datetime object which are in the
    local timezone.
    """        
    def __init__(self, target, tzone, t_measurement, inp_format, time_format):
        self.target = target
        self.tzone = tzone
        self.t_measurement = t_measurement
        self.inp_format = inp_format
        self.time_format = time_format
        
        self.out = None
        self.time_obj = None
                
        self.create_date_obj()
        self.get_corrected_timeobj()

    def create_date_obj(self):
        if self.inp_format == 'datestr':
            self.time_obj = np.array(
              [datetime.strptime(t, self.time_format) for t in self.target])
        elif self.inp_format == 'milisec':
            self.time_obj = np.array(
              [datetime.fromtimestamp(t) for t in self.target])            
        else:
            raise ValueError('inp_format of %s is not accepeted.'\
                             %(self.inp_format))

    def get_corrected_timeobj(self):
        from_zone = tz.gettz(self.t_measurement)
        to_zone = [tz.gettz(t_off) for t_off in self.tzone]
        
        self.out = np.array([_t.replace(tzinfo=from_zone).astimezone(_to_zone)
                            for (_t,_to_zone) in zip(self.time_obj,to_zone)])



