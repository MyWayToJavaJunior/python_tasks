import sys
import re

pattern = r'.*?\bcat\b.*?'
string = ['cat', 'catapult and cat', 'catac', 'concat', 'Cat', '"cat"', '!cat?']

for line in string:
    # line = line.rstrip()
    if re.match(pattern, line):
        print(line)
