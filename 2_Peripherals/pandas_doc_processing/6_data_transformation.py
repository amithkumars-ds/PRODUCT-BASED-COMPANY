import pandas as pd

data = {
    "Reference": ["NEFT001", "RTGS002", "IMPS003"],
    "Amount": ["25,000.00", "50,000.00", "15,000.00"]
}

df = pd.DataFrame(data)

df["Amount"] = pd.to_numeric(df["Amount"].str.replace(",",""),
                             errors="coerce")

print(df["Amount"])
