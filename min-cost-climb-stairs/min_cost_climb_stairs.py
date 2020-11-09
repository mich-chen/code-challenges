from typing import List

def minCostClimbingStairs(cost: List[int]) -> int:

    for i in range(2, len(cost)):
        # cost of ith step + min cost between taking previous 1 or previous 2 steps
        cost[i] = cost[i] + min(cost[i-1], cost[i-2])

    return min(cost[-1], cost[-2])


if __name__ == '__main__':
    
    print(minCostClimbingStairs([10, 15, 20])) # 15
    print(minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))  # 6
