## Code Challenge: Anagram Difference & Minimum Num of Steps to Make Two Strings Anagrams

**two problems with very similar solutions.**

**Combined prompt:**
Gven two arrays containing strings, we want to know minimum number of characters in either string that we must modify to make the two strings at each index anagrams. If it's not possible to make the two strings anagrams, we consider this number to be -1. 

The function must return an array of integers which denote the minimum number of characters in either string that need to be modified to make the two strings anagrams. 

Each strings consists of lowercase characters [a-z]. 
1 <= array.length <= 100

#### Example 1:
```
Input: a = ['a', 'jk', 'abb', 'mn', 'abc'] b = ['bb', 'kj', 'bbc', 'op', 'def']
Output: [-1, 0, 1, 2, 3]
```

Source: Leetcode and HackerRank
* https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/