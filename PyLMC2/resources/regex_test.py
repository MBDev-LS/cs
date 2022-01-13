import regex

import re

print(re.match(r"[A-Z]{3}\sR[0-9]{1,2},\s?([0-9]{1,3})", 'LDR R0, 99'))
print(re.search(r"'([0-9]{1,3})'", 'LDR R0, 99'))
print(re.findall(r"[A-Z]{3}\sR[0-9]{1,2},\s?[0-9]{1,3}", 'LDR R0, 99'))

print(re.findall(r"\s?[A-Z]{3}", 'LDR R0, 99'))