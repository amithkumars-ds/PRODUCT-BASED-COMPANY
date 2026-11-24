import pandas as pd

bank_a = pd.DataFrame({
    "Reference": ["NEFT001", "RTGS002"],
    "Debit": [25000, 0],
    "Credit": [0, 50000]
})

bank_b = pd.DataFrame({
    "Reference": ["IMPS003", "NEFT004"],
    "Debit": [15000, 10000],
    "Credit": [0, 0]
})

combined_df = pd.concat([bank_a,bank_b], ignore_index=True)
print(combined_df)

print(f"\nTotal Debit: {combined_df.Debit.sum()}")
print(f"Total Credit: {combined_df.Credit.sum()}")
print("\nRemoving duplicates based on ref numbers...")

combined_df = combined_df.drop_duplicates(subset=["Reference"])
print("\nFinal DataFrame\n")
print(combined_df)


