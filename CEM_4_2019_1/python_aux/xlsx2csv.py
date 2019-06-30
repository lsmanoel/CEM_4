import os
import glob
import pandas as pd

folder_path = "./"
search_path = glob.glob(os.path.join(folder_path, "*.xlsx"))
                        
for file_path in search_path:
	root, ext = os.path.splitext(file_path)
	data_xls = pd.read_excel(file_path, index_col=None)
	data_xls.to_csv(root + ".csv", encoding='utf-8')	
