#!/usr/bin/python3

# Given a string, you have to return a string in which each character (case-sensitive) is repeated once.
#
# double_char("String") ==&gt; "SSttrriinngg"
#
# double_char("Hello World") ==&gt; "HHeelllloo  WWoorrlldd"
#
# double_char("1234!_ ") ==&gt; "11223344!!__  "


def double_char(string):
    result = []

    for letter in string:
        
        result.append(letter)
        result.append(letter)

    return ''.join(result)

print(double_char('String'))
print(double_char('Hello World'))
print(double_char('1234!_ '))
