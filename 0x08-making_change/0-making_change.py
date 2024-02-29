#!/usr/bin/python3
"""Making Change Module"""


def makeChange(coins, total):
    """Function that determines the fewest number of
    coins needed to meet a given amount total.
    If the total cannot be met, return -1."""
    dp = [total + 1] * (total + 1)  # Initialize with impossible values
    dp[0] = 0  # Making 0 needs 0 coins

    for i in range(1, total + 1):
        for coin in coins:
            remaining = i - coin
            if remaining >= 0 and dp[remaining] != -1:
                dp[i] = min(dp[i], dp[remaining] + 1)

    return dp[total] if dp[total] != total + 1 else -1
