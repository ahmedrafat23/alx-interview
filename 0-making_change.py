#!/usr/bin/python3

def makeChange(coins, total):
    """
    Determine the minimum number of coins needed to achieve the total.
    :param coins: List of coin denominations
    :param total: Target total amount
    :return: Minimum number of coins needed or -1 if impossible
    """
    # If total is 0 or less, no coins are needed
    if total <= 0:
        return 0

    # Initialize dp array with a very large number
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins are needed to make total 0

    # Loop through each coin
    for coin in coins:
        for amount in range(coin, total + 1):
            # Update dp[amount] with the minimum coins needed
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # If dp[total] is still float('inf'), it means it's impossible to make the total
    return dp[total] if dp[total] != float('inf') else -1
