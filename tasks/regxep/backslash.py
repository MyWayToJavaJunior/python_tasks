import sys
import re

pattern = r'\\'
string = ['\w denotes word character', 'No slashes here']

for line in string:
    if re.findall(pattern, line):
        print(line)