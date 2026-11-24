import re
import pandas as pd

data = {
    "Reference": ["NEFT001", None, "IMPS003"],
    "Debit": [25000, None, 15000],
    "Credit": [0, 50000, None]
}

df = pd.DataFrame(data)

print("Checking for missing values in each column: \n")
print(df.isna().sum())

print("\nDisplaying columns with at least one missing value: \n")
print(df[df.isna().any(axis=1)])

print("\nReplacing NaN values in credit and debit with zero...")
df["Credit"] = df["Credit"].fillna(0)
df["Debit"] = df["Debit"].fillna(0)
print(df)

print("\nRemoving rows with no reference values...")
df = df.dropna(subset=["Reference"])
print(df)
