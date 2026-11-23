import re

text = """
Account Number: 123456789O12
Reference Number: NEFT2026I1230012
Amount: INR 25,5OO.OO
"""

pattern = r"Account\s*Number:\s*([A-Z0-9]{12})"
acc_num = re.findall(pattern, text)
corrected = acc_num[0].replace("O","0")

valid = bool(re.fullmatch(r"\d{12}", corrected))
print("acc number: ", corrected)
print("acc number valid - ", valid)
