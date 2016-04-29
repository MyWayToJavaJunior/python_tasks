

s, t = input(), input()

count_t = 0
index = 0
while index != -1:
    index = s.find(t, index + 1)
    count_t += 1
print(count_t)    
# while not (s.find(t, index) == -1):
#     index = s.find(t, index)
#     count_t += 1
# print(count_t)