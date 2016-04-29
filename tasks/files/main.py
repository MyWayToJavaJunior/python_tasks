import os
import re
import os.path


# '.+\.py$'
# [a-zA-Z0-9_-]*.py
lst = []
mask = re.compile(r'.+\.py$')
for current_dir, dirs, files in os.walk('./main'):
    if mask.search(' '.join(files)):
        r = mask.search(' '.join(files))
        lst.append(os.path.abspath(current_dir)[38:])


lst.sort()
f = open('resultFindPy', 'w')
contents = '\n'.join(lst)
f.write(contents)
