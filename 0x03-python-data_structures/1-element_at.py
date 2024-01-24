#!/usr/bin/python3
# 1-element_at.py


def element_at(my_list, idx):
    if idx > 0 and idx < len(my_list):
        return my_list[idx]
    else:
        return None
    
my_list = [1, 2, 3, -4, 5]
idx = 3
element_at(my_list, idx)
print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))
