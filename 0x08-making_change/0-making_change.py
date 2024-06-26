#!/usr/bin/python3
"""Making Change Module"""


def makeChange(coins, total):
    """determines the fewest number of coins
    needed to meet a given amount
    """
    if total <= 0:
        return 0

    remainder = total
    coins_count = 0
    coin_idx = 0

    # sorts the list of coins in descending order to always
    # try using the largest coin first.
    sorted_coins = sorted(coins, reverse=True)
    n = len(coins)

    while remainder > 0:
        if coin_idx >= n:
            return -1
        if remainder - sorted_coins[coin_idx] >= 0:
            remainder -= sorted_coins[coin_idx]
            coins_count += 1
        else:
            coin_idx += 1

    return coins_count
