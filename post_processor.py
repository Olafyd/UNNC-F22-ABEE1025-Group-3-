 # Author: CHEUH
 # Creating Date: 2022-10-27

 
import pandas as pd
import datetime as dt
import matplotlib.dates as matdates
import matplotlib.pyplot as plt

import pandas as pd
import datetime as dt
import matplotlib.dates as matdates
import matplotlib.pyplot as plt

'''
----- step 1: making sure the data is correct then transfer into pandas datetime form -----
'''
def eplus_to_datetime(date_str):
	if date_str[-8:-6]!= '24':
		date_pd = pd.to_datetime(date_str)
	# the date time is accurate --> transfer into pandas form
	else:
		date_str = date_str[0:-8] + '00' + date_str[-6:]
		date_pd = pd.to_datetime(date_str) + dt.timedelta(days = 1)
	# the data is inaccurate --> correct it --> transfer into pandas form 

	return date_pd 

'''
----- step 2: input the data toward matploylid function and style the plot-----
	
	Inputs:
		i.		output_paths(dict): the same as the output_paths in parametric_simulation
		ii.		plot_column_name(string): the column name of which 
											the results will be plotted in eplusout.csv
		iii.	y_axis_title(string): the title to the y axis of the plot
		iv.		plot_title(string): the title to the plot
'''

def plot_1D_results(output_paths, plot_column_name, 
					y_axis_title, plot_title):

	fig, axs = plt.subplots(1, 1, figsize=(20,10))
	# with axs --> easier to design the plot
	fontsize = 20
	#set the size of the plot to 10*20
	for explusout.cvs in this_path:
		this_path = 'param_exp_1'
		this_df = pd.read_cvs(this_path)
		# input the data from result of run_one_parameter_paramatric
		this_df['Date/Time'] = '2002' + this_df['Date/Time']
		this_df['Date/Time'] = this_df['Date/Time'].apply(eplus_to_datetime)
		# adding year to the date_str, then transfer the data into pandas form
		x_st_date = this_df.iloc[0,0]
		x_ed_date = this_df.iloc[0,-1]
		# set the starting and ending of the x_date
		x_date = this_df['Date/Time']
		y_iat = this_df[plot_column_name].values
		# set the x and y value
		# the y value is defined in the file cw_part2_main.py
		axs.plot(x_date, y_iat, 
			alpha = 0.7,
			ls = '--',
			lw = 2, 
			label = data)
		# plot with x and y and style the plot

		datetime_ax_loc = matdates.HourLocator()
		datetime_ax_fmt = matdates.DateFormatter('%H:%M')
		# set the funtion for interval of the xaxis becomes hour-base 
		# with the format hour+minutes
		axs.xaxis.set_major_locator(datetime_ax_loc)
		axs.xaxis.set_major_formatter(datetime_ax_fmt)
		# apply the function on to the xaxis
		for tick in axs.xaxis.get_major_ticks():
			tick.label.set_fontsize(fontsize*0.8)
		for tick in axs.yaxis.get_major_ticks():
			tick.label.set_fontsize(fontsize*0.8)
		# set the font size of ticks in xaxis and yaxis
		axs.tick_params('x', labelrotation = 45)
		# rotate xaxis parameters by 45 degree
		axs.set_xlabel('Time (%s to %s)'%(data_st_date, data_ed_date),
						fontsize = fontsize)
		axs.set_ylabel('Air Temperature (C)',
						fontsize = fontsize)
		# set x and y labels
		axs.yaxis.get_offset_text().set_fontsize(fontsize*0.7)
		axs.legend(fontsize = fontsize)
'''
	Outputs: 
			this function has no outputs. 
			It will read all eplusout.csv files listed in output_paths, 
			and plot the data at the column plot_column_name using matplotlib. 

	The final plot figure will have:
			i.		use hourly time steps as the x-axis
			ii.		have y_axis_title as the y axis title
			iii.	have plot_title as the plot title
			iv.		each line in the plot has the key in output_paths as the legend 
'''