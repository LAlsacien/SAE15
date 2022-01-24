import pandas as pd
import glob
import os

fichiers_csv = glob.glob('raw/sending*.csv')
raw_liste = []
for file in fichiers_csv:
    raw_liste.append(pd.read_csv(file))

df = pd.concat(raw_liste, axis=0, sort=True)
df.to_csv('raw/resultat2.csv',index=False)