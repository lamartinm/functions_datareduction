#Function that reads the data file
def read_data(np, name_data, index, num_headers):
	return np.loadtxt(name_data %index, skiprows = num_headers)

#plot 2D data
def plot_2d_data(plt, np, data, num_channels, num_pixels):
	plt.imshow(np.transpose(data), extent=[0,num_channels,0,num_pixels], aspect='auto')
	plt.xlabel('Emission energy (keV)')
	plt.ylabel('pixel')
	plt.show()
	
#align data based on an energy calibration file and a linear interpolation
def align_data(np, name_energy, pixel, data, num_channels, e_max ):
	print('pixel '+str(pixel))
	energy = np.loadtxt(name_energy) #load energy calibration file
	energy_int =energy.astype(int) #take entries as int
	if np.max(data[:,pixel])>0 and np.max(energy_int[:,pixel])>0:#if the pixel is not turned off and if the calibration is done
		print('good pixel')
		energy_pixel=energy_int[:,pixel]#selects energy calibration of pixel
		energy_range=np.arange(np.min(energy_pixel[energy_pixel>0]), np.max(energy_pixel[energy_pixel>0]),1) #crates a mesh based on the energy calibration
		data_interp_long=np.interp(energy_range*num_channels/energy_range[-1], np.arange(0,num_channels,1), data[:,pixel]) #interpolation
		data_interp=data_interp_long[np.arange(0,e_max*1000,10)] #take every tenth value of the interpolation
	else:		
		print('bad pixel')
		data_interp=0
	return data_interp
