# ===============================================================
# **************************************************************
# **************************************************************
class Field:
	def __init__(self):
		pass

    # ===========================================================
	# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	# Aux Functions:
	@staticmethod
	def save_local():
		pass

    # ===========================================================
	# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	# Aux Functions:
	@staticmethod
	def url2pd(csv_url):
		import pandas as pd
		
		columns_name = ['A','B','C','D','E','F','G','H','I','J','K','L','M']
		return pd.read_csv(csv_url, names=columns_name)

	@staticmethod
	def url2np(csv_url):
		return Field.pd2np(Field.url2pd(csv_url))

	@staticmethod
	def pd2np(pd_frame):
		return -pd_frame.values
	
	@staticmethod
	def np_interpolate(np_array, ratio):
		import numpy as np
		from scipy import interpolate

		X = np.arange(0, 13, 1)
		Y = np.arange(0, 13, 1)
		X, Y = np.meshgrid(X, Y)

		Z = np_array

		# ------------------------------------------------------------------------------
		# Interpolation
		tck = interpolate.bisplrep(X, Y, Z, s=2500)

		ratio = 10

		X_interp = np.arange(0, 13, 1/ratio)
		Y_interp = np.arange(0, 13, 1/ratio)

		X_interp, Y_interp = np.mgrid[0:13:ratio*13j, 0:13:ratio*13j]

		return interpolate.bisplev(X_interp[:,0], Y_interp[0,:], tck)

	# ===========================================================
	# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++	
	@staticmethod
	def field_dir_example():
		data_dict = {
		    'URL':  'https://raw.githubusercontent.com/lsmanoel/CEM_4/master/python_aux/data/data.csv',
		    'LOCAL': './data/data.csv'
		}

		info_dict = {
		    'URL':  'https://raw.githubusercontent.com/lsmanoel/CEM_4/master/python_aux/info/info.csv',
		    'LOCAL': './info/info.csv'
		}
				
		photo_dict = {
		    'URL':  'https://raw.githubusercontent.com/lsmanoel/CEM_4/master/python_aux/photo/info.csv',
		    'LOCAL': './photo/photo.csv'
		}
		
		field_dir = {
			'data': data_dict,
			'info': info_dict, 
		    'photo': photo_dict
		}

		return field_dir

	@staticmethod
	def field_example():
		data_dict = {
		    'URL':  'https://raw.githubusercontent.com/lsmanoel/CEM_4/master/python_aux/data/placaL_medidas%20-%20%20plane_bottom_24_MHz.csv',
		    'LOCAL': None
		}

		info_dict = {
		    'URL':   None,
		    'LOCAL':  None
		}
				
		photo_dict = {
		    'URL':   None,
		    'LOCAL':  None
		}
		
		field = {
			'data': data_dict,
			'info': info_dict, 
		    'photo': photo_dict
		}

		return field

	# ===========================================================
	# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	@staticmethod
	def testbeach(field):
		print('Pandas Data Frame:\n')
		print(Field.url2pd(field['data']['URL']))
		print('\n')

	@staticmethod
	def test_url_csv(url_csv):
		print('Pandas Data Frame:\n')
		print(Field.url2pd(url_csv))
		print('\n')

	@staticmethod
	def test_field_data_shape(field, shape=(13, 13)):
		if Field.url2np(field['data']['URL']).shape == shape:
			return field
		else:
			print('Test Field Data Format:\n')
			print("\tError: invalid shape: ", Field.url2np(field['data']['URL']).shape)
			print('\t\tdata shape for this experiment must be ', shape)


# ===============================================================
# **************************************************************
# **************************************************************
Field.testbeach(Field.test_field_data_shape(Field.field_example()))
