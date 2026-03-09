import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("city_day.csv")
print(df.shape)
df.head()
df.tail()

df.info()
print(df.columns)
df.isnull().sum()
df.describe()
# Remove duplicate rows
duplicates = df.duplicated().sum()
print("Duplicate rows:", duplicates)

df = df.drop_duplicates()

# Check dataset structure
print(df.info())

df.to_csv("processed_data.csv", index=False)