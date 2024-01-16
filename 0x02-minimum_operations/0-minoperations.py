#!/usr/bin/python3
"""Minimum Operations Module"""


def minOperations(n):
    """Minimum Operations"""
    if n <= 1:
        return 0
    else:
        i = 2
        number = n
        operation = 0
        while i <= number:
            if number % i == 0:
                operation += i
                number /= i
            else:
                i += 1
        return operation
