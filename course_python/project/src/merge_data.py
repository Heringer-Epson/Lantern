#!/usr/bin/env python

import os, time
import pickle
import numpy as np
import pandas as pd

from clean_timestamps import Clean_Timestamps

#Define decorator functions.
def operation_time(func):
    def inner(*args):
        start_time = time.time()
        print('Processing %s...' %('"' + func.__name__) + '"')
        func(*args)
        print('  --Completed in %.2f s' %(time.time() - start_time))
    return inner
    
class Merge_Data(object):
    """
    This routine reads and pre-process the relevant data files. It then outputs
    a json file which can be readily used for data analysis.
    
    Input files:
    ------------
    heart_rate.csv
    exercise.csv
    floors_climbed.csv
    sleepdata.csv
    step_count.csv
     
    Outputs:
    --------
    ./../outputs/master_data.pkl'
    """    
    
    def __init__(self):
        
        self.M = {}
        
        self.ref_time = None #reference time used for all input files.
        
        self.top_dir = os.path.abspath(
          os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
        self.run_preproc_data()
    
    @operation_time
    def clean_heart_rate(self):

        fpath = os.path.join(self.top_dir + '/data/heart_rate.csv')
        D = pd.read_csv(fpath, header=0, index_col=0, low_memory=False)

        #Only a few irrelevant columns contain nan. Drop these columns.
        drop_cols = D.columns[D.isna().any()].tolist()
        #print(drop_cols)
        D.drop(drop_cols, axis=1, inplace=True)
               
        start_t = D['start_time'].values
        start_obj = Clean_Timestamps(start_t, t_format='%Y-%m-%d %H:%M:%S.%f')
        
        #By inspecting the relative times, one sees that the earlist times
        #are spurious. The were also used as a reference to compute time
        #lapses. Remove these entries (rows) and re-compute time lapses.
        #print(start_obj.get_relative_time())
        #print(start_obj.t_ref_idx)
        D.drop(start_obj.t_ref_idx, inplace=True)
        del(start_obj)
        
        start_t = D['start_time'].values
        start_obj = Clean_Timestamps(start_t, t_format='%Y-%m-%d %H:%M:%S.%f')
        self.time_ref = start_obj.dt_ref #Assign reference time.
        
        #Data note: the column 'end_time' is identical to 'start_time' and
        #the columns 'update_time' and 'create_time' are also identical.
        #Using 'update_time' for end_time. Actual meaning is not clear.
        end_t = D['update_time'].values
        end_obj = Clean_Timestamps(
          end_t, t_format='%Y-%m-%d %H:%M:%S.%f', dt_ref=self.time_ref)

        #Update dataframe with relative start, end and duration times (days).
        D['start_time_rel'] = start_obj.get_relative_time()
        D['end_time_rel'] = end_obj.get_relative_time()
        D['duration'] = D['end_time_rel'] - D['start_time_rel']
        D['duration'] = D['duration']*24*60. #Convert days to min.

        #get standard edviation for duration time and remove spurious values.
        duration_std = np.std(D['duration'].values)
        D.drop(
          D[D['duration'] > 5.*duration_std].index, inplace=True)

        #Sort dataframe according to starting_time.
        D.sort_values(by ='start_time_rel', inplace=True)
        
        #Store cleaned dataframe in the master dataframe.
        self.M['heartrate'] = D
        del(D)

    @operation_time
    def clean_floors_climbed(self):
        #General notes:
        #No columns exhibit nan.
        #Start_time does not exhibit spurious entries.

        fpath = os.path.join(self.top_dir + '/data/floors_climbed.csv')
        D = pd.read_csv(fpath, header=0, index_col=0, low_memory=False)

        start_t = D['start_time'].values
        start_obj = Clean_Timestamps(
          start_t, t_format='%Y-%m-%d %H:%M:%S.%f', dt_ref=self.time_ref)

        end_t = D['end_time'].values
        end_obj = Clean_Timestamps(
          end_t, t_format='%Y-%m-%d %H:%M:%S.%f', dt_ref=self.time_ref)
 
        #Update dataframe with relative start, end and duration times (days).
        D['start_time_rel'] = start_obj.get_relative_time()
        D['end_time_rel'] = end_obj.get_relative_time()
        D['duration'] = D['end_time_rel'] - D['start_time_rel']
        D['duration'] = D['duration']*24*60. #Convert days to min. 

        #get standard edviation for duration time and remove spurious values.
        duration_std = np.std(D['duration'].values)
        D.drop(
          D[D['duration'] > 4.*duration_std].index, inplace=True)
        
        #Sort dataframe according to starting_time.
        D.sort_values(by ='start_time_rel', inplace=True)
        
        #Store cleaned dataframe in the master dataframe.
        self.M['floorsclimbed'] = D
        del(D)
    
    @operation_time
    def clean_exercise(self):
        #General notes:
        #Duration is in miliseconds.

        fpath = os.path.join(self.top_dir + '/data/exercise.csv')
        D = pd.read_csv(fpath, header=0, index_col=0, low_memory=False)

        #Drop irrelevant columns.
        keep_cols = [
          'start_time', 'end_time', 'distance', 'max_altitude', 'mean_speed',
          'calorie', 'max_speed', 'duration']
        D = D[keep_cols]

        start_t = D['start_time'].values
        start_obj = Clean_Timestamps(
          start_t, t_format='%Y-%m-%d %H:%M:%S.%f', dt_ref=self.time_ref)

        end_t = D['end_time'].values
        end_obj = Clean_Timestamps(
          end_t, t_format='%Y-%m-%d %H:%M:%S.%f', dt_ref=self.time_ref)

        #Update dataframe with relative start, end and duration times (days).
        D['start_time_rel'] = start_obj.get_relative_time()
        D['end_time_rel'] = end_obj.get_relative_time()

        #Replace nan values with medians.
        cols_with_values = [
          'distance', 'max_altitude', 'mean_speed', 'calorie', 'max_speed']
        for key in cols_with_values:
            D[key].fillna((D[key].median()), inplace=True)
        
        #get standard edviation for duration time and remove spurious values.
        duration_std = np.std(D['duration'].values)
        D.drop(
          D[D['duration'] > 4.*duration_std].index, inplace=True)
        
        #Sort dataframe according to starting_time.
        D.sort_values(by ='start_time_rel', inplace=True)
        
        #Store cleaned dataframe in the master dataframe.
        self.M['exercise'] = D
        del(D)

    @operation_time
    def clean_step_count(self):
        #Notes:
        #The end time is always a fixed interval past the start time (1min).
        
        fpath = os.path.join(self.top_dir + '/data/step_count.csv')
        D = pd.read_csv(fpath, header=0, index_col=0, low_memory=False)


        #Drop irrelevant columns.
        drop_cols = [
          'create_time', 'datauuid', 'time_offset', 'pkg_name', 'update_time']
        #print(drop_cols)
        D.drop(drop_cols, axis=1, inplace=True)

        start_t = D['start_time'].values
        start_obj = Clean_Timestamps(
          start_t, t_format='%Y-%m-%d %H:%M:%S.%f', dt_ref=self.time_ref)

        end_t = D['end_time'].values
        end_obj = Clean_Timestamps(
          end_t, t_format='%Y-%m-%d %H:%M:%S.%f', dt_ref=self.time_ref)

        #Update dataframe with relative start, end and duration times (days).
        D['start_time_rel'] = start_obj.get_relative_time()
        D['end_time_rel'] = end_obj.get_relative_time()
        D['duration'] = D['end_time_rel'] - D['start_time_rel']
        D['duration'] = D['duration']*24*60. #Convert days to min. 

        #Replace nan values with medians.
        cols_with_values = ['count', 'calorie', 'speed', 'distance']
        for key in cols_with_values:
            D[key].fillna((D[key].median()), inplace=True)
        
        #get standard edviation for duration time and remove spurious values.
        duration_std = np.std(D['duration'].values)
        #print(duration_std)
        #D.drop(
        #  D[D['duration'] > 4.*duration_std].index, inplace=True)
        
        #Sort dataframe according to starting_time.
        D.sort_values(by ='start_time_rel', inplace=True)
 
        #Store cleaned dataframe in the master dataframe.
        self.M['stepcount'] = D
        del(D) 

    @operation_time
    def save_output(self):
        fpath = os.path.join(self.top_dir + '/OUTPUTS/master_data.pkl')
        with open(fpath, 'wb') as f:
            pickle.dump(self.M, f, pickle.HIGHEST_PROTOCOL)        
                    
    def run_preproc_data(self):
        self.clean_heart_rate()
        self.clean_floors_climbed()
        self.clean_exercise()
        self.clean_step_count()
        self.save_output()

