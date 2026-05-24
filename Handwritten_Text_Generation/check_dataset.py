import pandas as pd

df = pd.read_parquet("datasets/train-00000-of-00001.parquet")

print(df.head())
print(df.columns)