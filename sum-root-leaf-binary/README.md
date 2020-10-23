## Code Challenge: Sum of Root to Leaf Binary Numbers
You are given the `root` of binary tree where each node has a value of `0` or `1`. Each root-to-leaf path represents a binary umber starting from the most significant bit. For example, if the path is `0 -> 1 -> 1 -> 0 -> 1`, then this could represent `01101` in binary, which is `13`.

For all leaves in the tree, consider the numbers represented by the path from the root to that leaf.

Return the sum of these numbers. The answer is guaranteed to fit in a 32-bits integer.

#### Example 1:
```
Input: root = [1,0,1,0,1,0,1]
OUtput: 22
Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22
```

Source: Leetcode
* https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/
