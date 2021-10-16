class Solution:
    def numSquares(self, n: int) -> int:
        if n <= 3:
            return n
        sqrtNum = (n ** 0.5)
        if int(sqrtNum) == sqrtNum:
            return 1
        dp = [i for i in range(n + 1)]
        for idx in range(4, n + 1):
            j, jSqr = 1, 1
            while jSqr <= idx:
                dp[idx] = min(dp[idx], dp[idx - jSqr] + 1)
                j += 1
                jSqr = j * j
                # If I write jSqr = j ** 2, Leetcode Judger will report Time Limit Exceeded. Why?
        return dp[-1]
