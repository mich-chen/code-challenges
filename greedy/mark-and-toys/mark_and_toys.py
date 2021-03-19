def maximumToys(prices, k):

    # first sort all the prices
    prices = sorted(prices)
    # maximize most num of toys by buying cheapest toys until reach budget
    max_toys = 0
    current_sum = 0

    for price in prices:
        # check if adding this current toy would exceed our budget
        # backtracking / early exit of function
        if current_sum + price > k:
            return max_toys
        # check if toy exceeds budget, and if current sum of toys is under budget
        if price < k and current_sum <= k:
            max_toys += 1
            current_sum += price
   
    return max_toys

if __name__ == '__main__':
    
    print(maximizeToys([1,12,5,111,200,1000,10], 50))  # 4
       
