#!/usr/bin/env python

import os
from merge_data import Merge_Data

class Master(object):
    """
    Code description: main script to call routines to analyse data from the
    Lantern institute.
    """
    def __init__(self, preprocess_data):
        
        if preprocess_data:
            Merge_Data()

if __name__ == '__main__':
    Master(preprocess_data=True)


