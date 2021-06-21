import pandas as pd
import csv
df = pd.read_csv("Data_merged.csv")
print(df.columns)
print(df.shape)

df.drop(['Unnamed: 0', 'Unnamed: 6', 'Distance.1', 'Radius.1',
        'Mass.1', 'Star_name.1', ], axis=1, inplace=True)

df.to_csv("Refined_Data.csv")