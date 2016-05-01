import re
import sys

pattern = r'.*?z.{3}z.*?'
string = ['zabcz', 'zzz', 'zzxzz', 'zz', 'zxz', 'zzxzxxz', '123zabcz456']

for line in string:
    # line = line.rstrip()
    if re.match(pattern, line):
        print(line)
