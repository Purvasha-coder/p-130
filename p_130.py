from os import access
import pandas as pd
import csv

df = pd.read_csv("merged_data.csv")
print(df.shape)

del df["Luminosity"] 
del df["Star_names"]
del df["Distance"]
del df["Mass"]
del df["Radius"]


print(df.shape)
print(list(df))


df.to_csv("cleaned_data.csv")
