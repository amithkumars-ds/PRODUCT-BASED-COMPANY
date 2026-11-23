import re

accounts = [
    "123456789012",
    "12345678901",
    "1234567890123",
    "12345ABC9012",
    " 123456789012 "
]

pattern = r"\b\d{12}\b"
for acc_num in accounts:
   result = re.fullmatch(pattern, acc_num)
   result_bool = bool(result)
   print(f"Account number: {acc_num}-{result_bool}")
