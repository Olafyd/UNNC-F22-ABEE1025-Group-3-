#Name: JJCHUEH
#date 2023. 2. 16 
#this file is for running EnergyPlus parametric simulation

from OOP_logic import simulation

eplus_run_path = './EnergyPlus9.5/energyplus'
idf_path = './1ZoneUncontrolled_win_test.idf'
out_put_dir='./simulation_output'
para_keys_1 = ['WindowMaterial:SimpleGlazingSystem', 'SimpleWindow:DOUBLE PANE WINDOW', 'solar_heat_gain_coefficient'] 
para_keys_2 = ['WindowMaterial:SimpleGlazingSystem', 'SimpleWindow:DOUBLE PANE WINDOW', 'u_factor'] 
interval = 1

simul=simulation(eplus_run_path,idf_path,out_put_dir)
simul.interval=0.25
simul.start_a=0.25
simul.end_a=1
#cause i use np.arrange, it actually ends at 0.75
simul.start_b=1.0
simul.end_b=2.75
#cause i use np.arrange, it actually ends at 2.5
simul.para_key_a=para_keys_1
simul.para_key_b=para_keys_2

simul.run_simulation()
print(simul._simulation_results)


