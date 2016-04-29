#
# with reversed(list(open('dataset_24465_4.txt'))) as f:
#     for line in f:
#         # w.write(line.rstrip())
#         print(line)

w = open('out.txt', 'w')

for line in reversed(list(open('dataset_24465_4.txt'))):
    w.write(line)

w.close()