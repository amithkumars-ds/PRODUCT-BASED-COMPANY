# BANK STATEMENT

# Account Number: 123456789012
# Transaction Date: 23-11-2026
# Reference Number: NEFT20261123001234
# Amount: INR 125,500.00
# Beneficiary: ABC Technologies Pvt Ltd


# You need to extract:
# - Account number
# - Transaction date
# - Reference number
# - Amount
# - Beneficiary


input_string = """# BANK STATEMENT

                # Account Number: 123456789012
                # Transaction Date: 23-11-2026
                # Reference Number: NEFT20261123001234
                # Amount: INR 125,500.00
                # Beneficiary: ABC Technologies Pvt Ltd"""


import re

# TASK 1
account_number = re.findall(r"\d{12}",input_string)
transaction_date = re.findall(r"\d{2}-\d{2}-\d{4}", input_string)
reference_number = re.findall(r"NEFT\d{14}", input_string)
amount = re.findall(r"\d+\.\d{2}", input_string)
beneficiary = re.findall(r"Beneficiary:\s*(.+)", input_string)

# print(account_number)
# print(transaction_date)
# print(reference_number)
# print(amount)
# print(beneficiary)


# TASK 2: Extract only the NEFT reference number.
input_string = """
Reference: NEFT20261115001234
Previous Reference: RTGS20261115005678
Payment Reference: IMPS20261115009999
"""

pattern = r"NEFT\d{14}"
neft_ref_number = re.findall(pattern, input_string)
# print(neft_ref_number)


# TASK 3: A realistic Treasury extraction problem
# Find both amounts
document = """
Transaction 1:
Date: 15-11-2026
Amount: INR 87,500.50
Reference: NEFT20261115001234

Transaction 2:
Date: 16-11-2026
Amount: INR 1,25,000.00
Reference: NEFT20261116005678
"""

pattern = r"Amount:\s*INR\s* ([\d,]+\.+\d{2})"
amount = re.findall(pattern, document)
# print(amount)


# TASK 4
input_string = """
                Amount: INR 87,500.50
                Amount: USD 1250.00
                Amount: EUR 950.75
                Amount: INR 500"""
pattern = r"Amount:\s*(INR|USD|EUR)\s*([\d,]+(?:\.\d{2})?)"
results = re.findall(pattern,input_string)
# print(results)


# TASK 5
# Extract,
# 1. All transaction dates.
# 2. All amounts.
# 3. All NEFT reference numbers.

import re

document = """
Transaction 1:
Date: 15-11-2026
Amount: INR 87,500.50
Reference: NEFT20261115001234

Transaction 2:
Date: 16-11-2026
Amount: INR 1,25,000.00
Reference: NEFT20261116005678
"""

transaction_dates = re.findall(r"\d{2}-\d{2}-\d{4}", document)
amounts = re.findall(r"Amount:\s*INR\s*([\d,]+\.\d{2})", document)
reference_numbers = re.findall(r"NEFT\d+", document)

print(transaction_dates)
print(amounts)
print(reference_numbers)
