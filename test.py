from parametric_simulation import run_one_parameter_parametric
import numpy
eplus_run_path = './energyplus9.5/energyplus'
idf_path = './1ZoneUncontrolled_win_1.idf'
parameter_key = ['WindowMaterial:SimpleGlazingSystem', 
'SimpleWindow:DOUBLE PANE WINDOW', 'solar_heat_gain_coefficient'] 
parameter_vals = [0.25 + i*0.02 for i in range(25)]
output_dir = './param_exp_1'

run_one_parameter_parametric(eplus_run_path, idf_path, output_dir,
                                parameter_key, parameter_vals)