#!/usr/bin/python3
# 6-print_sorted_dictionary.py


def print_sorted_dictionary(a_dictionary):
    """Prints a dictionary by ordered keys"""
    [print("{}: {}".format(n, a_dictionary[n])) for n in sorted(a_dictionary)]
