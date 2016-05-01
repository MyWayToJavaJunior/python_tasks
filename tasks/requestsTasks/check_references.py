import requests
import re

# a = 'https://stepic.org/media/attachments/lesson/24472/sample0.html'
# b = 'https://stepic.org/media/attachments/lesson/24472/sample2.html'
A, B = input().rstrip(), input().rstrip()
PATTERN = r'<a.*?href="(http[/\w.:-]+)">.*?</a>'


def get_url(pattern, text):
    return re.findall(pattern, text)


def res_url(a, b):
    res = requests.get(a)
    list_links = get_url(PATTERN, res.text)

    for link in list_links:
        second_link = requests.get(link)
        if second_link.status_code == 200:
            second_links = get_url(PATTERN, second_link.text)

            if b in second_links:
                return 'Yes'
            # for s_link in second_links:
            #     if s_link == b:
            #         return 'Yes'
    return 'No'

print(res_url(A, B))

