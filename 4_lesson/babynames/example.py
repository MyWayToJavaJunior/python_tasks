import os
import sys
import re


def extract_names(filename):
    f = open(filename, 'r')

    table = re.findall(r'''
           <tr>\s*?
                <td(\w+\d+)?>(.*?)</td>\s*?
                <td(\w+\d+)?>(.*?)</td>\s*?
                <td(\w+\d+)?>(.*?)</td>\s*?
                <td(\w+\d+)?>(.*?)</td>\s*?
                <td(\w+\d+)?>(.*?)</td>\s*?
                <td(\w+\d+)?>(.*?)</td>\s*?
                <td(\w+\d+)?>(.*?)</td>\s*?
           </tr>\s*?

        ''',
    f.read(), re.DOTALL | re.VERBOSE)
    return table

print(extract_names('babynames_girls.html'))