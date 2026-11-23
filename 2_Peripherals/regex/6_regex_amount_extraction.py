import re

text = """
INR 25000
INR 25,000
INR 25,000.00
INR 25000.00
"""

pattern = r"INR\s*([\d,]+(?:\.\d{2})?)"
result = re.findall(pattern, text)
print(result)
