import requests
import re

link = input().rstrip()

PATTERN_HREF = r'<a.*?href=[\'\"]([^\"]+?)[\'\"].*?>'
PATTERN_ONLY_HOST = r'([\w.-]+)'
PATTERN_HOST = r'[\w]+://([\w.-]+)'
PATTERN_PROTOCOL = r'[\w]+://'


# with open('02.html', 'r', encoding='windows-1251') as f:
#     text = f.read()
#     list_link = re.findall(PATTERN_HREF, text)

html = requests.get(link).text
list_link = re.findall(PATTERN_HREF, html)

print(html)
print(list_link)

res = []
for link in list_link:
    if link.startswith('../'):
        continue
    elif re.match(PATTERN_PROTOCOL, link):
        selected_link = re.search(PATTERN_HOST, link).group(1)
        if selected_link not in res:
            res.append(selected_link)
    else:
        selected_link = re.search(PATTERN_ONLY_HOST, link).group(1)
        if selected_link not in res:
            res.append(selected_link)

res.sort()

print(res)

# z = open('t.html', 'r')
# s = z.read().split()
# print(s)

