import sys
import re

string = ['this is a text',
          '"this\' !is. ?n1ce,']

for line in string:
    r'(\w)(\w)'
    line = re.sub(r'\b(\w)(\w)', r'\2\1', line)
    print(line)
