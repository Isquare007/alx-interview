#!/usr/bin/python3
"""making_change"""


def makeChange(coins, total):
    """Given a pile of coins of different values, determine the
    fewest number of coins needed to meet a given amount total.
    """
    coins.sort(reverse=True)

    # Initialize a counter for the number of coins needed
    count = 0

    # Iterate through each coin denomination
    for coin in coins:
        # Count the number of coins needed for the current denomination
        coin_count = total // coin
        count += coin_count

        # Update the remaining amount
        total -= coin * coin_count

        # Check if the amount has been reduced to 0
        if total == 0:
            break

    # If the amount is not reduced to 0, it cannot be made with the given coins
    if total != 0:
        return -1  # Or any other appropriate value to indicate impossibility

    return count
