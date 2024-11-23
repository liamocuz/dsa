#pylint: disable=all

"""
Leetcode 322
"""

from functools import lru_cache


def dfs_coin_change(coins: list[int], amount: int) -> int:
    """
    Performs a brute-force DFS implementation to find the min coin amount.
    This is a Top-Down implementation because it starts with the amount and builds down a
    recursive tree to find the min.
    """

    MAX: int = amount + 1

    def dfs(current_amount: int) -> int:
        # If we've reached 0, then we have found a valid sequence of coins
        # This is also the base case
        if current_amount == 0:
            return 0
        # We can return a level early
        # This can be negative when a level returns -1, and then the final check at the very end of
        # the recursion can turn the value MAX into -1
        if current_amount < 0:
            return MAX
        
        min_coins: int = MAX
        for coin in coins:
            # Only want to check for coins that won't go negative
            if current_amount - coin >= 0:
                resulting_coins: int = dfs(current_amount - coin)

                min_coins = min(min_coins, resulting_coins + 1)
        
        return min_coins if min_coins != MAX else -1
    
    return dfs(amount)

def fast_dfs_coin_change(coins: list[int], amount: int) -> int:
    """
    This is the same as the above function, except is uses an lru_cache
    to act as a memoization helper
    """

    MAX: int = amount + 1

    @lru_cache()
    def dfs(current_amount: int) -> int:
        # If we've reached 0, then we have found a valid sequence of coins
        # This is also the base case
        if current_amount == 0:
            return 0
        # We can return a level early
        # This can be negative when a level returns -1, and then the final check at the very end of
        # the recursion can turn the value MAX into -1
        if current_amount < 0:
            return MAX
        
        min_coins: int = MAX
        for coin in coins:
            # Only want to check for coins that won't go negative
            if current_amount - coin >= 0:
                resulting_coins: int = dfs(current_amount - coin)

                min_coins = min(min_coins, resulting_coins + 1)
        
        return min_coins if min_coins != MAX else -1
    
    return dfs(amount)
    

def memoized_dfs_coin_change(coins: list[int], amount: int) -> int:
    """
    This is the same as the above function, except is uses an lru_cache
    to act as a memoization helper
    """

    MAX: int = amount + 1
    memo: dict[int, int] = {}

    def dfs(current_amount: int) -> int:
        # If we've reached 0, then we have found a valid sequence of coins
        # This is also the base case
        if current_amount == 0:
            return 0

        # We can return a level early
        # This can be negative when a level returns -1, and then the final check at the very end of
        # the recursion can turn the value MAX into -1
        if current_amount < 0:
            return MAX

        if current_amount in memo:
            return memo[current_amount]
        
        min_coins: int = MAX
        for coin in coins:
            # Only want to check for coins that won't go negative
            if current_amount - coin >= 0:
                resulting_coins: int = dfs(current_amount - coin)

                min_coins = min(min_coins, resulting_coins + 1)
        
        memo[current_amount] = min_coins
        return min_coins if min_coins != MAX else -1
    
    return dfs(amount)

def bu_dp_coin_change(coins: list[int], amount: int) -> int:
    """
    Bottom Up Dynamic Programming coin change

    Given a list of coins of a certain denomination and an amount,
    find the smallest amount of coins out of the list that equals
    that amount.
    Assume you have an infinite amount of each coin.
    """
    # Idea: Perform Bottom-Up DP
    #   Create a tabulation for every amount from 0 to amount, where every starting amount
    #   is equal to amount + 1 since that is the max and we want to find mins.
    #   This table represents the minimum amount of coins needed for each amount at each step.
    #   The base case table[0] = 0 because to make an amount of 0, 0 coins are needed.
    #   Loop through all amounts from 1 to amount, and then through each coin

    #   If the coin value can fit into the current amount, find the minimum
    #   of one of those coins + the value at table[current_amount - coin_value] and the current_amount.
    #   Otherwise, the coin cannot fit into the current amount and so we move on.
    #   This will automatically find the minimum amount of coins at each amount.

    # Time: O(len(coins) * amount)
        # For each amount, loop over all coins
    # Space: O(amount)
        # Maintain a table of length amount + 1

    # amount + 1 will be the max for all combinations
    # essentially can only be an amount count of 1 coins as a max, so nothing will go 1 above that
    dp: list[int] = [amount + 1] * (amount + 1)

    # base case: amount of 0 can only be made with 0 coins
    dp[0] = 0

    for current_amount in range(1, amount + 1):
        for coin_val in coins:
            # If the current_amount is able to fit the current coin_val, then we can
            # calculate the current min number of coins given other previously computed values
            # plus 1 of the current coins
            if current_amount - coin_val >= 0:
                dp[current_amount] = min(dp[current_amount], 1 + dp[current_amount - coin_val])
    
    # The final min amount for the asked amount will be in the amount index of the table
    # But if the amount is equal to the defaulted max that can never be reached, which means
    # nothing minimum was ever found, that means we are unable to make the amount given the
    # coins, so we return -1
    return dp[amount] if dp[amount] != (amount + 1) else -1


if __name__ == "__main__":
    coins: list[int] = [1, 2, 5]
    amount: int = 11

    print(bu_dp_coin_change(coins, amount))
    assert(bu_dp_coin_change(coins, amount) == 3)

    # This is fine for small amounts of coins, but gets SUPER slow for larger amounts
    print(dfs_coin_change(coins, amount))

    # This will take so long
    coins_slow = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    amount_slow = 120
    # print(dfs_coin_change(coins_slow, amount_slow))

    # This will not take long as it uses the lru_cache to memoize
    coins_slow = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    amount_slow = 120
    print(fast_dfs_coin_change(coins_slow, amount_slow))

    # We can use the memoized version with a dict too to speed it up significantly
    coins_slow = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    amount_slow = 120
    print(memoized_dfs_coin_change(coins_slow, amount_slow))
