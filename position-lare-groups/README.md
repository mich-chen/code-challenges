## Code Challenge: Positions of Large Groups
in a string `s` of lowercase letters, these letters form consecuritve groups of the same character.

A group is indentified by an interval `[start, end]`, where `start` and `end` denote the start and end indices (inclusive) of the group.

A group is considered **large** if it has 3 or more characters.

Return the intervals of every large group sorted in increasing order by start index.

#### Example 1:
```
Input: s = "abbxxxxzzy"
Output: [[3,6]]
```

#### Example 2:
```
Input: s = "abcdddeeeeaabbbcd"
Output: [[3,5],[6,9],[12,14]]
```

#### Example 3:
```
Input: s = "abc"
Output: []
```

Source: Leetcode
* https://leetcode.com/problems/positions-of-large-groups/