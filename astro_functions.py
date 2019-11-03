#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 11:10:18 2019

@author: Ahana Banerjee

Astronomical Image Processing Lab

"""

#%% import packages

from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import norm
import matplotlib.mlab as mlab
#import seaborn as sns

#sns.set()

# imoprt data

filename = 'A1_mosaic.fits'

hdulist = fits.open(filename)

all_data = np.array(hdulist[0].data) # convert data into numpy array

flat_data = np.ndarray.flatten(all_data) # flattened array

#%% return dimensions

def dimensions(all_data):
    return np.array(all_data).shape

#%% histogram of all data (log scale)

def hist_all_data(flat_data):

    plt.hist(np.log10(flat_data[flat_data >= 3000]),bins=1000)
    plt.xlabel('Relative Brightness')
    plt.ylabel('Frequency (log scale)')
    plt.title('Histogram of Brightnesses for Astronomical Image')
    plt.yscale('log')
    plt.grid(alpha = 0.2)

#%% gaussian histogram

def gaussian_histogram(flat_data):

    flat_data = flat_data[flat_data >= 3350]
    flat_data = flat_data[flat_data <= 3500]
    
    # best fit of data
    (mu, sigma) = norm.fit(flat_data)
    
    # the histogram of the data
    n, bins, patches = plt.hist(flat_data, 80, normed=1, facecolor='green', alpha=0.75)
    
    # add a 'best fit' line
    y = mlab.normpdf( bins, mu, sigma)
    l = plt.plot(bins, y, 'r--', linewidth=2)
    
    #plot
    plt.xlabel('Relative Brightness')
    plt.xlim(3340, 3500)
    plt.ylabel('Probability')
    plt.title(r'$\mathrm{Histogram\ of\ Background Brightness:}\ \mu=%.3f,\ \sigma=%.3f$' %(mu, sigma))
    plt.grid(True)
    
    plt.show()
    
#%% plot image

def plot_image(all_data, color):
    
    if color == 'grey':
        plt.imshow(np.log10(all_data), cmap='gray')
        
    if color == 'hot':
        plt.imshow(np.log10(all_data), cmap='hot')
    plt.colorbar(label = 'Relative Brightness')
    plt.grid(alpha = 0)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Astronomical Image')

#%% remove background and plot histogram

def remove_background_flat(flat_data):

    (mu, sigma) = norm.fit(flat_data)
    flat_data  = flat_data[flat_data >= mu + 3 * sigma]
    plt.hist(flat_data, 80)
    plt.title('Background Removed Histogram')
    plt.xlabel('Relative Brightness')
    plt.ylabel('No. Occurrences')
    plt.grid(alpha = 0.2)
    plt.show()
    
#%% remove background and plot image

def remove_background(data):
    data[data <= 3472] = 0
    return data

#%% finding indices of pixels with descending brightness

#indices = []
#for i in range(len(flat_data)):
#    indices.append(np.where(all_data == flat_data[i]))
#    print(indices)
#    
#
#a = dict(zip(flat_data, indices))

#sorteeedd = np.matrix.sort(all_data)

#keys = ['brightness', 'index']


#flat_sorted_data = np.sort(flat_data)[::-1]
#
#for i in range(len(flat_sorted_data)):
#    brightness_ordered.append(np.where(all_data == np.max(flat_sorted_data[i])))


#print(brightness_ordered)




