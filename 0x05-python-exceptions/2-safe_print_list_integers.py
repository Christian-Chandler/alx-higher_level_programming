#!/usr/bin/python3
# 2-safe_print_list_integers.py
# CCC


def safe_print_list_integers(my_list=[], x=0):
    '''prints the first x elements of a list and only integers'''
    num_printed = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            num_printed += 1
        except (TypeError, ValueError):
            pass
    print("")
    return num_printed
