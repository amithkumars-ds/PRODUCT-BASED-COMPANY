import pandas as pd

data = {
    "Reference": ["TXN001", "TXN002", None, "TXN004"],
    "Debit": [1000, 500, 200, None],
    "Credit": [None, None, 300, 1500]
}

df = pd.DataFrame(data)

print(df[df["Reference"].isna()])
print(df[df[["Debit","Credit"]].isna().all(axis=1)])
print("Total Debit: ",df["Debit"].sum())
print("Total Credit: ",df["Credit"].sum())

