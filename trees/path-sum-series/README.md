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


## Binary Tree Maximum Path Sum

A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any path.

#### Example 1:
```
Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.
```

####  Example 2:
```
Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.
```

#### Example 3:
```
Input: [-3]
Output: -3
```

**Constraints:**
* The number of nodes in the tree is in the range [1, 3 * 104].
* -1000 <= Node.val <= 1000

Source: Leetcode
* https://leetcode.com/problems/binary-tree-maximum-path-sum/
