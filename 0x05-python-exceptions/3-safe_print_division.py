#!/usr/bin/python3
# 3-safe_print_division.py
# CCC


def safe_print_division(a, b):
    '''divides 2 integers and prints the result.'''
    try:
        quo = a / b
    except (ZeroDivisionError, TypeError):
        quo = None
    finally:
        print("Inside result: {}".format(quo))
    return quo
