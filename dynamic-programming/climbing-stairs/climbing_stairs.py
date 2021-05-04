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

if __name__ == '__main__':

    example = Solution()
    print(example.climbStairs(5)) # 8
    print(example.climbStairs(38)) # 63245986
