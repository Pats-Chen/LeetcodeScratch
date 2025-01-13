#! /usr/bin/env python3
from heapq import heappop, heappush

# problem description
# https://www.fastprep.io/problems/tiktok-get-total-impact
# test case 1 input
# initialReelImpacts = [2, 3], newReelImpacts = [4, 5, 1], k = 2
# test case 1 output
# 13

class Solution:
    def getTotalImpact(self, initialReelImpacts: list[int], newReelImpacts: list[int], k: int) -> int:
        minHeap = []
        minSize = k - 1
        maxHeap = []
        for impact in initialReelImpacts:
            heappush(minHeap, impact)
            if len(minHeap) > minSize:
                cand = heappop(minHeap)
                heappush(maxHeap, 0 - cand)
        result = 0 - maxHeap[0]
        for newImpact in newReelImpacts:
            heappush(minHeap, newImpact)
            if len(minHeap) > minSize:
                cand = heappop(minHeap)
                heappush(maxHeap, 0 - cand)
            result += 0 - maxHeap[0]
        return result


if __name__ == "__main__":
    testSolution = Solution()
    print(testSolution.getTotalImpact([2, 3], [4, 5, 1], 2))