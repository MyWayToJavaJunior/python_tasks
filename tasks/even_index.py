#!/usr/bin/python3


def even_index(list):
    max_even = max(x for i, x in enumerate(list) if (i+1) % 2 == 0)
    min_uneven = min(x for i, x in enumerate(list) if not (i+1) % 2 == 0)
    return max_even + min_uneven
    
    
print(even_index([1, -2, 3, -4, 5]))