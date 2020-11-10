# Code Challenge Series: Jump Game I, II, III

## Jump Game
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

#### Example 1:
```
Input: [2,3,1,1,4]
Output: True
```

#### Example 2:
```
Input: [3,2,1,0,4]
Output: False
```

Source: Leetcode
* https://leetcode.com/problems/jump-game/


## Jump Game III
Given an array of non-negative integers `arr`, you are initially positioned at `start` index of the array. When you are at index `i`, you can jump to `i + arr[i]` or `i - arr[i]`, check if you can reach to **any** index with value 0.

Notice that you can not jump outside of the array at any time.

Constraints:
```
* 1 <= arr.length <= 5 * 10^4
* 0 <= arr[i] < arr.length
* 0 <= start < arr.length
```

Source: Leetcode
* https://leetcode.com/problems/jump-game-iii/
