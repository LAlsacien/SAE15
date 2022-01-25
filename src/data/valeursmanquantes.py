'''
import pandas as pd
import numpy as np
import glob
import os

df = pd.read_csv("resultat.csv")
colonne = df['Title']
print(colonne)
'''
import pandas as pd


df = pd.read_csv('resultat.csv')

percent_missing = df.isnull().sum() * 100 / len(df)

missing_value_df = pd.DataFrame({'nom_colum': df.columns,'percent_missing': percent_missing})
missing_value_df.sort_values('percent_missing', inplace=True)
print(missing_value_df)