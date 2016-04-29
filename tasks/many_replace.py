


def many_replace():
    s, a, b = input(), input(), input()
    j = 0

    if a in b and a in s:
        return 'Impossible'

    while a in s:
        s = s.replace(a, b)
        j += 1
    else:
        return j

print(many_replace())

# put your python code here
# s, a, b = input(), input(), input()
# j = 0



# while a in s:
#     if a in b and a in s:
#         print('Impossible')
#         break
        
#     s = s.replace(a, b)
#     j += 1
# else:
#     print(j)