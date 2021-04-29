class Solution:
    def fib(self, N: int) -> int:
        
        # cache already calculated f(N) values
        # index in self.dp list represents N
        # dp[N] represents calculated fibonacci value
        self.dp = [None] * (N + 1)

        return self.recurse(N, self.dp)
    
    def recurse(self, N, dp):
        """Calculate fibonacci number recursively"""

        if N <= 1:
            return N
        
        # if dp[N] not cached yet, cache the fib value by recursing
        if not self.dp[N]:
            self.dp[N] = self.recurse(N-1, self.dp) + self.recurse(N-2, self.dp)
        
        # if cached fib number exists, return
        return dp[N]

    def fib_iterative_dp(self, N:int) -> int:
        """iterative and dp to store fib numbers solution."""

        # base case
        if N <= 1:
            return N

        dp = [0,1]

        for i in range(2, N + 1):
            dp.append(dp[i-1] + dp[i-2])

        return dp[N]

    def fib_recursive(self, N:int) -> int:
        """Recursive solution using one function."""
        # base case
        if N <= 1:
            return N
        else:
            return self.fib_recursive(N-1) + self.fib_recursive(N-2)
        

if __name__ == '__main__':

    example1 = Solution()
    print(example1.fib(4)) # 3
    example2 = Solution()
    print(example2.fib(30)) # 832040
    print(example2.fib_iterative_dp(30)) # 832040
    print(example1.fib_recursive(4)) # 3


