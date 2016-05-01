import sys
import re

string = ['I need to understand the human mind',
          'humanity']

for line in string:

    line = re.sub('human', 'computer', line)
    print(line)
