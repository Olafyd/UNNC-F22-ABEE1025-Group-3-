#Author: Yude Fu
#date 2023. 2. 16
#this file is for EnergyPlus parametric simulation

import os,sys
import json
import copy




from StaticEplusEngine import run_eplus_model,convert_json_idf


def run_combine_simulation_helper(eplus_run_path, idf_path, this_output_dir,
					parameter_key_a, parameter_val_a, parameter_key_b,parameter_val_b):
	"""
	This is a helper function to run one simulation with the changed
	value of the parameter_key
	"""
	######### step 1: convert an IDF file into JSON file #########
	convert_json_idf(eplus_run_path, idf_path)
	epjson_path = idf_path.split('.idf')[0] + '.epJSON'

	######### step 2: load the JSON file into a JSON dict #########
	with open(epjson_path) as epJSON:
		epjson_dict = json.load(epJSON)

	######### step 3: change the JSON dict value #########
	# ['WindowMaterial:SimpleGlazingSystem', 
	#			 				'SimpleWindow:DOUBLE PANE WINDOW', 
	#			 				'solar_heat_gain_coefficient']
	inner_dict = epjson_dict
	for i in range(len(parameter_key_a)):
		if i < len(parameter_key_a) - 1:
			inner_dict = inner_dict[parameter_key_a[i]]
	inner_dict[parameter_key_a[-1]] = parameter_val_a
	inner_dict[parameter_key_b[-1]] = parameter_val_b


	######### step 4: dump the JSON dict to JSON file #########
	with open(epjson_path, 'w') as epjson:
		json.dump(epjson_dict, epjson)

	######### step 5: convert JSON file to IDF file #########
	convert_json_idf(eplus_run_path, epjson_path)

	######### step 6: run simulation #########
	run_eplus_model(eplus_run_path, idf_path, this_output_dir)
	return this_output_dir + '/eplusout.csv'

def run_one_parameter_parametric(eplus_run_path,idf_path,output_dir,parameter_key_a,parameter_vals_a
								,parameter_key_b,parameter_vals_b):
	'''This is a function which automatically run simulations with different 
	solar_heat_gain_coefficient and u values, ranging from 0.25 to 0.75 and 1 to 2.5
	with 0.25 interval, for the model
	'''
	res_dict={}

	if not os.path.isdir(output_dir):
		os.mkdir(output_dir)

	for i in range(len(parameter_vals_a)):
		for j in range(len(parameter_vals_b)):
			this_output_dir = output_dir + os.sep + str(parameter_vals_a[i])+'_'+str(parameter_vals_b[j])
	
			this_res_path = run_combine_simulation_helper(eplus_run_path,idf_path,this_output_dir,parameter_key_a,
				parameter_vals_a[i], parameter_key_b,parameter_vals_b[j])

			parameter_val_a = parameter_vals_a[i]
			parameter_val_b = parameter_vals_b[j]
			res_dict[str(parameter_val_a)+'_'+str(parameter_val_b)] = this_res_path

	print (res_dict)
	return res_dict

