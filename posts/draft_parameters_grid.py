# import everything
import os, getpass

kilosort2_path = '/home/samuel/Documents/Spikeinterface/Kilosort2'
os.environ["KILOSORT2_PATH"] = kilosort2_path

kilosort_path = '/home/samuel/Documents/Spikeinterface/KiloSort/'
os.environ["KILOSORT_PATH"] = kilosort_path

ironclust_path = '/home/samuel/Documents/Spikeinterface/ironclust'
os.environ["IRONCLUST_PATH"] = ironclust_path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path


import spikeinterface as si
import spikeinterface.extractors as se
import spikeinterface.sorters as ss
import spikeinterface.widgets as sw
import spikeinterface.comparison as sc

from spikeinterface.comparison import GroundTruthStudy

p = Path('/home/samuel/Documents/DataSpikeSorting/mearec/')
study_folder = p / 'study_mearec_SqMEA1015um/'

param_folder = p / 'param_search'


mearec_filename = p / 'recordings_50cells_SqMEA-10-15_600.0_10.0uV_21-01-2020_18-12.h5'



study = GroundTruthStudy(study_folder)

sorter_names = ['ironclust', 'spykingcircus', 'herdingspikes']
#~ sorter_names = [ 'herdingspikes']
radius_list = [20, 50, 100, 150, 200]

def run_search_optimal_radius():
    rec  = se.MEArecRecordingExtractor(mearec_filename)
    
    param_names = {
        'ironclust': 'adjacency_radius',
        'spykingcircus': 'adjacency_radius',
        'herdingspikes': 'probe_neighbor_radius',
    }
    
    for sorter_name in sorter_names:
        for radius in radius_list:
            params = {param_names[sorter_name] : radius}
            sorting = ss.run_sorter(sorter_name, rec,
                                        output_folder=param_folder / f'{sorter_name}_{radius}',
                                        delete_output_folder=True,
                                        **params)
            se.NpzSortingExtractor.write_sorting(sorting, param_folder / f'{sorter_name}_{radius}.npz')
        


def plot_results():
    gt_sorting = se.MEArecSortingExtractor(mearec_filename)
    
    
    snr = study.get_units_snr()
    
    fig, axs = plt.subplots(nrows=len(sorter_names), ncols=len(radius_list))
    for r, sorter_name in enumerate(sorter_names):
        for c, radius in enumerate(radius_list):
            sorting = se.NpzSortingExtractor(param_folder / f'{sorter_name}_{radius}.npz')
            comp = sc.compare_sorter_to_ground_truth(gt_sorting, sorting)
            perfs = comp.get_performance(method='by_unit')
            axs[r, c].scatter(snr['snr'], perfs['accuracy'], s=10)
        
        
            axs[0, c].set_title(f'radius {radius}')
        
        axs[r, 0].set_ylabel(sorter_name)
    
    plt.show()
        
        
        


if __name__ == '__main__':
    #~ run_search_optimal_radius()
    
    plot_results()