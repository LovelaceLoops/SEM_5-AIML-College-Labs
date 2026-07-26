#Exploratory Data Analysis: descriptive stats, histograms, correlation matrix 

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("Dataset.csv")
print(data.head())

print(data.columns)

Mean_value = data["Balance"].mean()
print(f"Mean Value = {Mean_value}")

Median_value = data["Balance"].median()
print(f"Median Value = {Median_value}")

Mode_value = data["Balance"].mode()[0]
print(f"Mode Value = {Mode_value}")

plt.hist(data["Balance"],bins=20,color="pink")

plt.axvline(Mean_value, color="skyblue", linestyle="--", linewidth=2, label=f'Mean: {Mean_value}')
plt.axvline(Median_value, color="green", linestyle="--", linewidth=2, label=f'Mean: {Median_value}')
plt.axvline(Mode_value, color="yellow", linestyle="--", linewidth=2, label=f'Mean: {Mode_value}')

plt.title("Balance Distribution")
plt.xlabel("Balance")
plt.ylabel("Frequency")
plt.show()

corelation_matrix = data.corr(numeric_only=True)
print(corelation_matrix)
