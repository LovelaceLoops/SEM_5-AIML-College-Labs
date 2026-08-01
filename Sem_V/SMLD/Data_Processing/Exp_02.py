import pandas as pd
from sklearn.preprocessing import StandardScaler,LabelEncoder

data = pd.read_csv("test.csv")
print(data)
print(data.columns)

#Find the Total missing values in the Age column
print(f"Total missing values = {data["Age"].isnull().sum()}")

#Fill the missing rows with Mean of the column
data["Age"] = data["Age"].fillna(data["Age"].mean())
print(f"New number of missing values = {data["Age"].isnull().sum()}")

#Perfome scalling on the age column 
scalar = StandardScaler()
data["Age_Scaled"] = scalar.fit_transform(data[["Age"]])
print(f"Scaled age = {data["Age_Scaled"]}")

#Perform encoding on Sex column
le = LabelEncoder()
data["Sex_Encoded"] = le.fit_transform(data[["Sex"]])
print(f"Encoded gender = {data["Sex_Encoded"]}")

#Outlier detection
Q1 = data['Age'].quantile(0.25)
Q3 = data['Age'].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers = data[(data['Age'] < lower_bound) | (data['Age'] > upper_bound)]
print(f"Age outliers = {outliers["Age"]}")
