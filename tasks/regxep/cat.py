import sys
import re

pattern = r'cat'
string = ['catcat', 'cat and cat', 'catac', 'cat', 'ccaatt']
for line in string:
    # line = line.rstrip()
    r = re.findall(pattern, line)
    if len(r) > 1:
        print(line)
