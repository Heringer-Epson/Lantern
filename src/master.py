#!/usr/bin/env python

import os
from inspect_data import Inspect_Data

class Master(object):
    """
    Code description: main script to call routines to analyse data from the
    Lantern institute.
    """
    def __init__(self, run_inspect):
        
        if run_inspect:
            Inspect_Data()

if __name__ == '__main__':
    Master(run_inspect = True)


