# Author: Zhiang Zhang
# First create: 2022-10-10
import os
import threading
import subprocess
from EngineUtils.Logger import Logger

LOG_FMT = "[%(asctime)s] %(name)s %(levelname)s:%(message)s"
LOG_LEVEL = "INFO"
THIS_DIR = os.path.dirname(os.path.realpath(__file__))
DEFAULT_WEAT_PATH = THIS_DIR + os.sep + \
					'DefaultWeatherFiles' + os.sep + \
					'USA_IL_Chicago-OHare.Intl.AP.725300_TMY3.epw'

def convert_json_idf(eplus_run_path, model_path):
	logger = Logger().getLogger('convert_json_idf', LOG_LEVEL, LOG_FMT)
	####################################################################
	# Create an EnergyPlus process 
	cvt_json_sh = f"{eplus_run_path} --convert-only {model_path}"
	idf_dir = os.path.dirname(model_path)
	logger.debug('Convert to json script: {}'.format(cvt_json_sh))
	cvt_json_prcs = subprocess.Popen(
						cvt_json_sh,
                        shell = True,
                        cwd = idf_dir,
                        stdout = subprocess.PIPE,
                        stderr = subprocess.PIPE,
                        preexec_fn=os.setsid)
	log_info_t = threading.Thread(target=_log_subprocess_info,
										args=(cvt_json_prcs.stdout,
											logger))
	log_err_t = threading.Thread(target=_log_subprocess_err,
										args=(cvt_json_prcs.stderr,
											logger))
	while _get_is_subprocess_running(cvt_json_prcs):
		pass

def run_eplus_model(eplus_run_path, idf_path, output_dir,
					weather_path=DEFAULT_WEAT_PATH):
	logger = Logger().getLogger('run_eplus_model', LOG_LEVEL, LOG_FMT)
	####################################################################
	# Create an EnergyPlus process 
	idf_dir = os.path.dirname(idf_path)
	eplus_run_script = f'{eplus_run_path} -w {weather_path} \
						-d {output_dir} -r {idf_path}'
	eplus_process = subprocess.Popen(eplus_run_script,
                        shell = True,
                        cwd = idf_dir,
                        stdout = subprocess.PIPE,
                        stderr = subprocess.PIPE,
                        preexec_fn=os.setsid)
	####################################################################
	# Prepare for the logging
	log_info_t = threading.Thread(target=_log_subprocess_info,
									args=(eplus_process.stdout, logger))
	log_err_t = threading.Thread(target=_log_subprocess_err,
									args=(eplus_process.stderr, logger))
	log_info_t.start()
	log_err_t.start()
	while _get_is_subprocess_running(eplus_process):
		pass

def _log_subprocess_info(out, logger):
	for line in iter(out.readline, b''):
		line = line.decode()
		logger.info(line)

def _log_subprocess_err(out, logger):
	for line in iter(out.readline, b''):
		logger.error(line.decode())

def _get_is_subprocess_running(subprocess):
	if subprocess.poll() is None:
		return True
	else:
		return False