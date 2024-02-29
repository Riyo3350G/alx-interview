#!/usr/bin/python3
"""Making Change Module"""


def makeChange(coins, total):
    """Function that determines the fewest number of
    coins needed to meet a given amount total.
    If the total cannot be met, return -1."""
    if not coins or coins is None:
        return -1
    if total <= 0:
        return 0
    change = 0
    coins = sorted(coins)[::-1]
    for coin in coins:
        while coin <= total:
            total -= coin
            change += 1
        if (total == 0):
            return change
    return -1
