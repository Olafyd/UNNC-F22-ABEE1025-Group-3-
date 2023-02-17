# Author: Yude Fu
# Date: 2022-10-11

from StaticEplusEngine import run_eplus_model

eplus_exe_path = './energyplus9.5/energyplus' # Energyplus executable file path
eplus_model_path = './1ZoneUncontrolled_win_1.idf' # Energyplus model file path
res_dir = './result1' # Simulation result directory

run_eplus_model(eplus_exe_path, eplus_model_path, res_dir)

For example, ['WindowMaterial:SimpleGlazingSystem', 
    'SimpleWindow:DOUBLE PANE WINDOW', 'solar_heat_gain_coefficient'] 
    means (assume json_model is the EnergyPlus JSON model) json_model 
    ['WindowMaterial:SimpleGlazingSystem']
    ['SimpleWindow:DOUBLE PANE WINDOW']
    ['solar_heat_gain_coefficient'] is the innermost key to be accessed.