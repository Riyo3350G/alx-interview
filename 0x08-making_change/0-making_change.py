#!/usr/bin/python3
"""Making Change Module"""


def makeChange(coins, total):
    """Function that determines the fewest number of
    coins needed to meet a given amount total.
    If the total cannot be met, return -1."""
    if total <= 0:
        return 0

    # Initialize an array to store the minimum number of coins for each amount
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins needed to make change for 0

    # Iterate through each coin value
    for coin in coins:
        # Update dp array for each amount from coin value to total
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
