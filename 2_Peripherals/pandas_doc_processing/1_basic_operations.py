import pandas as pd

data = {
    "Date": ["23-11-2026", "24-11-2026", "25-11-2026"],
    "Reference": ["NEFT001", "RTGS002", "IMPS003"],
    "Debit": [25000, 0, 15000],
    "Credit": [0, 50000, 0]
}

df = pd.DataFrame(data)

# print(df)

print("Reference number: \n", df["Reference"].values) # print reference column
print("Total Debit: ", df["Debit"].sum()) # print total debit
print("Total Credit: ", df["Credit"].sum()) # print total credit
print(f"Total rows: {df.shape[0]}, columns: {df.shape[1]}")
