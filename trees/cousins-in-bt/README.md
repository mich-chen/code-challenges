## Code Challenge: Cousins in Binary Tree
In a binary tree, the root node is at depth `0`, and children of each depth `k` node are at depth `k+1`.

Two nodes of a binary tree are cousins if they have the same depth, but have **different parents**.

We are given the `roor` of binary tree with unique values, and the values `x` and `y` of two different nodes in the tree.

Return `True` if and only if the nodes corresponding to the values `x` and `y` are cousins.

#### Example 1:
```
Input: root = [1,2,3,4], x = 4, y = 3
Output: False
```

#### Example 2:
```
Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
Output: True
```

Source: Leetcode
* https://leetcode.com/problems/cousins-in-binary-tree/