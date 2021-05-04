class Solution:
    def climbStairs(self, n: int) -> int:

        # base case
        if n <= 2:
            return n

        # very similar to fib
        # cache already calculated steps
        # fill in steps with known num of ways --> no zero indexing for easier understanding of current step
        dp = [0] * n
        dp[0], dp[1] = 1, 2

        # to calculate ith step:
        #   add up num ways of i - 1 step and i - 2 step.
        #   i-1 step represents option to climb 1 step to current step
        #   i-2 step represents option to climb 2 steps to current step
        for i in range(2, n):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[-1]

    def climbStairs_constant_space(self, n: int) -> int:

        # base case 
        if n <= 2:
            return n

        one_step_previous = 1
        two_step_previous = 2
        ways = 2 # initialize ways as 2 since n is > 2

        # use pointers to indicate num of ways one step previous and two step previous
        for i in range(2, n):
            ways = one_step_previous + two_step_previous
            # move pointers accordingly
            one_step_previous = two_step_previous
            two_step_previous = ways # ways now represents i - 1 for next interation

        return ways

    def climbStairs_recurseively(self, n: int) -> int:
        
        # base case
        if n <= 2:
            return n

        dp = {1:1, 2:2}
        self.recurse(n, dp)
        return dp[n]

    def recurse(self, step, dp):
        if step <= 2:
            return step

        # if step's ways is not cached in dp
        if step not in dp:
            # calculate one previous step and two previous step by recursion
            dp[step] = self.recurse(step - 1, dp) + self.recurse(step - 2, dp)
        
        # return cached step's ways
        return dp[step]


if __name__ == '__main__':

    example = Solution()
    print(example.climbStairs(5)) # 8
    print(example.climbStairs(38)) # 63245986
    print(example.climbStairs_constant_space(5))
    print(example.climbStairs_constant_space(38))
    print(example.climbStairs_recurseively(5))
    print(example.climbStairs_recurseively(38))
