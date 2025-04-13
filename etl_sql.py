##Script de ingesta de SQL a DataLake
import pandas as pd

df = pd.read_csv('input.csv')
df['processed'] = df['value'] * 10
df.to_csv('output4.csv', index=False)
print("ETL completado.")
