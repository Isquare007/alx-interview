#!/usr/bin/python3
"""making_change"""


def makeChange(coins, total):
    """Given a pile of coins of different values, determine the
    fewest number of coins needed to meet a given amount total.
    """
    if total <= 0:
        return 0

    dp = [total + 1] * (total + 1)
    dp[0] = 0

    for t in range(1, total + 1):
        for c in coins:
            if c <= t:
                dp[t] = min(dp[t], 1 + dp[t - c])

    return dp[total] if dp[total] != total + 1 else -1
