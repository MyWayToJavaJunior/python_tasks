

# f = open('test.txt', 'r')
#
# for line in f:
#     line = line.rstrip()
#     print(repr(line))
#
# x = f.read()
# print(repr(line))
#
#
# f.close()


# write

# f = open('text1.txt', 'w')
# lines = ['line1', 'line2', 'line3']
# contents = '\n'.join(lines)
# f.write(contents)
#
# f.close()


# with - сам закрывает

with open('test.txt') as f, open('test_copy.txt', 'w') as w:
    for line in f:
        w.write(line)