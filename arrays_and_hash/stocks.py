# Given an array of stock priceses
# find maxProfit if you can buy or sell
# only once in given days

# -------------------------------------------
# Solution 1:
# Brute-force
#  for i in range(0, n):
#   for j in range(1, n):
#       cP = arr[j] - arr[i]
#           if cP > mP:
#                mP = cP
#
# return mP
# Runtime: O(n2)

def maxProfitOne(arr):
    """
    Returns maxProfit.
    Find 2 elements with maximum difference. Smallest should be on the left
    side.
        Runtime: O(n)
    Parameters:
        arr (list): Stock prices at the start of the day
    Returns:
        float: Maximum profit

    """
    if arr is None:
        return 0
    if len(arr) <= 1:
        return 0

    max_profit = 0
    cur_low = arr[0]
    for i in range(1, len(arr)):
        cur_profit = arr[i] - cur_low
        if cur_profit > max_profit:
            max_profit = cur_profit
        # end of if
        if arr[i] < cur_low:
            cur_low = arr[i]
        # end of if
    # end of for
    return max_profit

def maxProfitTwo(arr):
    """
        Change problem slightly. You want to know days as well as maxProfit.
    """
    if arr is None:
        return 0
    n = len(arr)
    if n <= 1:
        return 0
    i = 0
    while i < n-1:
        # Find local minima
        while (i < n -1) and (arr[i+1] <= arr[i]):
            i +=1
        if i == n - 1:
            break
        print(i)
        buy = i
        # Find local maxima for sell
        # Look back for local max, since it can be last index
        i += 1
        while (i < n) and (arr[i-1] <= arr[i]):
            i += 1
        # end of while
        sell = i -1
        profit = arr[sell] - arr[buy]
        print("Buy on: ", buy, "\tSell on:", sell, "\tProfit:", profit)
    # end of while



if __name__ == '__main__':
    price = [100, 180, 260, 310, 40, 535, 695]
    print(maxProfitTwo(price))
