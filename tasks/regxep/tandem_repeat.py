import sys
import re

pattern = r'\b(\w+)\1\b'
string = ['blabla is a tandem repetition',
          '123123 is good too',
          'go go',
          'aaa',
          'aaaa']

for line in string:
    if re.match(pattern, line):
        print(line)
