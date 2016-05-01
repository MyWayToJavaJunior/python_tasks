import sys
import re

string = ['There’ll be no more "Aaaaaaaaaaaaaaa"',
          'AaAaAaA AaAaAaA']

for line in string:
    line = line.rstrip()
    line = re.sub(r'\b[aA]+\b', 'argh', line, 1)
    print(line)
