#Name: JJCHUEH and Yude Fu
#date 2023. 2. 16 
#this file is for OOP design for the cw

import sys,os
import pandas as pd
import numpy as np

from parametric_simulation import run_one_parameter_parametric

class simulation():
	def __init__(self,eplus_run_path,
						idf_path,
						output_dir):

		self.interval=0.02
		self.para_vals=[]
		self.eplus_run_path=eplus_run_path
		self.idf_path=idf_path
		self.output_dir=output_dir
		self._start_a = None
		self._end_a = None
		self._start_b = None
		self._end_b = None
		self._para_key_a=None
		self._para_key_b=None
		self._simulation_results=None


	#getter 
	@property
	def interval(self):
		return self._interval
	#setter
	@interval.setter
	def interval(self, new_interval):
		new_interval=float(new_interval)
		self._interval=new_interval

	#getter	
	@property
	def para_key_a(self):
		return self._para_key_a
	#setter
	@para_key_a.setter
	def para_key_a(self,new_para_key_a):
		self._para_key_a=new_para_key_a

	#getter	
	@property
	def para_key_b(self):
		return self._para_key_b
	#setter
	@para_key_b.setter
	def para_key_b(self, new_para_key_b):
		self._para_key_b = new_para_key_b

	#getter	
	@property
	def start_a(self):
		return self._start_a
	#setter
	@start_a.setter
	def start_a(self,new_start_a):
		new_start_a=float(new_start_a)
		self._start_a=new_start_a

	#getter	
	@property
	def start_b(self):
		return self._start_b
	#setter
	@start_b.setter
	def start_b(self,new_start_b):
		new_start_b=float(new_start_b)
		self._start_b=new_start_b

	#getter	
	@property
	def end_a(self):
		return self._end_a
	#setter
	@end_a.setter
	def end_a(self,new_end_a):
		new_end_a=float(new_end_a)
		self._end_a=new_end_a

	#getter	
	@property
	def end_b(self):
		return self._end_b
	#setter
	@end_b.setter
	def end_b(self,new_end_b):
		new_end_b=float(new_end_b)
		self._end_b=new_end_b
		
	def simulation_results(self):		
		return self._simulation_results



	def run_simulation(self):
		para_vals_a= np.arange(self.start_a,self.end_a,self.interval)
		para_vals_b= np.arange(self.start_b,self.end_b,self.interval)

		result=run_one_parameter_parametric(self.eplus_run_path,self.idf_path,self.output_dir,
			self.para_key_a,para_vals_a,self.para_key_b,para_vals_b)

		out_dir={}

		for i in result.keys():
			table_df=pd.read_csv(result[i])
			temp_vals=table_df[self._plot_column_name].values()
			out_dir[i]=sum(temp_vals/len(temp_vals))
		
		self._simulation_results=out_dir

