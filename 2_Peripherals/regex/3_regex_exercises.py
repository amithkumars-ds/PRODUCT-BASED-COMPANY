# Suppose OCR/PDF extraction gives you this text,

# Transaction Date: 23-11-2026
# Reference No: NEFT202611230012
# Debit Amount: INR 25,500.00
# Credit Amount: INR 0.00
# Account Number: 123456789012

# extract all five fields using Python Regex.

text = """
Transaction Date: 23-11-2026
Reference No: NEFT202611230012
Debit Amount: INR 25,500.00
Credit Amount: INR 0.00
Account Number: 123456789012
"""

import re
date = re.findall(r"\d{2}-\d{2}-\d{4}", text)
ref_number = re.findall(r"\bNEFT\d{12}\b", text)
amounts = re.findall(r"[\d,]+\.\d{2}", text)
account_number = re.findall(r"\b\d{12}\b", text)

print("date: ", date)
print("reference number: ", ref_number)
print("amounts: ", amounts)
print("account number: ", account_number)
