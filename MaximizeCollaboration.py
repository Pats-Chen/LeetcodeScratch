#! /usr/bin/env python3

# problem description
# https://www.fastprep.io/problems/tiktok-create-maximum-collaborations
# test case 1 input
# creatorsEngagementPower = [4, 4, 3, 6, 4, 3, 5]
# minCreatorsRequired = 2
# minTotalEngagementPowerRequired = 8
# test case 1 output
# 3
# test case 2 input
# creatorsEngagementPower = [5, 4, 3, 2, 1]
# minCreatorsRequired = 3
# minTotalEngagementPowerRequired = 20
# test case 2 output
# 0
# test case 3 input
# creatorsEngagementPower = [4, 6, 8, 11, 9, 12]
# minCreatorsRequired = 2
# minTotalEngagementPowerRequired = 15
# test case 3 output
# 2

class Solution:
    def createMaximumCollaborations(self, creatorsEngagementPower: list[int], minCreatorsRequired: int, minTotalEngagementPowerRequired: int) -> int:
        # Solution by ChatGPT
        validList = []
        start = 0
        currSum = 0

        for end in range(len(creatorsEngagementPower)):
            currSum += creatorsEngagementPower[end]

            # 保证窗口长度至少为 minCreatorsRequired
            while end - start + 1 >= minCreatorsRequired and currSum >= minTotalEngagementPowerRequired:
                validList.append((start, end))
                currSum -= creatorsEngagementPower[start]
                start += 1
        # End of solution by ChatGPT

        if not validList:
            return 0
        lastValid = validList[0]
        count = 1
        for idx in range(1, len(validList)):
            if validList[idx][0] > lastValid[1]:
                count += 1
                lastValid = validList[idx]
        return count


if __name__ == "__main__":
    testSolution = Solution()
    print(testSolution.createMaximumCollaborations([4, 4, 3, 6, 4, 3, 5], 2, 8))
    print(testSolution.createMaximumCollaborations([5, 4, 3, 2, 1], 3, 20))
    print(testSolution.createMaximumCollaborations([4, 6, 8, 11, 9, 12], 2, 15))