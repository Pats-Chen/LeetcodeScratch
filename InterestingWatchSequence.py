#! /usr/bin/env python3

# problem description
# https://www.fastprep.io/problems/tiktok-interesting-watch-sequence
# test case 1 input
# videoRatings = [1, 10, 4, 5, 3]
# test case 1 output
# 1
# custom test case 1 input
# videoRatings = [1, 5, 10, 2, 3, 4, 6]
# custom test case 1 output
# 2

class Solution:
    def minDiscardToMakeSequenceCoherent(self, videoRatings: list[int]) -> int:
        # Solution by ChatGPT
        n = len(videoRatings)
        # Step 1: Calculate LIS ending at each index
        def calculate_lis(arr):
            dp = [1] * len(arr)  # dp[i] = LIS ending at i
            for i in range(1, len(arr)):
                for j in range(i):
                    if arr[i] > arr[j]:
                        dp[i] = max(dp[i], dp[j] + 1)
            return dp

        # Step 2: LIS from left-to-right and right-to-left
        left_lis = calculate_lis(videoRatings)
        right_lis = calculate_lis(videoRatings[::-1])[::-1]

        # Step 3: Find the minimum removals to make the array coherent
        min_removals = float('inf')
        for i in range(n):
            # Total LIS when keeping the left and right parts around index i
            max_lis = left_lis[i] + right_lis[i] - 1
            min_removals = min(min_removals, n - max_lis)

        return min_removals


if __name__ == "__main__":
    testSolution = Solution()
    print(testSolution.minDiscardToMakeSequenceCoherent([1, 10, 4, 5, 3]))
    print(testSolution.minDiscardToMakeSequenceCoherent([1, 5, 10, 2, 3, 4, 6]))