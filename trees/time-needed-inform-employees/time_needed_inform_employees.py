from typing import List
from collections import defaultdict

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        # dict to represent tree, keys is employees, values is subordinates
        tree = defaultdict(list)
        for i in range(len(manager)):
            tree[manager[i]].append(i)
            # leaves of tree will not be added to dict tree

        # dfs to calculate and add time
        def dfs(employee, tree):
            # employee is index of arrays
            time = informTime[employee]
            subordinates = tree[employee]
            # leaves of tree not in dict tree, therefore do not traverse further
            if time == 0:
                return time
            
            sub_time = 0
            for sub in subordinates:
                # add the max inform time from all subordinates
                sub_time = max(sub_time, dfs(sub, tree))

            return time + sub_time
        
        result = 0 
        result += dfs(headID, tree)
        print(result)
        return result

if __name__ == '__main__':

    examples = Solution()
    examples.numOfMinutes(6, 2, [2,2,-1,2,2,2], [0,0,1,0,0,0]) # 1
    examples.numOfMinutes(7, 6, [1,2,3,4,5,6,-1], [0,6,5,4,3,2,1]) # 21
    examples.numOfMinutes(15, 0, [-1,0,0,1,1,2,2,3,3,4,4,5,5,6,6], [1,1,1,1,1,1,1,0,0,0,0,0,0,0,0]) # 3
    examples.numOfMinutes(4, 2, [3,3,-1,2], [0,0,162,914]) # 1076
            