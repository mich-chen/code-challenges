### Greedy
* https://leetcode.com/problems/assign-cookies/
* https://www.hackerrank.com/challenges/mark-and-toys/problem

**Tell-tale signs of a problem where greedy may be applicable, but isn't immediately apparent.**:
* Choice of element depends only on immediate neighbors
* Answer is non-decresing or non-increasing (sorting)
* Anything requires lexicographically largest or smallest of something
* Anything processing the input in sorted order will help
* Anywhere processing input in forward or reverse (as given) will help
* ANything requires you to track min or max of something (similar to sliding window approach).
* Can I make the argument that greedy is no worse than optimal solution?
