#!/usr/bin/python3
"""Minimum Operations Module"""


def minOperations(n):
    """Minimum Operations"""
    if n <= 1:
        return 0
    else:
        i = 2
        num = n
        op = 0
        while i <= num:
            if num % i == 0:
                op += i
                num /= i
            else:
                i += 1
        return op
