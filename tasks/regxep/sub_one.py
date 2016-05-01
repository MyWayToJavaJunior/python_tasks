import sys
import re

string = ['attraction',
          'buzzzz']

for line in string:

    line = re.sub(r'(\w)\1+', r'\1', line)
    print(line)
