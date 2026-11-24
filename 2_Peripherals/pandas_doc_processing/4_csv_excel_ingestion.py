import pandas as pd

data = {
    "Reference": ["NEFT001", "RTGS002", "IMPS003", "NEFT004"],
    "Debit": [25000, 0, 15000, 10000],
    "Credit": [0, 50000, 0, 0]
}

df = pd.DataFrame(data)

df.to_csv("../../docs/sample.csv", index=False) # exporting to csv
df.to_excel("../../docs/output.xlsx", 
            sheet_name="sheet1",
            index=False) # exporting to excel
print(f"Total Debit: {df.Debit.sum()}")
print(f"Total Credit: {df.Credit.sum()}")

df_new = pd.read_csv("../../docs/sample.csv")
print(df_new.head(2))

