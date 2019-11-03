#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 11:11:27 2019

@author: ahanabanerjee
"""
#%% imports

from astro_functions import *

#%%

dimensions(all_data)

#%%

hist_all_data(flat_data)

#%%

gaussian_histogram(flat_data)

#%%

remove_background_flat(flat_data)

#%%

plot_image(all_data, 'grey')

#%%

plot_image(remove_background(all_data), 'hot')
