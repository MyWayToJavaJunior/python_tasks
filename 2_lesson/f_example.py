f = open('example.txt', 'r', encoding='utf-8')

print(f.readline())

f.seek(0)

for s in f:
    print(s)


# f.write('timur\n')
# f.writelines(['safin\n', 'the\n', 'best\n', '!\n'])