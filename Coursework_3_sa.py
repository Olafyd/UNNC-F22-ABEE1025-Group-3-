# thermal_absorptance

from StaticEplusEngine import run_eplus_model, convert_json_idf
import json

eplus_run_path = './Energyplus9.5.0/energyplus'
# the energyplus exe file
eplus_model_path = './1ZoneUncontrolled_win_1.idf'
# the model file
eplus_output_dir = './result'
# the result location 

#---change parameter---
convert_json_idf(eplus_run_path, eplus_model_path)
epjson_path = eplus_model_path.split('.idf')[0] + '.epJSON'

with open (epjson_path) as f:
	epjson = json.load(f)

parameter_vals = [x*0.04 for x in range(0,26)]

for i in parameter_vals:
	epjson_new = epjson
	epjson_new['Material:NoMass']['R31LAYER']['thermal_absorptance'] = i
	with open(f'epjson_path_ta{i}.epJSON', 'w') as f:
		json.dump(epjson_new, f, indent = 4)

# ---run simulation---(ERRO)
import subprocess
eplus_run_path = './Energyplus9.5.0/energyplus'
epw_relative_filepath = './USA_IL_Chicago-OHare.Intl.AP.725300_TMY3.epw'
eplus_output_dir = './result'
for i in parameter_vals:
    input_file = f'epjson_path_ta{i}.epJSON'
    output_file = eplus_output_dir + f'/run_result{i}'
    cl_st = (f'"{eplus_run_path}"'
            + f'--output-prefix thermal_absorptance{i}'
            + '--readvars ' 
            + f'--output-directory "{eplus_output_dir}"'
            + f'--weather "{epw_relative_filepath}" '
            + f'"{input_file}"'
            )

    subprocess.run(cl_st, capture_output = True)