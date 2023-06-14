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
        
        # Update the total
        total -= coin * coin_count
        
        # Check if the total has been reduced to 0
        if total == 0:
            break
    
    # If the total is not reduced to 0, it cannot be made with the given coins
    if total != 0:
        return -1  # Or any other appropriate value to indicate impossibility
    
    return count



# -----------------------_________---------------____________----------------_________----------

# def makeChange(coins, total):
#     """Given a pile of coins of different values, determine the
#     fewest number of coins needed to meet a given amount total.
#     """
#     if total <= 0:
#         return 0
    
#     # sets dp to a list length of total+1 each number is total+1
#     dp = [total + 1] * (total + 1)
#     # base case sets dp[0] to 0
#     dp[0] = 0

#     # A loop ranging through 1-total+1
#     for t in range(1, total + 1):
#         for c in coins:
#             #checks if the t - c is less or equal to 0
#             if t - c >= 0:
#                 #then sets dp[t] to the minimum value
#                 dp[t] = min(dp[t], 1 + dp[t - c])

#     return dp[total] if dp[total] != total + 1 else -1