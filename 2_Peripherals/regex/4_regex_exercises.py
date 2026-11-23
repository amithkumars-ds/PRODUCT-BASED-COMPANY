import re

text = """
NEFT202611230012
RTGS202611230013
IMPS202611230014
"""

pattern = r"\b(?:NEFT|RTGS|IMPS)\d{12}"
results = re.findall(pattern, text)
print(results)
