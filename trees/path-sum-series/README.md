# Code Challenge: Path Sum series

## Path Sum I
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

Return True or False if there exist a root-to-leaf path which sums to given sum.

#### Example 1:
```
Input: [5,4,8,11,null,13,4,7,2,null,null,null,1] sum = 22
Output: True
```

Source: Leetcode
* https://leetcode.com/problems/path-sum/


## Path Sum II
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Return a 2d list of each path's values in a list. (ex: [[1, 2, 3], [4, 5, 6]])

#### Example 1:
```
Input: [5,4,8,11,null,13,4,7,2,null,null,5,1] sum = 22
Output: [
   [5,4,11,2],
   [5,8,4,5]
]
```

Source: Leetcode
* https://leetcode.com/problems/path-sum-ii/


## Path Sum III
You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

#### Example 1:
```
Input: [1,-2,-3] sum = -1
Output: 1
```

#### Example 2:
```
Input: [10,5,-3,3,2,null,11,3,-2,null,1] sum = 8
Output: 3
```

Source: Leetcode
* https://leetcode.com/problems/path-sum-iii/