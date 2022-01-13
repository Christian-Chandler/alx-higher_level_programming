#!/usr/bin/python3
# 2-uniq_add.py


def uniq_add(my_list=[]):
    """Add all unique integers in a list (once for each integer)."""
    sum = 0
    new_list = set(my_list)
    for z in new_list:
        sum = sum + z
    return (sum)
