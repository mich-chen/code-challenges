from typing import List

def maxProfit(prices: List[int]) -> int:

    if not prices:
        return 0

    maxprofit = 0
    minprice = max(prices)

    for price in prices:
        if price < minprice:
            minprice = price
        maxprofit = max(maxprofit, price - minprice)

    return maxprofit

def maxProfit_ii(prices: List[int]) -> int:
    # base case
    if len(prices) == 1:
        return 0

    prices.append(0)
    profit = 0
    buy = prices[0]

    # iterate through prices
    # only update when previous day is greater than current day's price
    for day, price in enumerate(prices):
        if prices[day - 1] > price:
            # this means need to reset buy price
            # and calculate gains from yesterday's sell price subtract whatever was previous buy
            profit += prices[day - 1] - buy
            buy = price
    return profit


if __name__ == '__main__':

    print(maxProfit([7, 1, 5, 3, 6, 4])) # 5
    print(maxProfit([7, 6, 4, 3, 1])) # 0
    print(maxProfit_ii([7, 1, 5, 3, 6, 4])) # 7
