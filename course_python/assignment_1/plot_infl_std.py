import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.ticker import MultipleLocator

mpl.rcParams['mathtext.fontset'] = 'stix'
mpl.rcParams['mathtext.fontset'] = 'stix'
mpl.rcParams['font.family'] = 'STIXGeneral'
fs = 28. #Default font size for plots.

class Plot_Heart(object):
    """
    Description:
    ------------
    This code plots the inflamation data.

    Parameters:
    -----------
    show_fig ~ bool
        Flag to determine whether or not to display the figure.
    save_fig ~ bool
        Flag to determine whether or not to save the figure.    

    Outputs:
    --------
    ./../OUTPUTS/analyses/Fig_std.png
    
    """        
    def __init__(self, show_fig, save_fig):
        self.show_fig = show_fig
        self.save_fig = save_fig

        #Initialize figure and its axes.
        self.fig = plt.figure(figsize=(10,10))
        self.ax = self.fig.add_subplot(111)

        self.data = None

        #Get the path to the top directory.
        self.top_dir = os.path.abspath(
          os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
                
        #Call all functions below to produce the figure.
        self.make_plot()
        
    def set_fig_frame(self):
    
        xlabel = r'Time [days]'
        
        ylabel = r'std inflammation [arb]'
        self.ax.set_xlabel(xlabel, fontsize=fs)
        self.ax.set_ylabel(ylabel, fontsize=fs)
        #self.ax.set_xlim(1.e9, 1.e12)
        self.ax.set_ylim(0., 6.)
        self.ax.tick_params(axis='y', which='major', labelsize=fs, pad=8)      
        self.ax.tick_params(axis='x', which='major', labelsize=fs, pad=8)
        self.ax.tick_params('both', length=12, width=2., which='major',
                             direction='in', right=True, top=True)
        self.ax.tick_params('both', length=6, width=2., which='minor',
                             direction='in', right=True, top=True) 
        self.ax.xaxis.set_minor_locator(MultipleLocator(5.))
        self.ax.xaxis.set_major_locator(MultipleLocator(10.))
        self.ax.yaxis.set_minor_locator(MultipleLocator(.5))
        self.ax.yaxis.set_major_locator(MultipleLocator(2.)) 

    def retrieve_data(self):
        #Read heart data.
        fpath = os.path.join(self.top_dir + '/data/data/inflammation-01.csv')
        self.data = np.loadtxt(fpath, delimiter=',')
               
        
    def plot_quantities(self):
        self.ax.plot(np.std(self.data, axis=0), lw=3., c='k')
        
        diff = np.diff(self.data)
        print(np.max(np.abs(diff), axis=1))


    def manage_output(self):
        plt.tight_layout()
        if self.save_fig:
            fpath = './../OUTPUTS/analyses/Fig_std.png'
            plt.savefig(fpath, format='png')
        if self.show_fig:
            plt.show()
        plt.close(self.fig)    

    def make_plot(self):
        self.set_fig_frame()
        self.retrieve_data()
        self.plot_quantities()
        self.manage_output()             

if __name__ == '__main__':
    Plot_Heart(show_fig=False, save_fig=True)
