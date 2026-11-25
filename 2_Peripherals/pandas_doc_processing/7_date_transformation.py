import pandas as pd

data = {
    "Date": ["23-11-2026", "24-11-2026", "25-11-2026"]
}

df = pd.DataFrame(data)

df["Date"] = pd.to_datetime(df["Date"], format="%d-%m-%Y")

print(df)
print(df.dtypes)

df["Years"] = df["Date"].dt.year 
df["Months"] = df["Date"].dt.month
df["Day"] = df["Date"].dt.day
print(df["Years"])
print(df["Months"])
print(df["Day"])

datetime_filter = df["Date"] > pd.Timestamp("23-11-2026")
print(df[datetime_filter])
