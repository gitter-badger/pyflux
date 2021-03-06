import pandas as pd
import numpy as np

def data_check(data,target):
	""" Checks data type

	Parameters
	----------
	data : pd.DataFrame or np.array
		Field to specify the time series data that will be used.
	
	target : int or str
		Target column
		
	Returns
	----------
	transformed_data : np.array
		Raw data array for use in the model
		
	data_name : str
		Name of the data
	
	data_type : str (Change to Boolean in future)
		Whether numpy or pandas
	
	data_index : np.array
		The time indices for the data
	"""

	# Check pandas or numpy
	if isinstance(data, pd.DataFrame):
		data_index = data.index			
		if target is None:
			transformed_data = data.ix[:,0].values
			data_name = data.columns.values[0]
		else:
			transformed_data = data[target]			
			data_name = target					
		data_type = 'pandas'
		print str(data_name) + " picked as target variable"
		print ""
		
	elif isinstance(data, np.ndarray):
		data_name = "Series"		
		data_type = 'numpy'	
		if any(isinstance(i, np.ndarray) for i in data):
			if target is None:
				transformed_data = data[0]			
				data_index = range(len(data[0]))
			else:
				transformed_data = data[target]			
				data_index = range(len(data[target]))
			print "Nested list " + str(target) + " chosen as target variable"
			print ""
		else:
			transformed_data = data					
			data_index = range(len(data))
	else:
		raise Exception("The data input is not pandas or numpy compatible!")
	
	return transformed_data, data_name, data_type, data_index