from functions_ligia import *
import numpy as np
import matplotlib.pyplot as plt


name_data="/space/data/AgRTIL_DO54/AgRTIL_DO54_250K_2/scan_%04d.dat" #name and path of file
index=1 # index in the scan
num_headers=11 #number of headers
num_channels=2048 #number of channels
num_pixels=100 #number of pixels in the detector

# Reads data "name_data"
data=read_data(np, name_data, index, num_headers)

#plots 2D array data (num_channels,num_pixels)
plot_2d_data(plt, np, data, num_channels, num_pixels)

name_energy="energy_he.dat" #energy calibration file
e_max=28 #maximum malue of energy (keV) in the calibration

#Alignment with a calibration file "name_energy"
data_interp=np.ndarray(shape=(num_pixels,e_max*100)) #intialice array of aligned data 

for pixel in range(num_pixels):
	data_interp[pixel,:]=align_data(np, name_energy, pixel, data, num_channels, e_max )

#plots 2D array aligned data (e_max*100,num_pixels)
plot_2d_data(plt, np, np.transpose(data_interp), num_channels, num_pixels)
