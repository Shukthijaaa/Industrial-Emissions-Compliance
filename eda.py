import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("processed_data.csv")

print("Dataset Shape:", df.shape)
print(df.info())
print(df.describe())