import re
import pandas as pd

data = {
    "Date": ["23-11-2026", "24-11-2026", "25-11-2026"],
    "Reference": ["NEFT001", "RTGS002", "IMPS003"],
    "Debit": [25000, 0, 15000],
    "Credit": [0, 50000, 0]
}
df = pd.DataFrame(data)

debit_filter = df["Debit"] > 20000
print(f"Debit greater than 20000: \n {df[debit_filter]}")

credit_filter = df["Credit"] == 0
print(f"Zero Credit Transactions: \n {df[credit_filter]}")

ref_numbers = df[df["Reference"].str.startswith("NEFT")]
print(f"Reference Numbers: \n {ref_numbers}")

combined_filter = (df["Debit"] > 10000) & (df["Credit"] == 0)
print(f"Transactions with combined filter: \n {df[combined_filter]}")
