import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class Lec_Four(object):
    """Collection of routines for lecture 4 of the python course.
    """

    def __init__(self):
        
        self.data = None
        
        self.run_funcs()
    
    def read_data(self):
        """Read and store the data from the input file.
        """
        fpath = './data/surveys.csv'
        self.data = pd.read_csv(fpath, header=0, low_memory=False)
        #print(self.data.head(n=5))
        print(self.data.shape)

    def preproc_data(self):
        self.data = self.data.dropna(subset=['weight'])
        print(self.data.shape)

    def check_unique(self):
        clean_species = self.data.dropna(subset=['species_id'])
        unique_species = np.unique(clean_species.species_id)
        print('There are %i unique species' %(len(unique_species)))

    def grouping(self):
        gr = self.data.groupby('species_id')
        #print(gr)
        #print(gr.describe())
        #print(gr.count())
        
    def count_gender(self):
        #print(self.data.sex)
        #print(self.data.groupby('sex').count())
        #print(self.data.groupby('sex').count()['record_id'])
        #self.data.groupby('sex').count()['record_id'].plot(kind='bar')
        #plt.show()
        
        #data_grouped = self.data.groupby(['sex', 'species_id']).count()
        #data_grouped = self.data.groupby(['species_id', 'sex']).count()
        self.data.groupby(
          ['species_id', 'sex']).count()['record_id'].unstack().plot(
          kind='bar', color=['r', 'b'], stacked=True)
        plt.yscale('log')
        plt.show()
        #print(data_grouped.index)
        #print(data_grouped['record_id'])
        
    def utilities(self):
        D = self.data.copy()
        #print(D)
        #print(D[['species_id', 'sex']][2:5])
        #print(D.iloc[2:5,1:3])
        #print(D[D['weight']>2.])
        #print(D[D['year']==2000].groupby('sex').count()['record_id'])
        #print(D[((D['year']==2000) & (D['sex']=='M'))].count()['record_id'])
        print(D[(D['species_id'].isin(['PX', 'DM']))])
        
    def assignment(self):
        D = self.data.copy()
        #D = D[((D['sex'].isin(['M','F'])) & (D['weight'] > 0.))]
        #print(D)
        #D = D.groupby(['sex', 'plot_id']).mean()['record_id']
        #D.unstack().plot(kind='bar', color=['r', 'b'], stacked=True)
        
        D = D[D['weight']>0.].groupby(['plot_id', 'sex']).mean()
        #D = D['weight'].unstack()
        D = D['weight']
        D.plot(kind='bar', color=['r', 'b'], stacked=True)
        plt.show()
    
    def plot_foot_weight(self):
        sns.scatterplot(self.data.hindfoot_length,self.data.weight)
        plt.show()
    
    def run_funcs(self):
        self.read_data()
        #self.preproc_data()
        #self.check_unique()
        #self.grouping()
        #self.count_gender()
        self.utilities()
        self.assignment()
        #self.plot_foot_weight()
        
Lec_Four()

