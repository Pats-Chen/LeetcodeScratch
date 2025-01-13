#! /usr/bin/env python3

# problem description
# https://www.fastprep.io/problems/tiktok-maximize-processing-power
# test case 1 input
# processingPower = [1, 3, 9, 2, 3]
# test case 1 output
# 16
# test case 2 input
# processingPower = [3, 3, 5, 5, 2, 2, 5]
# test case 2 output
# 21
# test case 3 input
# processingPower = [8, 5, 1, 5]
# test case 3 output
# 19

class Solution:
    def maximizeProcessingPower(self, processingPower: list[int]) -> int:
        freq = [0] * 100002
        for i in range(len(processingPower)):
            freq[processingPower[i]] += 1
        dp = [0] * 100002
        dp[1] = freq[1]
        for i in range(2, 100001):
            dp[i] = max(dp[i - 2] + i * freq[i], dp[i - 1])
        return dp[100000]



if __name__ == "__main__":
    testSolution = Solution()
    print(testSolution.maximizeProcessingPower([1, 3, 9, 2, 3]))
    print(testSolution.maximizeProcessingPower([3, 3, 5, 5, 2, 2, 5]))
    print(testSolution.maximizeProcessingPower([8, 5, 1, 5]))