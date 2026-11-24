import re

text = "NEFT2026I1230012"

pattern = r"NEFT(.{12})"
result_before = re.findall(pattern,text)
valid_num_before = bool(re.fullmatch(r"\d{12}",text))

text = text.replace("I","1")
valid_num_after = bool(re.fullmatch(r"\d{12}",text))
result_after = re.findall(pattern,text)

print(f"Validation before correction: {valid_num_before}")
print(f"Result: {result_before}")
print(f"Validation after correction: {valid_num_after}")
print(f"Result: {result_after}")
