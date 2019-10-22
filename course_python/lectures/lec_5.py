import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class Lec_Five(object):
    """Collection of routines for lecture 4 of the python course.
    """

    def __init__(self):
        
        self.data = None
        
        self.run_funcs()
    
    def read_data(self):
        """Read and store the data from the input file.
        """
        fpath = './data/surveys.csv'
        self.survey_df = pd.read_csv(fpath, header=0, low_memory=False)
        
        fpath = './data/species.csv'
        self.species_df = pd.read_csv(fpath, header=0, low_memory=False)

        print(self.survey_df.shape)
        print(self.species_df.shape)

    def concatenate_data(self):

        data_t10 = self.survey_df.head(10)
        data_b10 = self.survey_df.tail(10)

        #Add rows.
        df_out = pd.concat([data_t10, data_b10])
        df_out = df_out.reset_index(drop=True)
        #print(df_out.head())        

    def merging_data(self):
        
        #Get intersection
        df_out = pd.merge(self.survey_df, self.species_df, how='inner')
        #print(df_out.head())
        #print(df_out.shape)

        #Preserve the left dataframe.
        df_out = pd.merge(self.survey_df, self.species_df, how='left')
        print(df_out.head())
        print(df_out.shape)
        
        #Identify missing values.
        print(pd.isnull(df_out[['taxa']]).any(axis=1).sum())
        
        species_id = set(self.species_df['species_id'].values)
        survey_id = set(self.survey_df['species_id'].values)
        print(species_id - survey_id)
        
        print(self.species_df[~self.species_df['species_id'].isin(self.survey_df['species_id'])])
    
    def run_funcs(self):
        self.read_data()
        self.concatenate_data()
        self.merging_data()

        
Lec_Five()

