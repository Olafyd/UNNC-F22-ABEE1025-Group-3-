import pandas as pd
import copy
import os
import json

from StaticEplusEngine import run_eplus_model, convert_json_idf
def run_25_parameter_parametric(eplus_run_path, idf_path, output_dir,
                                parameter_key, parameter_vals):
    """
    """
    ######### step 1: convert an IDF file into JSON file #########
    convert_json_idf(eplus_run_path, idf_path)
    epjson_path = idf_path.split('.idf')[0] + '.epJSON'

    ######### step 2: load the JSON file into a JSON dict #########
    with open(epjson_path) as epJSON:
        epjson_dict = json.load(epJSON)

    ######### step 3: change the JSON dict value #########
    # ['WindowMaterial:SimpleGlazingSystem', 
    #                           'SimpleWindow:DOUBLE PANE WINDOW', 
    #                           'solar_heat_gain_coefficient']
    inner_dict = copy.deepcopy(epjson_dict)
    import numpy as np
    for i in np.arange (0.25, 0.75, 0.02):
        if i < len(parameter_key) - 1:
            inner_dict = inner_dict [parameter_key[i]]
        inner_dict[parameter_key[-1]] = parameter_vals

      
    ######### step 4: dump the JSON dict to JSON file #########
    with open(epjson_path, 'w') as epjson:
        json.dump(epjson_dict, epjson)

    ######### step 5: convert JSON file to IDF file #########
    convert_json_idf(eplus_run_path, epjson_path)

    ######### step 6: run simulation #########
    run_eplus_model(eplus_run_path, idf_path, output_dir)