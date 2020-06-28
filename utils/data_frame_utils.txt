'''
Created on 30-Mar-2020

@author: knagatej
'''

import pandas as pd
from tzlocal import get_localzone
	tz = get_localzone()
from sklearn import preprocessing


class Data_Frame_Utils: 
    
    @staticmethod
    def convert_colnames_toupper(datadf):  
        datadf.columns = map(str.upper, datadf.columns)
        return datadf

    @staticmethod
    def convert_colnames_tolower(datadf):  
        datadf.columns = map(str.lower, datadf.columns)
        return datadf
    
    @staticmethod
    def get_df_from_csv(csv_file_name):
        datadf = pd.read_csv(csv_file_name)
        return Data_Frame_Utils.convert_colnames_toupper(datadf)
    
    @staticmethod
    def add_column_to_df_with_given_value(inputdf, colname, value):
        inputdf[colname] = value if colname not in inputdf.columns else inputdf
        return inputdf 
    
    @staticmethod
    def merge_df_from_file_paths(comma_seperated_file_path):
        path_list = comma_seperated_file_path.split(",")
        combined_data_df = pd.concat([Data_Frame_Utils.get_df_from_csv(f) for f in path_list]).reset_index(drop=True)
        return Data_Frame_Utils.convert_colnames_toupper(combined_data_df)

    @staticmethod
    def merge_df_from_dfs(dataDf, dataDf1, key, how="inner"):
        return pd.merge(dataDf, dataDf1, on=key, how=how)

    @staticmethod
    def date_to_datetime(date):
        return tz.localize(pd.to_datetime(date), is_dst=None)

    @staticmethod
    def convert_date_to_datetime(df, column_name):
        try:
            df[column_name] = df[column_name].apply(Data_Frame_Utils.date_to_datetime)
        except:
            pass

	def overwrite_outliers(df):
		limit_qunatile_value = df.quantile(.95)
		outliers_high = (df > limit_qunatile_value)
		return df.mask(outliers_high, limit_qunatile_value, axis=1)


	def do_scaling_df(dataDf):
		x_scaled = do_scaling_series(dataDf)
		return pd.DataFrame(x_scaled)


	def do_scaling_series(dataDf):
		x = dataDf.values
		min_max_scaler = preprocessing.MinMaxScaler()
		return min_max_scaler.fit_transform(x)
