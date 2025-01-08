#! /usr/bin/env python3
from heapq import heappop, heappush

# test case 1 input
# s = ")(("
# kitParentheses = ")(()))"
# efficiencyRatings = [3, 4, 2, -4, -1, -3]
# test case 1 output
# 6

class Solution:
    def maximizeEfficiencyScore(self, s: str, kitParentheses: str, efficiencyRatings: list[int]) -> int:
        d = dict()
        for idx in range(len(kitParentheses)):
            if kitParentheses[idx] not in d:
                d[kitParentheses[idx]] = []
            heappush(d[kitParentheses[idx]], 0 - efficiencyRatings[idx])
        
        # print(d["("], d[")"])
        maxScore = 0
        for p in s:
            if p == "(":
                currScore = 0 - heappop(d[")"])
            else:
                currScore = 0 - heappop(d["("])
            maxScore += currScore

        # print(maxScore, d["("], d[")"])
        while d["("] and d[")"] and d["("][0] < 0 and d[")"][0] < 0:
            maxScore += (0 - heappop(d[")"]) + 0 - heappop(d["("]))
        return maxScore

if __name__ == "__main__":
    testSolution = Solution()
    print(testSolution.maximizeEfficiencyScore(")((", ")(()))", [3, 4, 2, -4, -1, -3]))